"""log_prompt.py (UserPromptSubmit 훅) 단위 테스트.

훅을 서브프로세스로 실행해, 사용자 프롬프트가 prompts-logs/prompts.jsonl 에
JSONL 한 줄로 append 되는지 검증한다.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

HOOK = Path(__file__).resolve().parent / "log_prompt.py"


def run_hook(payload: dict, project_dir: Path) -> subprocess.CompletedProcess:
    env = {**os.environ, "CLAUDE_PROJECT_DIR": str(project_dir)}
    return subprocess.run(
        [sys.executable, str(HOOK)],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        env=env,
    )


def read_log(project_dir: Path) -> list[dict]:
    logf = project_dir / "prompts-logs" / "prompts.jsonl"
    return [json.loads(line) for line in logf.read_text(encoding="utf-8").splitlines()]


def test_writes_record(tmp_path):
    r = run_hook({"session_id": "s1", "cwd": "/x", "prompt": "hello"}, tmp_path)
    assert r.returncode == 0
    rec = read_log(tmp_path)[0]
    assert rec["prompt"] == "hello"
    assert rec["session_id"] == "s1"
    assert rec["cwd"] == "/x"
    assert rec["ts"]  # 타임스탬프 존재


def test_appends_in_order(tmp_path):
    run_hook({"prompt": "a"}, tmp_path)
    run_hook({"prompt": "b"}, tmp_path)
    recs = read_log(tmp_path)
    assert [r["prompt"] for r in recs] == ["a", "b"]


def test_no_stdout(tmp_path):
    # UserPromptSubmit 은 exit 0 시 stdout 을 컨텍스트에 주입한다 → 반드시 비어 있어야 한다.
    r = run_hook({"prompt": "x"}, tmp_path)
    assert r.stdout == ""


def test_missing_prompt_is_ok(tmp_path):
    r = run_hook({}, tmp_path)
    assert r.returncode == 0
    assert read_log(tmp_path)[0]["prompt"] == ""


def test_invalid_stdin_does_not_crash(tmp_path):
    env = {**os.environ, "CLAUDE_PROJECT_DIR": str(tmp_path)}
    r = subprocess.run(
        [sys.executable, str(HOOK)],
        input="not-json",
        capture_output=True,
        text=True,
        env=env,
    )
    assert r.returncode == 0  # 훅은 절대 프롬프트 제출을 막지 않는다


def test_multiline_and_unicode_preserved(tmp_path):
    prompt = "여러 줄\n프롬프트 🍓"
    run_hook({"prompt": prompt}, tmp_path)
    assert read_log(tmp_path)[0]["prompt"] == prompt
