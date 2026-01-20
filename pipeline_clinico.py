from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional, Literal, TypedDict
from pydantic import BaseModel, Field, ValidationError
from langgraph.graph import StateGraph, END

BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "data" / "input"
PROMPTS_DIR = BASE_DIR / "prompts"
OUT_PATH = BASE_DIR / "results.json"


# =========================
# 1. Pydantic Schemas (Exigência do Case)
# =========================

class RiskAssessment(BaseModel):
    level: Literal["baixo", "médio", "alto"]
    signals: List[str]


class ClinicalReport(BaseModel):
    required: bool
    summary: str


class ClinicalOutput(BaseModel):
    analysis: str = Field(description="Análise clínica estruturada")
    themes: List[str] = Field(min_length=3, max_length=6)
    signifiers: List[str] = Field(min_length=3, max_length=8)
    hypotheses: List[str] = Field(min_length=2, max_length=4)
    questions: List[str] = Field(min_length=3, max_length=6)
    risk_assessment: RiskAssessment
    clinical_report: ClinicalReport


# =========================
# 2. State & IO Helpers
# =========================

class ClinicalState(TypedDict):
    filename: str
    input_text: str
    prompt_version: str
    raw_response: Optional[str]
    parsed_output: Optional[ClinicalOutput]
    errors: List[str]


def load_prompt(version: str) -> str:
    path = PROMPTS_DIR / f"prompt_{version}.txt"
    return path.read_text(encoding="utf-8") if path.exists() else "Analise: {INPUT}"


def read_inputs(input_dir: Path) -> List[Tuple[str, str]]:
    if not input_dir.exists():
        return []
    return [(f.name, f.read_text(encoding="utf-8")) for f in input_dir.glob("*.txt")]


def call_model(prompt: str) -> str:
    # Mock com dados que passam exatamente na validação do Pydantic
    mock_response = {
        "analysis": "O paciente apresenta resistência inicial e fragmentação subjetiva importante no discurso.",
        "themes": ["Angústia", "Resistência", "Desejo Inconsciente"],
        "signifiers": ["atraso", "silêncio", "mãe", "repetição"],
        "hypotheses": ["Neurose de transferência", "Inibição intelectual"],
        "questions": ["Por que o atraso?", "Qual o papel da mãe?", "O que silencia agora?"],
        "risk_assessment": {"level": "baixo", "signals": ["Boa aliança terapêutica"]},
        "clinical_report": {"required": False, "summary": "Paciente estável emocionalmente."}
    }
    return json.dumps(mock_response)


# =========================
# 3. LangGraph Nodes (Orquestração)
# =========================

def generation_node(state: ClinicalState) -> ClinicalState:
    print(f"--- Node: Generation ({state['filename']}) ---")
    template = load_prompt(state['prompt_version'])
    prompt = template.replace("{INPUT}", state['input_text'])
    response_str = call_model(prompt)
    return {"raw_response": response_str}


def validation_node(state: ClinicalState) -> ClinicalState:
    print("--- Node: Validation ---")
    raw = state.get("raw_response", "")
    try:
        parsed_obj = ClinicalOutput.model_validate_json(raw)
        return {"parsed_output": parsed_obj, "errors": []}
    except Exception as e:
        return {"parsed_output": None, "errors": [str(e)]}


# =========================
# 4. Graph & Execution
# =========================

def build_graph() -> StateGraph:
    workflow = StateGraph(ClinicalState)
    workflow.add_node("generator", generation_node)
    workflow.add_node("validator", validation_node)
    workflow.set_entry_point("generator")
    workflow.add_edge("generator", "validator")
    workflow.add_edge("validator", END)
    return workflow.compile()


def main(prompt_version: str = "v2"):
    items = read_inputs(INPUT_DIR)
    if not items:
        print("Erro: Nenhum arquivo .txt encontrado em data/input/")
        return

    app = build_graph()
    results = []
    ok_count = 0

    print(f"Iniciando Pipeline (LangGraph + Pydantic) - Prompt {prompt_version}...\n")

    for fname, text in items:
        initial_state = {
            "filename": fname,
            "input_text": text,
            "prompt_version": prompt_version,
            "raw_response": None,
            "parsed_output": None,
            "errors": []
        }

        final_state = app.invoke(initial_state)

        is_ok = final_state["parsed_output"] is not None and not final_state["errors"]
        if is_ok: ok_count += 1

        results.append({
            "file": fname,
            "ok": is_ok,
            "errors": final_state["errors"],
            "output": final_state["parsed_output"].model_dump() if is_ok else None
        })

    payload = {"total": len(results), "ok": ok_count, "results": results}
    OUT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    print(f"Sucesso: {ok_count} | Falhas: {len(results) - ok_count}")


if __name__ == "__main__":
    main()