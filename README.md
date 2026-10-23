# Survey paper collection

A working literature collection for Kishan’s supervisor discussion. Initial scope: medical vision-language hallucination and grounding, with separate efficiency and background tracks. The final survey scope is still to be agreed with the supervisor.

**11 supplied papers indexed: 1 from 2025 and 10 from 2026.** Metadata and experiment descriptions were initially extracted with AI assistance on 23 October 2026. These are starting notes for human review; no experiments have been reproduced.

## Browse

- [Full comparison](CATALOG.md) — year, data, dimensionality, evaluated tasks and metrics.
- [By year](BY_YEAR.md), [topic](BY_TOPIC.md), [dimension](BY_DIMENSION.md), [dataset](BY_DATASET.md) and [task](BY_TASK.md).
- [CSV spreadsheet](papers.csv) and [structured source data](papers.json).
- [Paper notes](notes/) and [reading workflow](READING_WORKFLOW.md).

## Classification rules

- **2D** means image/slice input in the evaluated setup. A CT or MRI source does not automatically mean the method consumes full 3D volumes.
- **Video** is temporal image input; it is not automatically volumetric 3D.
- **Mixed** describes the broad benchmark paper covering 2D, 3D/multiview and video tasks.
- **N/A** applies to surveys with no single original experimental dataset.
- Dataset names refer to evaluation unless a record says otherwise; training-data details need separate review before reproduction.
- Missing code links mean “not identified in the supplied PDF,” not proof that no code exists. Linked code has not been run.

## Sources and local PDFs

Each paper card records the original filename and evidence sections. The source PDFs remain in the parent `Research paper` folder locally. This repository contains metadata, original notes and source links; the PDFs and books are not copied into it. It therefore remains usable after publication without links that depend on the parent directory.

Official arXiv pages, ACL Anthology and the MedAlign author repository were checked on 23 October 2026. ACM/IEEE DOI pages were inaccessible to the browsing tool; those records explicitly rely on the supplied PDFs. arXiv records are pinned to the local PDF version where available. Later versions may differ.

## Update

1. Add or correct a record in `papers.json`, including evidence locations and uncertainties.
2. Run `python3 scripts/render_catalog.py`.
3. Edit the corresponding note in `notes/` with your own understanding; existing note cards are preserved by the generator. If metadata changes, update its note card too.
4. Commit the changed catalogue and notes.

Next extraction gaps: all 55 benchmarks in P11; exact training data, splits and compute for each experimental method; reproduction status and numerical results with exact table rows.
