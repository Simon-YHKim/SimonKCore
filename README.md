# SimonKCore

> SimonK 플러그인 공유 인프라 (위임·모델라우팅·메모리·지식도구)

공유 라이브러리 — 상위 오케스트레이터 없음. 다른 플러그인이 의존.

## 설치
```
/plugin marketplace add Simon-YHKim/SimonKCore
/plugin install simonk-core@simonk-core
```

## 의존
SimonKCore 권장 동반 설치 (agent-delegate, model-router, instincts 등 공유 인프라). 없으면 일부 기능 제한.

## 구조
- `skills/` — 도메인 스킬
- `agents/` — 서브에이전트
- `commands/` — 슬래시 커맨드

_스킬 목록은 분류 매니페스트 확정 후 채워집니다._
