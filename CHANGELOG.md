# Changelog

All notable changes to this plugin are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-06-16

### Added
- **CI quality gate** (`.github/workflows/skills-ci.yml` + vendored stdlib `skill-ci/`): per-skill lint (0 errors) + required `evals/cases.json` + cases dry-run + description score ≥ 0.6; fails the build on regression.
- **Eval coverage**: `evals/cases.json` for every skill (test coverage 0 → 100%) — 23 eval sets added across the 56 skills.
- **Runtime entry commands** under `commands/`: `/find-skill` and `/simonk` (the documented slash entry points, previously an empty dir).
- **CONTRIBUTING.md** tying skill authoring to the quality gate.
- **HTML completion-report standard**: every skill now emits a self-contained HTML report on completion — simple at-a-glance summary + intuitive inline-SVG charts/images, each item behind a `[자세히]` progressive-disclosure button.

### Changed
- Rewrote skill descriptions to lead with "Use when …" and state output (routing quality) — 9 descriptions rewritten.
- **`completion-report` skill upgraded to 0.2.0** — the HTML report engine + `[자세히]` progressive-disclosure template that powers the HTML completion-report standard across all SimonK plugins.

### Fixed
- Migrated stale-schema `evals/cases.json` to the canonical object schema — 20 migrated.

[0.2.0]: https://github.com/Simon-YHKim/SimonKCore/releases/tag/v0.2.0
