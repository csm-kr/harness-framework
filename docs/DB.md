# 데이터베이스

> **Refs**: [ARCHITECTURE](./ARCHITECTURE.md) · [API](./API.md) · [STATE](./STATE.md)

## 스키마 (Prisma)
```prisma
// schema.prisma — {SQLite 등 datasource}

model {모델명} {
  id        String   @id @default(cuid())
  createdAt DateTime @default(now())
  // {필드들}
}

// model {다른 모델} { ... }
```

## 모델 설명
| 모델 | 역할 | 핵심 관계 |
|---|---|---|
| {모델명} | {무엇을 표현하는가} | {1:N, N:M 등} |

## 파생값
DB에 저장하지 않고 조회/계산 시 도출하는 값.

| 파생값 | 계산 방식 | 소스 |
|---|---|---|
| {예: 진행률} | {완료 step / 전체 step} | {steps 테이블} |

## 인덱스·제약
- {예: `@@unique([userId, slug])`}
- {예: 조회 패턴에 따른 인덱스}

## 마이그레이션 규칙
- {예: `prisma migrate dev`로만 스키마 변경. 수동 SQL 금지}
