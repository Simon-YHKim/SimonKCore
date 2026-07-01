---
name: semantic-recall
description: Use when the user wants meaning-based (not keyword) search over the Obsidian second brain / SimonKWiki vault or the .claude memory — triggers "의미검색", "시맨틱 검색", "벌트 의미로 찾아", "semantic search", "smart lookup", "메모리 의미검색", "뜻으로 찾아줘", "벡터 검색 벌트", or /semantic-recall. Fills the L3 gap (the second-brain "levels" model): our vault relies on grep + wikilinks (L1/L2) but has no embedding search. This skill builds and queries a LOCAL, zero-API-cost vector index (sentence-transformers, all-MiniLM-L6-v2) over markdown, returning meaning-similar chunks. Evergreen summaries stay markdown — vectors are for needle-in-haystack recall only (they miss aggregates/whole-file context). Different from wiki-query (exact/link traversal) and memory MEMORY.md (flat index).
---

# semantic-recall — 로컬 의미검색 (L3)

> Second Brain "levels" 모델의 **L3 결손**을 메운다. 우리는 L1(CLAUDE.md 라우터)·L2(Karpathy 위키·wiki-ingest) 초과 달성했으나, **임베딩 의미검색이 없어** grep+wikilink에 의존했다. 이 스킬은 **로컬·무료** 벡터 인덱스로 뜻 기반 회상을 제공한다. API 비용 0(로컬 모델).

## 원칙 (영상 caveat 반영)
- **벡터는 검색 전용**. 에버그린 요약·집계·전체맥락은 **markdown 유지**(벡터는 "최고매출 주" 같은 집계를 놓침 — 청크만 봄).
- **파생 인덱스**(system-of-record 아님). 원본 불변, 언제든 재생성.
- 검색순서 fallback: **memory → wiki(위키링크) → semantic(이 스킬) → live-source**.

## 사용
```bash
# 1) 최초/갱신: 인덱스 빌드 (벌트 + memory 스캔 → 임베딩 → .semantic-index/)
python semantic_index.py build

# 2) 질의: 뜻으로 top-k 회상
python semantic_index.py query "번아웃 없이 지속가능한 자율 루프" -k 8
```
최초 1회 `pip install sentence-transformers numpy`. 모델(all-MiniLM-L6-v2 ~90MB)은 첫 실행 시 자동 다운로드(로컬 캐시, 이후 오프라인).

## 대상 (기본, `--roots`로 변경)
- `C:\Coding Infra\obsidian\SimonKWiki\wiki` (Karpathy 위키)
- `C:\Users\Soha.Bae\.claude\projects\C--Coding-Infra\memory` (per-fact 메모리)

## 출력
top-k 청크: `점수 · 파일:섹션 · 스니펫`. 에이전트는 이걸 후보로 받아 **원본 md를 열어** 전체맥락 확인(청크 요약 신뢰 금지).

## 언제 안 쓰나
- 정확 단어/파일명 → grep/`wiki-query`. 관계체인 추적 → 위키링크/(향후)그래프. 집계·전체요약 → 원본 md 직독.

## 로드맵
- v0.1(현재): 로컬 임베딩 build/query, npz 저장, 코사인 top-k.
- v0.2: 증분 인덱싱(변경파일만), 하이브리드(키워드+벡터) 재랭킹.
- v0.3: POLE+ 엔티티 추출로 typed-edge 제안(L4 컨텍스트그래프, Neo4j 영상) — 규칙기반 우선(LLM 비용 회피).
- 정본 스펙: `reports/external-knowledge-integration-spec-20260702.md` SPEC-2.
