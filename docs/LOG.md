# LOG (append-only)

docs 위키의 변경 로그. 의미 있는 변경마다 한 줄을 **추가만** 한다(기존 줄 수정·삭제 금지).
형식: `## [YYYY-MM-DD] {종류} | {요약}` — 종류: `ingest`(새 정본/결정) · `update`(정본 갱신) · `lint`(정합성 점검) · `promote`(ISSUE→RULES 승격).

## [2026-06-13] ingest | 역할별 docs 위키 구성(user·dev·design·security·agent) + LLM Wiki 라우팅·Refs·LOG 도입
