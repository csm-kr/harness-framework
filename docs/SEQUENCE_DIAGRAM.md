# Sequence Diagram

> **Refs**: [API](./API.md) · [SCREEN_FLOW](./SCREEN_FLOW.md)

주요 동작의 컴포넌트 호출 순서를 기술한다. 화면 단위 흐름은 [SCREEN_FLOW](./SCREEN_FLOW.md), API 계약은 [API](./API.md) 참조.

## {동작 1: 예 — 로그인}
```
User → Client: {액션}
Client → API Route: {요청}
API Route → Service: {호출}
Service → 외부 API/DB: {쿼리}
외부 API/DB --> Service: {응답}
Service --> API Route: {결과}
API Route --> Client: {응답}
Client --> User: {UI 갱신}
```

## {동작 2}
```
{동일 형식으로 호출 순서를 기술}
```

## 비동기·백그라운드 동작
{예: LLM 파이프라인처럼 즉시 응답 후 백그라운드로 처리되는 흐름이 있으면 별도로 명시}
- 큐잉 / 폴링 / 웹훅 중 무엇인지
- 상태 전이: pending → processing → done/failed
