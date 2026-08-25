import html
import re
ME = "Jeong Hun Yeo"

# NOTE: the d="..." one-line summaries are no longer rendered.
#       They are kept here in case the descriptions are wanted back later.
pubs = [
 dict(t="Diffusion Large Language Models for Visual Speech Recognition",
      a=[("Jeong Hun Yeo",""),("Chae Won Kim",""),("Hyeongseop Rha",""),("Yong Man Ro","")],
      v="EMNLP 2026", img="dllm_vsr.png",
      links=[("paper","https://arxiv.org/abs/2605.28456"),("code","https://github.com/JeongHun0716/dllm-vsr")],
      d="Parallel decoding with a diffusion language model for fast visual speech recognition."),
 dict(t="Decoding Strategies for Diffusion-Based ASR: A Systematic Evaluation of Confidence-Based Thresholding",
      a=[("Jeong Hun Yeo",""),("Minsu Kim",""),("Hyeongseop Rha",""),("Yong Man Ro","")],
      v="EMNLP 2026", img="dllm_decoding.png",
      links=[("paper","https://arxiv.org/abs/2605.29613")],
      d="How confidence thresholds trade off speed and accuracy in diffusion-based speech recognition."),
 dict(t="GCAgent: Long-Video Understanding via Schematic and Narrative Episodic Memory",
      a=[("Jeong Hun Yeo","*"),("Sangyun Chung","*"),("Sungjune Park",""),("Dae Hoe Kim",""),("Jinyoung Moon",""),("Yong Man Ro","")],
      v="IEEE TMM 2026", img="gcagent.png",
      links=[("paper","https://arxiv.org/abs/2511.12027")],
      d="An agent that builds episodic memory to reason over long videos."),
 dict(t="Emotion-Coherent Reasoning for Multimodal LLMs via Emotional Rationale Verifier",
      a=[("Hyeongseop Rha",""),("Jeong Hun Yeo",""),("Yeonju Kim",""),("Yong Man Ro","")],
      v="AAAI 2026", img="erv.png",
      links=[("paper","https://arxiv.org/abs/2510.23506"),("code","https://github.com/Rhatanii/ERV")],
      d="Keeping a multimodal LLM's reasoning consistent with the emotion it predicts."),
 dict(t="Zero-AVSR: Zero-Shot Audio-Visual Speech Recognition with LLMs by Learning Language-Agnostic Speech Representations",
      a=[("Jeong Hun Yeo","*"),("Minsu Kim","*"),("Chae Won Kim",""),("Stavros Petridis",""),("Yong Man Ro","")],
      v="ICCV 2025", img="zero_avsr.png",
      links=[("paper","https://arxiv.org/abs/2503.06273"),("code","https://github.com/JeongHun0716/zero-avsr")],
      d="Language-agnostic speech representations let an LLM transcribe unseen languages from audio and lips."),
 dict(t="MMS-LLaMA: Efficient LLM-based Audio-Visual Speech Recognition with Minimal Multimodal Speech Tokens",
      a=[("Jeong Hun Yeo","*"),("Hyeongseop Rha","*"),("Se Jin Park",""),("Yong Man Ro","")],
      v="Findings of ACL 2025", img="mms_llama.png",
      links=[("paper","https://arxiv.org/abs/2503.11315"),("code","https://github.com/JeongHun0716/MMS-LLaMA")],
      d="Compressing audio-visual speech into a handful of tokens for efficient LLM-based recognition."),
 dict(t="Personalized Lip Reading: Adapting to Your Unique Lip Movements with Vision and Language",
      a=[("Jeong Hun Yeo",""),("Chae Won Kim",""),("Hyunjun Kim",""),("Hyeongseop Rha",""),("Seunghee Han",""),("Wen-Huang Cheng",""),("Yong Man Ro","")],
      v="AAAI 2025", img="personalized.png",
      links=[("paper","https://arxiv.org/abs/2409.00986"),("code","https://github.com/JeongHun0716/Personalized-Lip-Reading")],
      d="Adapting a lip reading model to an individual speaker with vision and language cues."),
 dict(t="Where Visual Speech Meets Language: VSP-LLM Framework for Efficient and Context-Aware Visual Speech Processing",
      a=[("Jeong Hun Yeo","*"),("Seunghee Han","*"),("Minsu Kim",""),("Yong Man Ro","")],
      v="Findings of EMNLP 2024", img="vsp_llm.png",
      links=[("paper","https://arxiv.org/abs/2402.15151"),("code","https://github.com/sally-sh/vsp-llm")],
      d="Context-aware visual speech recognition and translation with an LLM backbone."),
 dict(t="Efficient Training for Multilingual Visual Speech Recognition: Pre-training with Discretized Visual Speech Representation",
      a=[("Minsu Kim","*"),("Jeong Hun Yeo","*"),("Se Jin Park",""),("Hyeongseop Rha",""),("Yong Man Ro","")],
      v="ACM MM 2024", img="emvsr.png",
      links=[("paper","https://arxiv.org/abs/2401.09802"),("code","https://github.com/JeongHun0716/e-mvsr")],
      d="Discrete visual speech units make multilingual lip reading cheap to pre-train."),
 dict(t="Let's Go Real Talk: Spoken Dialogue Model for Face-to-Face Conversation",
      a=[("Se Jin Park","*"),("Chae Won Kim","*"),("Hyeongseop Rha",""),("Minsu Kim",""),("Joanna Hong",""),("Jeong Hun Yeo",""),("Yong Man Ro","")],
      v="ACL 2024 (Oral)", img="realtalk.png",
      links=[("paper","https://arxiv.org/abs/2406.07867"),("data","https://huggingface.co/datasets/IVLLab/MultiDialog"),("demo","https://multidialog.github.io/")],
      d="A spoken dialogue model and dataset for face-to-face conversation."),
 dict(t="AKVSR: Audio Knowledge Empowered Visual Speech Recognition by Compressing Audio Knowledge of a Pretrained Model",
      a=[("Jeong Hun Yeo",""),("Minsu Kim",""),("Jeongsoo Choi",""),("Dae Hoe Kim",""),("Yong Man Ro","")],
      v="IEEE TMM 2024", img="akvsr.png",
      links=[("paper","https://arxiv.org/abs/2308.07593")],
      d="Distilling audio knowledge from a pretrained model into a lip reading network."),
 dict(t="Visual Speech Recognition for Languages with Limited Labeled Data using Automatic Labels from Whisper",
      a=[("Jeong Hun Yeo","*"),("Minsu Kim","*"),("Shinji Watanabe",""),("Yong Man Ro","")],
      v="ICASSP 2024 (Oral)", img="vsr_low.png",
      links=[("paper","https://arxiv.org/abs/2309.08535"),("code","https://github.com/JeongHun0716/vsr-low")],
      d="Whisper-generated labels unlock lip reading for low-resource languages."),
 dict(t="Towards Practical and Efficient Image-to-Speech Captioning with Vision-Language Pre-training and Multi-modal Tokens",
      a=[("Minsu Kim",""),("Jeongsoo Choi",""),("Soumi Maiti",""),("Jeong Hun Yeo",""),("Shinji Watanabe",""),("Yong Man Ro","")],
      v="ICASSP 2024", img="i2s.png",
      links=[("paper","https://arxiv.org/abs/2309.08531"),("code","https://github.com/ms-dot-k/Image-to-Speech")],
      d="Generating spoken captions directly from images with multimodal tokens."),
 dict(t="Lip Reading for Low-resource Languages by Learning and Combining General Speech Knowledge and Language-specific Knowledge",
      a=[("Minsu Kim","*"),("Jeong Hun Yeo","*"),("Jeongsoo Choi",""),("Yong Man Ro","")],
      v="ICCV 2023", img="lmd_vsr.png",
      links=[("paper","https://arxiv.org/abs/2308.09311"),("code","https://github.com/JeongHun0716/lmd-vsr")],
      d="Separating general speech knowledge from language-specific knowledge for low-resource lip reading."),
 dict(t="Multi-Temporal Lip-Audio Memory for Visual Speech Recognition",
      a=[("Jeong Hun Yeo",""),("Minsu Kim",""),("Yong Man Ro","")],
      v="ICASSP 2023", img="mtlam.png",
      links=[("paper","https://arxiv.org/abs/2305.04542")],
      d="A memory that recalls audio at multiple temporal scales from lip movements."),
 dict(t="Distinguishing Homophenes Using Multi-head Visual-Audio Memory for Lip Reading",
      a=[("Minsu Kim",""),("Jeong Hun Yeo",""),("Yong Man Ro","")],
      v="AAAI 2022", img="mvm.png",
      links=[("paper","https://ojs.aaai.org/index.php/AAAI/article/view/20003/19762"),("code","https://github.com/ms-dot-k/Multi-head-Visual-Audio-Memory")],
      d="Resolving visually identical words with a multi-head audio memory."),
]

