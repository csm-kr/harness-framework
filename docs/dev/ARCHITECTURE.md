# 아키텍처

> **Refs**: [ADR](../agent/ADR.md) · [DB](./DB.md) · [API](./API.md) · [STATE](../agent/STATE.md) · [RULES](../agent/RULES.md)

## 디렉토리 구조
```
src/
├── app/               # 페이지 + API 라우트
├── components/        # UI 컴포넌트
├── types/             # TypeScript 타입 정의
├── lib/               # 유틸리티 + 헬퍼
└── services/          # 외부 API 래퍼
```

## 패턴
{사용하는 디자인 패턴 (예: Server Components 기본, 인터랙션이 필요한 곳만 Client Component)}

## 데이터 흐름
```
{데이터가 어떻게 흐르는지 (예:
사용자 입력 → Client Component → API Route → 외부 API → 응답 → UI 업데이트
)}
```

## 상태 관리
{상태 관리 방식 (예: 서버 상태는 Server Components, 클라이언트 상태는 useState/useReducer)}
앱 레벨 vs 서버 영속 상태 구분은 [STATE](../agent/STATE.md) 참조.

## 프로덕션 스택
| 레이어 | 사용 기술 | 비고 |
|---|---|---|
| 프레임워크 | {예: Next.js 15} | |
| DB | {예: SQLite + Prisma} | 스키마는 [DB](./DB.md) |
| 인증 | {예: NextAuth} | |
| 호스팅 | {예: Vercel} | |

## 교체표 (MVP → 프로덕션)
개발 편의를 위한 MVP 선택과, 확장 시 교체할 대상을 명시한다.

| 항목 | MVP | 프로덕션 교체 | 교체 트리거 |
|---|---|---|---|
| {예: DB} | {SQLite} | {Postgres} | {동시 사용자 N 이상} |
| {예: 파일 저장} | {로컬 FS} | {S3} | {배포 환경 멀티 인스턴스} |
