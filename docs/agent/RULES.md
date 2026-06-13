# 불변 규칙 (RULES)

> **Refs**: [ISSUES](./ISSUES.md) · [ADR](./ADR.md) · [ARCHITECTURE](../dev/ARCHITECTURE.md) · [SECURITY](../security/SECURITY.md)

절대 어기면 안 되는 규칙. 모든 step·리뷰는 이 규칙을 기준으로 검증한다. CLAUDE.md의 CRITICAL 규칙과 함께 최우선으로 적용된다.

규칙은 두 경로로 추가된다: (1) 설계 시 합의된 불변 조건, (2) [ISSUES](./ISSUES.md)에서 **3회 이상 반복된 이슈가 승격된 것**. 후자는 출처 이슈 번호를 함께 적는다.

## 아키텍처
- R1: 모든 외부 API/DB 접근은 서버(`app/api/` route handler, `services/`)에서만 한다. 클라이언트에서 직접 호출 금지.
- R2: [ARCHITECTURE](../dev/ARCHITECTURE.md)의 디렉토리 구조를 벗어나지 않는다.

## 보안
- R3: 리소스 접근은 서버에서 소유자/권한을 검증한다 ([SECURITY](../security/SECURITY.md)).
- R4: 비밀 값을 코드·로그·클라이언트 번들에 노출하지 않는다.

## 데이터
- R5: 스키마 변경은 마이그레이션으로만 한다 ([DB](../dev/DB.md)). 수동 SQL 금지.
- R6: 파괴적 작업(삭제·덮어쓰기)은 되돌릴 수 없으므로 명시적 확인 없이 수행하지 않는다.

## 프로세스
- R7: 새 기능은 테스트를 먼저 작성한다 (TDD).
- R8: 기존 테스트를 깨뜨린 채로 step을 완료(completed)로 표시하지 않는다.

## 이슈에서 승격된 규칙
ISSUES.md에서 3회 이상 반복되어 승격된 규칙을 여기에 기록한다(출처 이슈 번호 포함).

- {예: R9 (← ISSUES F1, 3회 반복): 클라이언트에서 외부 API 직접 호출 금지}

> 새 규칙을 추가할 때는 번호를 이어가고, 위반 시 영향을 한 줄로 적는다.