preprints = [
 dict(t="Learning What to Attend First: Modality-Importance-Guided Reasoning for Reliable Multimodal Emotion Understanding",
      a=[("Hyeongseop Rha","*"),("Jeong Hun Yeo","*"),("Se Jin Park",""),("Yong Man Ro","")],
      v="arXiv 2025", img="migr.png",
      links=[("paper","https://arxiv.org/abs/2512.02699")],
      d="Teaching a multimodal LLM which modality to trust first when reading emotion."),
 dict(t="Towards Inclusive Communication: A Unified Framework for Generating Spoken Language from Sign, Lip, and Audio",
      a=[("Jeong Hun Yeo",""),("Hyeongseop Rha",""),("Sungjune Park",""),("Junil Won",""),("Yong Man Ro","")],
      v="arXiv 2025", img="inclusive.png",
      links=[("paper","https://arxiv.org/abs/2508.20476")],
      d="One model that turns sign language, lip movements, or audio into spoken language."),
]

news = [
 ("Aug 2026","Two papers accepted to <b>EMNLP 2026</b>."),
 ("Mar 2026","Started as a postdoctoral researcher at KAIST, supported by the <b>Jang Young Sil Fellowship</b>."),
 ("Feb 2026","Received my Ph.D. in Electrical Engineering from KAIST."),
 ("Jan 2026","GCAgent accepted to <b>IEEE TMM</b>; ERV accepted to <b>AAAI 2026</b>."),
 ("Jun 2025","Zero-AVSR accepted to <b>ICCV 2025</b>. Gave an invited talk at ETRI."),
]

