# SimonKCore

![version](https://img.shields.io/badge/version-0.2.0-5b8cff) ![license](https://img.shields.io/badge/license-MIT-green) [![validate](https://github.com/Simon-YHKim/SimonKCore/actions/workflows/validate-plugin.yml/badge.svg)](https://github.com/Simon-YHKim/SimonKCore/actions/workflows/validate-plugin.yml)

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

## 진입점

Core 는 오케스트레이터가 없는 공유 라이브러리라 대부분의 스킬은 다른 플러그인이 호출하거나 자동 라우팅된다. 사용자가 직접 부르는 슬래시 진입점은 2개:

```
/find-skill   # 원하는 기능의 스킬을 외부 카탈로그 + 내부 INDEX 에서 검색
/simonk       # 통합 자율 팀 하네스 — 진단→분해→병렬실행→검증→push
```

### 사용 예시

```
/find-skill PDF 요약하는 스킬 있어?
/find-skill find a skill for taking screenshots
/simonk 이 레포 스킬 검증 돌리고 통과하면 커밋해줘
/simonk 통합 자율로 끝까지 진행해
```

인자 없이 입력하면 각 스킬이 무엇을 찾을지 / 무엇을 실행할지 먼저 물어본다. 나머지 인프라 스킬(`model-router`, `persona-validate`, `completion-report`, `*-upgrade` 등)은 상위 플러그인·세션 훅이 자동 호출한다.

## 수록 스킬 (56개)

공유 인프라 스킬 — 다른 플러그인/오케스트레이터가 호출하거나 직접 사용.

`agent-delegate` · `careful` · `caveman` · `checkpoint` · `completion-report` · `defuddle` · `designmd-upgrade` · `domain-glossary` · `find-skill` · `founder-context` · `gcloud-helper` · `grill-me` · `gstack-upgrade` · `html-default-output` · `human-voice-guard` · `json-canvas` · `keepass-helper` · `learn` · `llm-wiki-builder` · `model-router` · `multi-terminal-dispatcher` · `notebooklm-import` · `obsidian-bases` · `obsidian-cli` · `obsidian-markdown` · `office-docs` · `office-hours` · `omc-upgrade` · `omo-upgrade` · `opencowork-upgrade` · `open-gstack-browser` · `openharness-upgrade` · `pair-agent` · `persona-validate` · `perspectives` · `plan-ceo-review` · `project-context-md` · `session-context-export` · `session-context-tracker` · `session-start-hook` · `setup-browser-cookies` · `simon-handoff` · `simon-instincts` · `simonk` · `simonk-report` · `simon-ohmo` · `simon-research` · `simon-worktree` · `sprint-optimizer` · `stack-update` · `tech-preference-tracker` · `unfreeze` · `web-publisher` · `wiki-ingest` · `wiki-lint` · `wiki-query`

## 기여

스킬 추가·수정은 **평가셋(`evals/cases.json`) + CI 품질게이트**를 통과해야 한다.
Core 는 공유 인프라라 대부분의 스킬은 커맨드 없이 다른 플러그인이 호출한다 — 진짜 사용자 진입점(`find-skill`·`simonk`)만 `commands/` 에 둔다.
자세한 절차·스키마·도메인 규칙은 [`CONTRIBUTING.md`](./CONTRIBUTING.md) 참고.

```bash
python3 .github/skill-ci/run_ci.py   # 머지 전 로컬 게이트
```

## 라이선스 / 출처

MIT. 일부 인프라 스킬은 Simon 의 기존 SimonK 스택에서 가져왔고 gstack(garrytan, MIT) 출신이 섞일 수 있으며 출처는 각 SKILL.md·NOTICE 에 유지. © Simon Kim (Simon-YHKim).
