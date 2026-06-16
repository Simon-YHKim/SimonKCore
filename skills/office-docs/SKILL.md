---
name: office-docs
description: >
  Use when the user wants office docs — triggers "워드 문서 만들어", "엑셀 만들어", "PPT 만들어", "PDF 만들어", "create docx", "create xlsx", "create pptx", "generate office document", or /office-docs. Produces Anthropic 공식 Big Four 사무 문서 생성 — Docx (Word), Xlsx (Excel multi-sheet), Pptx (PowerPoint), PDF. python-docx / openpyxl / python-pptx / weasyprint 사용. 사용자 요청 분석 후 적절한 형식 자동 선택 또는 명시 형식으로 생성. 차용 출처 Anthropic document-skills Different from /design-html (web HTML), /slides (presentation HTML), /make-pdf gstack (markdown to PDF only). This handles native Office formats.
version: 1.0.0
allowed-tools:
  - Bash
  - Read
  - Write
---

# /office-docs

Anthropic 공식 Big Four 사무 문서 생성 — Docx (Word), Xlsx (Excel multi-sheet), Pptx (PowerPoint), PDF. python-docx / openpyxl / python-pptx / weasyprint 사용. 사용자 요청 분석 후 적절한 형식 자동 선택 또는 명시 형식으로 생성. 차용 출처 Anthropic document-skills

## When to use

Trigger phrases:
- Korean: 워드 문서 만들어, 엑셀 만들어, PPT 만들어, PDF 만들어
- English: create docx, create xlsx, create pptx, generate office document
- Slash: `/office-docs`

## What it does

Anthropic 공식 Big Four 사무 문서 생성 — Docx (Word), Xlsx (Excel multi-sheet), Pptx (PowerPoint), PDF. python-docx / openpyxl / python-pptx / weasyprint 사용. 사용자 요청 분석 후 적절한 형식 자동 선택 또는 명시 형식으로 생성. 차용 출처 Anthropic document-skills

## Boundaries

Different from /design-html (web HTML), /slides (presentation HTML), /make-pdf gstack (markdown to PDF only). This handles native Office formats.

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
