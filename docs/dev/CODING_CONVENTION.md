# 코딩 컨벤션

> **Refs**: [ARCHITECTURE](./ARCHITECTURE.md) · [RULES](../agent/RULES.md)

## 스택
- {프레임워크 (예: Next.js 15 App Router)}
- {언어 (예: TypeScript strict mode)}
- {스타일링 (예: Tailwind CSS)}

## 네이밍
| 대상 | 규칙 | 예 |
|---|---|---|
| 파일 | {예: kebab-case} | `user-card.tsx` |
| 컴포넌트 | {예: PascalCase} | `UserCard` |
| 함수/변수 | {예: camelCase} | `getUser` |
| 타입/인터페이스 | {예: PascalCase} | `UserDto` |
| 상수 | {예: UPPER_SNAKE} | `MAX_RETRIES` |

## 타입 규칙
- {예: `any` 금지. unknown + 좁히기 사용}
- {예: API 응답은 `types/`에 DTO로 정의}
- {예: 함수 시그니처에 명시적 반환 타입}

## 디렉토리 배치
- 컴포넌트는 `components/`, 타입은 `types/`에 분리한다.
- {추가 규칙}

## 금지 규칙
- CRITICAL: 클라이언트 컴포넌트에서 직접 외부 API를 호출하지 않는다.
- {예: console.log 커밋 금지}
- {예: 기본 export 금지 — named export만}

## 커밋
- conventional commits 형식 (`feat:`, `fix:`, `docs:`, `refactor:`).
