"""
논문 PDF 18편을 papers/ 폴더로 내려받는다.

사용법:  이 파일이 있는 폴더에서
             python fetch_papers.py

인터넷만 되면 다른 준비물은 없다 (표준 라이브러리만 사용).
이미 받은 파일은 건너뛰므로 중간에 끊겨도 그냥 다시 실행하면 된다.
"""

import os
import ssl
import sys
import time
import urllib.request

PAPERS = [
    ("dllm_vsr",      "https://arxiv.org/pdf/2605.28456"),
    ("dllm_decoding", "https://arxiv.org/pdf/2605.29613"),
    ("gcagent",       "https://arxiv.org/pdf/2511.12027"),
    ("erv",           "https://arxiv.org/pdf/2510.23506"),
    ("zero_avsr",     "https://arxiv.org/pdf/2503.06273"),
    ("mms_llama",     "https://arxiv.org/pdf/2503.11315"),
    ("personalized",  "https://arxiv.org/pdf/2409.00986"),
    ("vsp_llm",       "https://arxiv.org/pdf/2402.15151"),
    ("emvsr",         "https://arxiv.org/pdf/2401.09802"),
    ("realtalk",      "https://arxiv.org/pdf/2406.07867"),
    ("akvsr",         "https://arxiv.org/pdf/2308.07593"),
    ("vsr_low",       "https://arxiv.org/pdf/2309.08535"),
    ("i2s",           "https://arxiv.org/pdf/2309.08531"),
    ("lmd_vsr",       "https://arxiv.org/pdf/2308.09311"),
    ("mtlam",         "https://arxiv.org/pdf/2305.04542"),
    ("mvm",           "https://ojs.aaai.org/index.php/AAAI/article/view/20003/19762"),
    ("migr",          "https://arxiv.org/pdf/2512.02699"),
    ("inclusive",     "https://arxiv.org/pdf/2508.20476"),
]

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "papers")
UA = "Mozilla/5.0 (compatible; homepage-thumbnail-builder/1.0)"


def fetch(url, dest, tries=3):
    ctx = ssl.create_default_context()
    for attempt in range(1, tries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60, context=ctx) as r:
                data = r.read()
            if not data.startswith(b"%PDF"):
                raise ValueError("PDF가 아님 (%d bytes, 앞부분: %r)" % (len(data), data[:20]))
            with open(dest, "wb") as f:
                f.write(data)
            return len(data)
        except Exception as e:
            if attempt == tries:
                raise
            print("      재시도 %d/%d ... (%s)" % (attempt + 1, tries, e))
            time.sleep(3 * attempt)


def main():
    os.makedirs(OUT, exist_ok=True)
    ok, skipped, failed = 0, 0, []

    for i, (name, url) in enumerate(PAPERS, 1):
        dest = os.path.join(OUT, name + ".pdf")
        label = "[%2d/%d] %-14s" % (i, len(PAPERS), name)

        if os.path.exists(dest) and os.path.getsize(dest) > 10_000:
            print(label + "이미 있음 — 건너뜀")
            skipped += 1
            continue

        print(label + "받는 중 ... ", end="", flush=True)
        try:
            n = fetch(url, dest)
            print("%.1f MB" % (n / 1e6))
            ok += 1
        except Exception as e:
            print("실패: %s" % e)
            failed.append((name, url))
        time.sleep(1)          # arXiv 예의상 간격

    print("\n" + "=" * 56)
    print("받음 %d개 · 건너뜀 %d개 · 실패 %d개" % (ok, skipped, len(failed)))
    print("저장 위치: %s" % OUT)
    if failed:
        print("\n실패한 논문 — 브라우저로 직접 받아 위 폴더에 저장하세요:")
        for name, url in failed:
            print("  %-14s -> %s.pdf   %s" % (name, name, url))
    print("=" * 56)
    print("\n끝나면 Claude 에게 '다 받았다'고 알려주세요.")


if __name__ == "__main__":
    sys.exit(main())
