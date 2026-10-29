"""Offline-Sanity-Checks; keine Streamlit-Sitzung oder Modellverbindung erforderlich."""
import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_python_syntax():
    for name in ("app.py", "conference_mode.py", "topics.py"):
        ast.parse((ROOT / name).read_text(encoding="utf-8"), filename=name)

def test_dependencies_present():
    text = (ROOT / "requirements.txt").read_text(encoding="utf-8")
    assert "streamlit" in text and "openai" in text

def test_required_files():
    assert all((ROOT / name).exists() for name in ("app.py", "conference_mode.py", "topics.py", "requirements.txt"))
