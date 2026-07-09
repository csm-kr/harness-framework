#!/usr/bin/env python3
"""UserPromptSubmit 훅 — 모든 사용자 프롬프트를 prompts-logs/prompts.jsonl 에 append 한다.

프로젝트 분석용 프롬프트 로그. Claude Code 가 프롬프트 제출 시 훅 JSON 을 stdin 으로 준다.
stdout 으로는 아무것도 출력하지 않는다: UserPromptSubmit 은 exit 0 시 stdout 을
프롬프트 컨텍스트에 주입하므로, 로그만 남기고 조용히 통과시킨다.
로깅 실패가 사용자의 프롬프트 제출을 막아서는 안 되므로 항상 exit 0 한다.
"""
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        payload = {}

    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", ".")
    log_dir = Path(project_dir) / "prompts-logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    record = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "session_id": payload.get("session_id", ""),
        "cwd": payload.get("cwd", ""),
        "prompt": payload.get("prompt", ""),
    }
    with (log_dir / "prompts.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        # 어떤 이유로도 프롬프트 제출을 막지 않는다.
        sys.exit(0)
