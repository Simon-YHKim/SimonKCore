---
name: find-skill
description: >
  Use when the user wants find skill — triggers "스킬 찾아", "스킬 검색", "이런 거 하는 스킬", "find a skill", "search skills", "is there a skill for", or /find-skill. Produces 외부 awesome-claude-skills (26k+ star GitHub 카탈로그) 검색 + SimonK Stack INDEX.md 검색을 합쳐 사용자가 원하는 기능을 가진 skill 추천. 키워드에서 매칭되는 외부 skill 이름·URL 과 내부 등가물 비교. WebFetch 기반 slim 구현. Different from INDEX.md browse (manual) — this is automated search. Different from /skill-gen-agent (creates new skills) — this finds existing ones.
version: 1.0.0
allowed-tools:
  - WebFetch
  - Read
  - Bash
---

# /find-skill

외부 awesome-claude-skills (26k+ star GitHub 카탈로그) 검색 + SimonK Stack INDEX.md 검색을 합쳐 사용자가 원하는 기능을 가진 skill 추천. 키워드에서 매칭되는 외부 skill 이름·URL 과 내부 등가물 비교. WebFetch 기반 slim 구현.

## When to use

Trigger phrases:
- Korean: 스킬 찾아, 스킬 검색, 이런 거 하는 스킬
- English: find a skill, search skills, is there a skill for
- Slash: `/find-skill`

## What it does

외부 awesome-claude-skills (26k+ star GitHub 카탈로그) 검색 + SimonK Stack INDEX.md 검색을 합쳐 사용자가 원하는 기능을 가진 skill 추천. 키워드에서 매칭되는 외부 skill 이름·URL 과 내부 등가물 비교. WebFetch 기반 slim 구현.

## Boundaries

Different from INDEX.md browse (manual) — this is automated search. Different from /skill-gen-agent (creates new skills) — this finds existing ones.

## Operational notes

- 검증 가능 산출물: 사용자가 직접 확인 가능한 파일/URL 우선 생성
- 외부 의존: SKILL body 에 명시 (Vercel CLI, Expo CLI, LaTeX 등)
- 실패 시: 어떤 단계에서 막혔는지 명시, 사용자 결정 받기

## 완료 보고 (HTML) — 표준
작업을 끝내면 **HTML 완료 보고서**를 생성한다 (SimonKCore `completion-report` 표준).
- 첫 화면은 **심플 요약**(한눈 카드 한 줄) + 직관 그래픽/차트(인라인 SVG)·이미지.
- 각 항목 옆 **[자세히] 버튼**(`<details>`)을 펼치면 상세 — 처음부터 쏟지 않는다(progressive disclosure).
- 자체완결 1파일(인라인 CSS/SVG, 무JS) · 사용자 언어 · 현지시간 스탬프.
- Core 있으면 `completion-report` 호출, 없으면 동일 형식으로 인라인 생성.
