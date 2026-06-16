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

## 수록 스킬 (56개)

공유 인프라 스킬 — 다른 플러그인/오케스트레이터가 호출하거나 직접 사용.

`agent-delegate` · `careful` · `caveman` · `checkpoint` · `completion-report` · `defuddle` · `designmd-upgrade` · `domain-glossary` · `find-skill` · `founder-context` · `gcloud-helper` · `grill-me` · `gstack-upgrade` · `html-default-output` · `human-voice-guard` · `json-canvas` · `keepass-helper` · `learn` · `llm-wiki-builder` · `model-router` · `multi-terminal-dispatcher` · `notebooklm-import` · `obsidian-bases` · `obsidian-cli` · `obsidian-markdown` · `office-docs` · `office-hours` · `omc-upgrade` · `omo-upgrade` · `opencowork-upgrade` · `open-gstack-browser` · `openharness-upgrade` · `pair-agent` · `persona-validate` · `perspectives` · `plan-ceo-review` · `project-context-md` · `session-context-export` · `session-context-tracker` · `session-start-hook` · `setup-browser-cookies` · `simon-handoff` · `simon-instincts` · `simonk` · `simonk-report` · `simon-ohmo` · `simon-research` · `simon-worktree` · `sprint-optimizer` · `stack-update` · `tech-preference-tracker` · `unfreeze` · `web-publisher` · `wiki-ingest` · `wiki-lint` · `wiki-query`