def authors(a):
    out=[]
    for n,s in a:
        n2 = f"<b>{n}</b>" if n==ME else n
        out.append(n2+s)
    return ", ".join(out)

def entry(p):
    links = " / ".join(f'<a href="{u}">{l}</a>' for l,u in p["links"])
    return f"""
      <div class="pub">
        <div class="thumb"><img src="images/{p['img']}" alt="" loading="lazy" onerror="this.parentNode.classList.add('missing')"></div>
        <div class="meta">
          <p class="title">{html.escape(p['t'])}</p>
          <p class="authors">{authors(p['a'])}</p>
          <p class="venue">{p['v']} &nbsp;·&nbsp; {links}</p>
        </div>
      </div>"""

def year_of(v):
    m = re.search(r"\b(20\d{2})\b", v)
    return m.group(1) if m else ""

def render(items, year_marks=False):
    out, cur = [], None
    for p in items:
        if year_marks:
            y = year_of(p["v"])
            if y != cur:
                cur = y
                out.append(f'\n  <p class="year">{y}</p>')
        out.append(entry(p))
    return "".join(out)


SANS = '-apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, Roboto, sans-serif'

page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Jeong Hun Yeo</title>
<meta name="description" content="Jeong Hun Yeo — postdoctoral researcher at KAIST working on audio-visual speech recognition and multimodal LLMs.">
<link rel="icon" href="data:,">
<style>
  :root {{
    --ink: #1a1a1a;
    --muted: #6b6b6b;
    --line: #e4e4e0;
    --accent: #1f3a5f;
    --bg: #ffffff;
    --thumb-bg: #f3f3f0;
  }}
  * {{ box-sizing: border-box; }}
  html {{ -webkit-text-size-adjust: 100%; }}
  body {{
    margin: 0; background: var(--bg); color: var(--ink);
    font-family: Charter, "Bitstream Charter", "Iowan Old Style", Georgia, serif;
    font-size: 16px; line-height: 1.6;
  }}
  a {{ color: var(--accent); text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  a:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px; }}
  .wrap {{ max-width: 820px; margin: 0 auto; padding: 56px 24px 80px; }}

  header {{ display: flex; gap: 40px; align-items: flex-start; }}
  header .text {{ flex: 1; min-width: 0; }}
  header .photo {{ flex: 0 0 180px; }}
  header .photo img {{ width: 180px; height: 180px; border-radius: 50%; object-fit: cover; background: var(--thumb-bg); display: block; }}
  h1 {{ font-size: 34px; font-weight: 600; letter-spacing: -0.01em; margin: 0 0 4px; }}
  .role {{ color: var(--muted); margin: 0 0 18px; font-size: 15px; }}
  header p {{ margin: 0 0 12px; }}
  .links {{ font-size: 15px; margin-top: 4px; }}
  .links a {{ margin-right: 4px; }}
  .links span {{ color: var(--line); margin: 0 8px; }}

  h2 {{
    font-size: 15px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase;
    color: var(--accent); margin: 56px 0 14px; padding-bottom: 8px; border-bottom: 1px solid var(--line);
  }}
  .note {{ color: var(--muted); font-size: 14px; margin: -4px 0 18px; }}

  .news {{ display: grid; grid-template-columns: 84px 1fr; gap: 6px 16px; margin: 0; }}
  .news dt {{ color: var(--muted); font-size: 14px; padding-top: 2px; }}
  .news dd {{ margin: 0; }}

  .pub {{ display: grid; grid-template-columns: 210px 1fr; gap: 26px; padding: 18px 0; align-items: center; }}
  .thumb {{ width: 210px; height: 129px; border: 1px solid var(--line); border-radius: 8px;
            overflow: hidden; background: var(--bg);
            transition: box-shadow .18s ease, transform .18s ease; }}
  .pub:hover .thumb {{ box-shadow: 0 6px 18px rgba(0,0,0,.10); transform: translateY(-2px); }}
  .thumb img {{ width: 100%; height: 100%; object-fit: cover; display: block; }}
  .thumb.missing img {{ display: none; }}
  .meta p {{ margin: 0; }}
  .title {{ font-weight: 600; font-size: 17px; line-height: 1.4; }}
  .authors {{ font-size: 15px; margin-top: 3px !important; }}
  .venue {{ font-family: {SANS}; font-size: 13px; letter-spacing: .01em;
            color: var(--muted); margin-top: 4px !important; }}

  .year {{ font-family: {SANS}; font-size: 12px; font-weight: 600; letter-spacing: 0.14em;
           color: #9a9a96; font-variant-numeric: tabular-nums; margin: 30px 0 2px; }}
  .note + .year {{ margin-top: 8px; }}

  .list {{ margin: 0; padding-left: 0; list-style: none; }}
  .list li {{ display: flex; justify-content: space-between; gap: 16px; padding: 4px 0; }}
  .list .when {{ color: var(--muted); font-size: 14px; white-space: nowrap; }}
  .group {{ margin: 0 0 18px; }}
  .group b {{ display: block; margin-bottom: 4px; }}

  footer {{ margin-top: 64px; color: var(--muted); font-size: 13px; }}

  @media (max-width: 640px) {{
    .wrap {{ padding: 32px 18px 60px; }}
    header {{ flex-direction: column-reverse; gap: 20px; }}
    header .photo img {{ width: 120px; height: 120px; }}
    .pub {{ grid-template-columns: 1fr; gap: 12px; }}
    .thumb {{ width: 100%; height: auto; aspect-ratio: 600 / 368; }}
    .news {{ grid-template-columns: 1fr; gap: 2px; }}
    .news dt {{ margin-top: 8px; }}
  }}
</style>
</head>
<body>
<div class="wrap">

  <header>
    <div class="text">
      <h1>Jeong Hun Yeo</h1>
      <p class="role">Postdoctoral Researcher · School of Electrical Engineering, KAIST</p>
      <p>I am a postdoctoral researcher in the <a href="https://www.ivllab.kaist.ac.kr/">Integrated Vision &amp; Language Lab</a> at KAIST, supported by the Jang Young Sil Fellowship. I received my Ph.D. in Electrical Engineering from KAIST in 2026, advised by <a href="https://www.ivllab.kaist.ac.kr/people/professor">Prof. Yong Man Ro</a>.</p>
      <p>My research focuses on visual and audio-visual speech recognition with large language models — disambiguating what lips alone cannot tell, scaling to languages with little or no labeled data, and making inference fast enough for real-time use. Recently I am working on diffusion language models for low-latency speech interaction and multimodal agents for long-video understanding.</p>
      <p class="links">
        <a href="mailto:jh.y@ieee.org">Email</a><span>/</span>
        <a href="cv.pdf">CV</a><span>/</span>
        <a href="https://scholar.google.com/citations?user=PJoYv2cAAAAJ">Google Scholar</a><span>/</span>
        <a href="https://github.com/JeongHun0716">GitHub</a><span>/</span>
        <a href="https://www.linkedin.com/in/jeong-hun-yeo-295024280/">LinkedIn</a>
      </p>
    </div>
    <div class="photo"><img src="images/profile.jpg" alt="Jeong Hun Yeo"></div>
  </header>

  <h2>News</h2>
  <dl class="news">
    {"".join(f"<dt>{d}</dt><dd>{t}</dd>" for d,t in news)}
  </dl>

  <h2>Publications</h2>
  <p class="note">* equal contribution. Also on <a href="https://scholar.google.com/citations?user=PJoYv2cAAAAJ">Google Scholar</a>.</p>
  {render(pubs, year_marks=True)}

  <h2>Preprints</h2>
  {render(preprints)}

  <h2>Awards</h2>
  <ul class="list">
    <li><span>Jang Young Sil Postdoctoral Fellowship, KAIST</span><span class="when">2026</span></li>
    <li><span>KAIST Outstanding Paper Award for Graduate Students</span><span class="when">2024</span></li>
  </ul>

  <h2>Service</h2>
  <p class="group"><b>Journal reviewer</b> IEEE TPAMI, IJCV, IEEE TIP, IEEE TMM, IEEE/ACM TASLP</p>
  <p class="group"><b>Conference reviewer</b> CVPR 2026, ICCV 2025, ECCV 2026, NeurIPS 2026, AAAI 2026, ARR 2025–2026, ICASSP 2025–2026, ICIP 2024–2025</p>
  <p class="group"><b>Invited talk</b> ETRI, “Efficient LLM-Based Audio-Visual Speech Recognition”, June 2025</p>
  <p class="group"><b>Teaching</b> Teaching assistant, Multimedia Processing and Learning, KAIST, Fall 2023</p>

  <footer>Layout in the spirit of <a href="https://jonbarron.info/">Jon Barron's</a> website.</footer>
</div>
</body>
</html>
"""
open("index.html","w").write(page)
print("ok", len(page))
