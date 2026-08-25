# jeonghun0716.github.io

## 배포 (5분)
1. GitHub에서 새 저장소 생성 — 이름은 정확히 `JeongHun0716.github.io` (Public).
2. 이 폴더의 `index.html`, `images/`, `cv.pdf` 를 올린다.
3. Settings → Pages → Source: `Deploy from a branch`, Branch: `main` / `(root)` → Save.
4. 1~2분 뒤 https://jeonghun0716.github.io 에서 확인.

## 넣어야 할 파일
- `cv.pdf` — cv_modern.pdf 를 이 이름으로 복사
- `images/profile.jpg` — 프로필 사진 (정사각형 권장, 400×400 이상)
- 논문 썸네일 — 각 논문 Figure 1을 캡처해서 `images/` 에 아래 이름으로 저장. 권장 비율 150:92 (예: 600×368). 없으면 회색 박스로 표시되므로 하나씩 채워도 됨.

| 파일명 | 논문 |
|---|---|
| dllm_vsr.png | Diffusion LLMs for VSR (EMNLP 2026) |
| dllm_decoding.png | Decoding Strategies for Diffusion-Based ASR (EMNLP 2026) |
| gcagent.png | GCAgent (TMM 2026) |
| erv.png | Emotional Rationale Verifier (AAAI 2026) |
| zero_avsr.png | Zero-AVSR (ICCV 2025) |
| mms_llama.png | MMS-LLaMA (Findings of ACL 2025) |
| personalized.png | Personalized Lip Reading (AAAI 2025) |
| vsp_llm.png | VSP-LLM (Findings of EMNLP 2024) |
| emvsr.png | Efficient Multilingual VSR (ACM MM 2024) |
| realtalk.png | Let's Go Real Talk (ACL 2024) |
| akvsr.png | AKVSR (TMM 2024) |
| vsr_low.png | VSR with Whisper labels (ICASSP 2024) |
| i2s.png | Image-to-Speech Captioning (ICASSP 2024) |
| lmd_vsr.png | Lip Reading for Low-resource Languages (ICCV 2023) |
| mtlam.png | Multi-Temporal Lip-Audio Memory (ICASSP 2023) |
| mvm.png | Multi-head Visual-Audio Memory (AAAI 2022) |
| migr.png | Modality-Importance-Guided Reasoning (arXiv) |
| inclusive.png | Towards Inclusive Communication (arXiv) |

## 수정
- 논문/뉴스 추가: `build.py` 의 `pubs`, `news` 리스트를 편집하고 `python3 build.py` 실행 → `index.html` 재생성.
- `build.py` 없이 `index.html` 을 직접 편집해도 됨.
- 논문 한 줄 요약(`d=` 필드)은 제목 기반으로 임시로 써둔 것이니 본인 표현으로 다듬을 것.

## 기존 Google Sites
새 사이트가 뜨면 Google Sites 첫 화면에 새 주소 링크를 남기거나 사이트를 내리고, Scholar/LinkedIn 프로필의 홈페이지 URL을 새 주소로 바꿀 것.
