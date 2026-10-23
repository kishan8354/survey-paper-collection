# Papers by topic

## Background survey

| ID | Year | Paper | Data / benchmarks | Input dimension | Evaluated tasks | Metrics |
|---|---|---|---|---|---|---|
| P09 | 2026 | [Understanding Hallucinations in Large Visual and Language Models](https://doi.org/10.1145/3811409) | N/A — reviews datasets and studies rather than introducing one experimental dataset | N/A — survey across modalities | Hallucination taxonomy and root-cause survey | N/A — survey; discusses evaluation limitations |
| P10 | 2026 | [LLM Post-Training: A Deep Dive Into Reasoning Large Language Models](https://doi.org/10.1109/TPAMI.2026.3720414) | N/A — survey of post-training literature; benchmarks catalogued in Section V | N/A — primarily text; multimodal coverage | Supervised fine-tuning survey; Preference optimization and RL survey; Test-time scaling survey | N/A — literature comparisons, not one unified experimental score |

## Broad vision benchmarking

| ID | Year | Paper | Data / benchmarks | Input dimension | Evaluated tasks | Metrics |
|---|---|---|---|---|---|---|
| P11 | 2026 | [Hard Vision, Easy Vision: What GPT-6 Astra Reveals Across Computer Vision](https://arxiv.org/abs/2609.35718v1) | 55 benchmarks across 34 capabilities; full benchmark-by-task inventory still to extract | Mixed — 2D, 3D/multiview, video | Recognition and visual reading; Spatial and visual reasoning; 2D grounding and segmentation; 3D perception and geometry; Video understanding; Generation and restoration; Robotics and expert-domain vision | Task-specific benchmark metrics; not comparable as one shared score |

## General VLM hallucination evaluation

| ID | Year | Paper | Data / benchmarks | Input dimension | Evaluated tasks | Metrics |
|---|---|---|---|---|---|---|
| P05 | 2026 | [Robustness of Internal Signals for Hallucination Detection in Vision-Language Models](https://arxiv.org/abs/2610.27041v1) | MSCOCO 2014; Objects365 (generalization) | 2D | Object hallucination detection in image captions; Robustness and modality sensitivity; Detector ensembling | AUROC; AUPRC; CHAIR-derived hallucination labels |

## Medical VLM alignment

| ID | Year | Paper | Data / benchmarks | Input dimension | Evaluated tasks | Metrics |
|---|---|---|---|---|---|---|
| P01 | 2026 | [Enhancing Medical Large Vision-Language Models via Alignment Distillation](https://github.com/Aofei-Chang/MedAlign) | MIMIC-CXR; IU-Xray; SLAKE; VQA-RAD; PathVQA; OmniMedVQA | 2D | Medical report generation; Medical VQA | BLEU; ROUGE-L; METEOR; BERTScore; CheXbert; RadGraph; RaTEScore; Closed-ended accuracy; Open-ended recall |
| P02 | 2026 | [Beyond Surface Features: Advancing Medical Vision-Language Alignment via Dynamic Evidence-Guided Preference Optimization](https://aclanthology.org/2026.acl-long.1200/) | SLAKE (English subset); VQA-RAD; MIMIC-CXR; IU-Xray | 2D | Medical VQA; Medical report generation | Open/closed accuracy; BLEU; ROUGE-L; METEOR |

## Medical hallucination detection and correction

| ID | Year | Paper | Data / benchmarks | Input dimension | Evaluated tasks | Metrics |
|---|---|---|---|---|---|---|
| P03 | 2026 | [Hallucination Detection and Correction in Medical VLMs via Counter-Evidence Verification](https://arxiv.org/abs/2606.18609v1) | VQA-RAD; MIMIC-VQA; MIMIC-CXR; IU-Xray | 2D | Medical VQA; Medical report generation; Hallucination detection; Hallucination correction | PR-AUC; ROC-AUC; Mi-F1-5; Mi-F1-14; CHAIR-I/S; MediHall; VQA accuracy |

## Medical hallucination mitigation

| ID | Year | Paper | Data / benchmarks | Input dimension | Evaluated tasks | Metrics |
|---|---|---|---|---|---|---|
| P04 | 2026 | [Counterfactual Anatomy-guided Spatial-Temporal Decoding for Annotation-Free Hallucination Mitigation in Medical VLMs](https://arxiv.org/abs/2608.17427v1) | SLAKE; MIMIC-CXR (VQA formulation) | 2D | Medical VQA; Decoding-time hallucination mitigation | Closed-ended accuracy; Open-ended recall; Weighted overall performance |

## Medical interpretability

| ID | Year | Paper | Data / benchmarks | Input dimension | Evaluated tasks | Metrics |
|---|---|---|---|---|---|---|
| P06 | 2026 | [Beyond Explanation: Debugging Medical Imaging Models via Concept Intervention](https://arxiv.org/abs/2610.09031v1) | Mayo Clinic ovarian ultrasound dataset; CheXpert 5×200 | 2D | Image classification; Concept-based explanation; Model debugging and intervention | Accuracy; Precision; Recall; F1 / Macro F1; AUROC |

## Visual token pruning

| ID | Year | Paper | Data / benchmarks | Input dimension | Evaluated tasks | Metrics |
|---|---|---|---|---|---|---|
| P08 | 2026 | [An AI4AI Framework for Visual Token Pruning](https://arxiv.org/abs/2608.07193v2) | VQAv2; GQA; VizWiz; ScienceQA-IMG; HallBench; POPE; MME; MMBench-EN; MMBench-CN; MM-Vet; TextVQA; ChartQA; AI2D; OCRBench | 2D | Image VQA; Reasoning; Hallucination evaluation; OCR and chart understanding; Efficient inference | Official benchmark scores; Aggregate accuracy; Relative performance; FLOPs; Prefill latency |
| P07 | 2025 | [TransPrune: Token Transition Pruning for Efficient Large Vision-Language Model](https://arxiv.org/abs/2507.20630v2) | MME; MMBench; SEED; ScienceQA; VQA-v2; POPE; GQA; TextVQA; TGIF; MSVD | 2D images + video frames | Multimodal perception and reasoning; Image VQA; Video VQA; Efficient inference | Benchmark-specific scores; Relative performance; TFLOPs; Token budget |
