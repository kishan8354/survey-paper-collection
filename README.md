# Survey paper collection

I collect papers here on vision-language hallucination, visual grounding and medical VLMs. I also include related work on visual token pruning and generative AI.

The collection currently has **11 papers: 1 from 2025 and 10 from 2026**.

## Browse the papers

- [Full comparison](CATALOG.md): year, datasets, input dimensions, tasks and metrics.
- [By year](BY_YEAR.md), [topic](BY_TOPIC.md), [dimension](BY_DIMENSION.md), [dataset](BY_DATASET.md) and [task](BY_TASK.md).
- [CSV file](papers.csv) and [structured records](papers.json).
- [Paper notes](notes/) and [reading checklist](READING_WORKFLOW.md).

## How I classify papers

- **2D:** the method uses images or individual slices. A CT or MRI source does not automatically mean full 3D volume input.
- **Video:** the method uses a sequence of frames.
- **Mixed:** the paper covers several input types, including 2D, 3D/multiview or video.
- **N/A:** a survey without one original experimental dataset.

Dataset entries describe evaluation data unless stated otherwise. I keep code links and source sections in each paper note. Missing code links mean I have not identified a link in the source record.

## Sources

The records use the local PDFs and links to arXiv, ACL Anthology, publisher pages and author repositories. Version numbers and source sections are included where available. The repository contains paper records and notes; the PDFs remain in my local paper folder.

Reading status and reproduction status are tracked separately. A catalogue entry does not mean I have run the paper's experiments.

## Updating the collection

1. Add or update a record in `papers.json`.
2. Run `python3 scripts/render_catalog.py` to refresh the comparison, CSV and category pages.
3. Add my own reading notes in `notes/`. Existing notes are kept when the catalogue is regenerated.
4. Commit and push the changes.

## To review

- Complete the benchmark list for P11.
- Check training data, splits and compute requirements for the experimental papers.
- Add result-table references as I read each paper in detail.
