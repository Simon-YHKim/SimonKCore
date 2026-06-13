---
name: completion-report
description: >
  플러그인 작업 완료 후 자체완결 HTML 보고서를 생성한다 — 이미지/스크린샷·표·차트(인라인 SVG)를 적극 사용하고,
  사용자 언어로 작성하며, 현지 시간을 불러와 로케일 형식으로 완료 시각을 남긴다. 트리거 "작업 보고서", "완료 리포트",
  "HTML 보고", "결과 보고서 만들어", "completion report", /completion-report. 모든 오케스트레이터(skstack·skdesign·
  skmarket·skaihub)가 완료 직후 호출하는 공용 스킬(SimonKCore).
allowed-tools:
  - Read
  - Write
  - Bash
  - Glob
  - Grep
---

# /completion-report — 완료 보고 HTML (사용자 언어 + 현지시간)

작업이 끝나면 "무엇을·어떻게·결과"를 한 장의 HTML로. **글보다 시각**(표·차트·이미지)이 우선.

## 0. 원칙
- **자체완결 HTML** — 인라인 CSS + 인라인 SVG 차트. 외부 의존·빌드 없음. 어디서 열어도 동일.
- **사용자 언어** — 대화에서 쓰인 언어로 보고서 전체 작성(한국어면 한국어, 영어면 영어 …).
- **시각 우선** — 표 + 차트(인라인 SVG bar/line/donut) + 이미지/스크린샷 적극. 설명이 길면 그래픽이 실패한 것.
- **현지 시간 명시** — 완료 시각을 로케일 형식으로(아래 표). 추정 금지 — 시스템 시간을 실제로 읽는다.

## 1. 완료 시각 (로케일 형식)
`node scripts/localtime.mjs` 실행 → 시스템 타임존을 감지해 형식화. 국가/로케일별 기본 형식:

| 지역 | 형식 |
|---|---|
| 한국 (Asia/Seoul) | `[YYYY-MM-DD / HH:MM:SS KST]` |
| 미국 (America/*) | `[MM/DD/YYYY / hh:MM:SS AM/PM PST]` (12h, TZ 약어) |
| 영국·EU (Europe/*) | `[DD/MM/YYYY / HH:MM:SS CET]` (24h) |
| 일본 (Asia/Tokyo) | `[YYYY-MM-DD / HH:MM:SS JST]` |
| 그 외 | ISO: `[YYYY-MM-DD / HH:MM:SS ±HH:MM]` |

타임존이 사용자와 다르면 `--tz`/`--locale`로 오버라이드. 표에 없는 나라는 그 나라 관용 날짜순서(혹은 ISO) + 해당 TZ 약어로.

## 2. 보고서 섹션 (순서)
1. **헤더** — 작업명 · 플러그인 · **완료 시각(로케일 형식)** · 한 줄 요약
2. **무엇을 했나** — 표(항목 / 상태 / 산출물). 상태는 색 배지(완료/부분/대기)
3. **결과·지표** — 인라인 SVG 차트(전/후 비교 bar, 추세 line, 비율 donut). 숫자가 있으면 반드시 차트로
4. **시각 증거** — 스크린샷/생성 이미지/다이어그램(있으면 `<img>` 임베드 또는 base64). 디자인·UI 작업은 필수
5. **다음 단계** — 남은 일·권장 후속(체크리스트)
6. **푸터** — 생성 시각·도구·관련 링크

## 3. 생성 절차
1. 사용자 언어 확정. `localtime.mjs`로 완료 시각 획득.
2. `templates/report.template.html`을 복제해 섹션 채움(표·SVG 차트·이미지). 데이터 없는 섹션은 생략(빈 차트 금지).
3. `reports/completion-<YYYYMMDD-HHMMSS>.html`로 저장.
4. 사용자에게 파일 경로 안내 + (가능하면) 자동 열기/프리뷰. 파일 경로만 던지지 말 것.

## 4. 차트 가이드 (인라인 SVG)
- bar: 전/후·항목 비교. line: 시간 추세(점수 라운드별 등). donut: 구성비.
- 색은 3색 이내(accent+text+muted), 접근성(대비·라벨). 축·범례·값 라벨 포함. 애니메이션 불필요.

## Boundaries
- 데이터 없는데 차트 만들지 않음(가짜 시각화 금지). 추정 시각 금지(실제 시스템 시간).
- `simonk-report`(하네스 세션 리포트)와 다름 — 이건 **플러그인 작업 완료 보고**(로케일 시간 + 사용자 언어 표준).
관련: [[html-default-output]], [[simonk-report]], [[persona-validate]].
