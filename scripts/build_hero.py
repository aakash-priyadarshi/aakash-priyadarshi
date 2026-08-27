"""Generate GitHub-safe animated hero assets from assets/profile.png."""

from __future__ import annotations

import base64
import io
from pathlib import Path

from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
SRC = ASSETS / "profile.png"


def prepare_portrait() -> tuple[str, int, int]:
    im = Image.open(SRC).convert("RGB")
    width = 1400 if im.width >= im.height else 720
    height = max(1, int(width * im.height / im.width))
    resized = im.resize((width, height), Image.Resampling.LANCZOS)
    resized = resized.filter(ImageFilter.UnsharpMask(radius=0.55, percent=70, threshold=2))
    buf = io.BytesIO()
    resized.save(buf, format="JPEG", quality=82, optimize=True, progressive=True)
    return base64.b64encode(buf.getvalue()).decode("ascii"), width, height


def hero_svg(b64: str, w: int, h: int) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-labelledby="title desc">
  <title id="title">Aakash Priyadarshi coding at his Alienware workstation</title>
  <desc id="desc">Portrait of Aakash, a full-stack and AI / RL engineer, at a late-night workstation. Teal Alienware lighting, a live monitor, and a focused desk setup. Motif: BUILD, VERIFY, SHIP.</desc>
  <defs>
    <style>
      .teal {{ opacity: 0.16; animation: teal 10s ease-in-out infinite; }}
      .purple {{ opacity: 0.12; animation: purple 10s ease-in-out infinite; }}
      .aw {{ opacity: 0.22; animation: aw 10s ease-in-out infinite; }}

      @keyframes teal {{
        0%, 100% {{ opacity: 0.10; }}
        50% {{ opacity: 0.26; }}
      }}
      @keyframes purple {{
        0%, 100% {{ opacity: 0.08; }}
        50% {{ opacity: 0.22; }}
      }}
      @keyframes aw {{
        0%, 100% {{ opacity: 0.16; }}
        50% {{ opacity: 0.38; }}
      }}

      @media (prefers-reduced-motion: reduce) {{
        * {{ animation: none !important; }}
        .teal, .purple, .aw {{ opacity: 0.22; }}
      }}
    </style>
    <linearGradient id="border" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#00D4AA"/>
      <stop offset="50%" stop-color="#7C3AED"/>
      <stop offset="100%" stop-color="#00D4AA"/>
    </linearGradient>
    <clipPath id="shot">
      <rect x="8" y="8" width="{w - 16}" height="{h - 16}" rx="20"/>
    </clipPath>
    <filter id="blur8" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="8"/>
    </filter>
    <filter id="blur16" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="16"/>
    </filter>
  </defs>

  <rect width="{w}" height="{h}" rx="24" fill="#1A1A2E"/>
  <rect x="2" y="2" width="{w - 4}" height="{h - 4}" rx="22" fill="none" stroke="url(#border)" stroke-width="2" opacity="0.85"/>

  <g clip-path="url(#shot)">
    <image href="data:image/jpeg;base64,{b64}" x="8" y="8" width="{w - 16}" height="{h - 16}" preserveAspectRatio="xMidYMid slice"/>

    <!-- Lighting only — no floating particles, scanlines, or steam over the scene. -->
    <ellipse class="aw" cx="{w * 0.48:.1f}" cy="{h * 0.68:.1f}" rx="{w * 0.06:.1f}" ry="{h * 0.07:.1f}" fill="#00D4AA" filter="url(#blur8)"/>
    <ellipse class="teal" cx="{w * 0.48:.1f}" cy="{h * 0.84:.1f}" rx="{w * 0.14:.1f}" ry="{h * 0.12:.1f}" fill="#00D4AA" filter="url(#blur16)"/>
    <ellipse class="purple" cx="{w * 0.78:.1f}" cy="{h * 0.40:.1f}" rx="{w * 0.10:.1f}" ry="{h * 0.22:.1f}" fill="#7C3AED" filter="url(#blur16)"/>
  </g>
</svg>
'''


def terminal_svg() -> str:
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 228" width="520" height="228" role="img" aria-labelledby="tt td">
  <title id="tt">Live engineering loop</title>
  <desc id="td">Terminal sequence: whoami, focus, build, verify, ship. Agent to verifier graph. Signature line: AI has to be correct, not just confident.</desc>
  <defs>
    <style>
      .t0 { animation: t0 10s linear infinite; }
      .t1 { animation: t1 10s linear infinite; }
      .t2 { animation: t2 10s linear infinite; }
      .t3 { animation: t3 10s linear infinite; }
      .t4 { animation: t4 10s linear infinite; }
      .cursor { animation: blink 1.05s steps(1, end) infinite; }
      .n1 { animation: node 10s ease-in-out infinite; }
      .n2 { animation: node 10s ease-in-out infinite 0.7s; }
      .n3 { animation: node 10s ease-in-out infinite 1.4s; }
      .ok { animation: ok 10s ease-in-out infinite; }
      .edge { animation: edge 10s ease-in-out infinite; }

      @keyframes t0 { 0%,16% { opacity:1 } 18%,100% { opacity:0 } }
      @keyframes t1 { 0%,16% { opacity:0 } 18%,38% { opacity:1 } 40%,100% { opacity:0 } }
      @keyframes t2 { 0%,38% { opacity:0 } 40%,56% { opacity:1 } 58%,100% { opacity:0 } }
      @keyframes t3 { 0%,56% { opacity:0 } 58%,78% { opacity:1 } 80%,100% { opacity:0 } }
      @keyframes t4 { 0%,80% { opacity:0 } 83%,96% { opacity:1 } 100% { opacity:0 } }
      @keyframes blink { 0%,49% { opacity:1 } 50%,100% { opacity:0 } }
      @keyframes node { 0%,48% { opacity:0.28 } 58%,84% { opacity:1 } 94%,100% { opacity:0.28 } }
      @keyframes ok { 0%,70% { opacity:0 } 76%,90% { opacity:1 } 100% { opacity:0 } }
      @keyframes edge { 0%,50% { stroke-dashoffset: 40; opacity:0.25 } 62%,84% { stroke-dashoffset:0; opacity:0.9 } 100% { stroke-dashoffset:40; opacity:0.25 } }

      @media (prefers-reduced-motion: reduce) {
        * { animation: none !important; }
        .t0 { opacity: 1; }
        .t1, .t2, .t3, .t4 { opacity: 0; }
        .n1, .n2, .n3 { opacity: 0.85; }
      }
    </style>
  </defs>

  <rect width="520" height="228" rx="16" fill="#1A1A2E"/>
  <rect x="1" y="1" width="518" height="226" rx="15" fill="none" stroke="#00D4AA" stroke-opacity="0.35"/>

  <!-- Terminal -->
  <rect x="14" y="14" width="318" height="200" rx="10" fill="#0E1020"/>
  <circle cx="32" cy="32" r="4" fill="#7C3AED"/>
  <circle cx="46" cy="32" r="4" fill="#00D4AA"/>
  <circle cx="60" cy="32" r="4" fill="#FFFFFF" opacity="0.28"/>
  <text x="78" y="36" fill="#FFFFFF" opacity="0.4" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="11">aakash — verify</text>

  <g font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="14" fill="#E6EDF3">
    <g class="t0">
      <text x="28" y="70"><tspan fill="#00D4AA">$</tspan> whoami</text>
      <text x="28" y="96">Aakash Priyadarshi</text>
      <rect class="cursor" x="28" y="108" width="8" height="15" fill="#00D4AA"/>
    </g>
    <g class="t1">
      <text x="28" y="70"><tspan fill="#00D4AA">$</tspan> focus</text>
      <text x="28" y="96">AI · RL · Full Stack</text>
      <rect class="cursor" x="28" y="108" width="8" height="15" fill="#00D4AA"/>
    </g>
    <g class="t2">
      <text x="28" y="70"><tspan fill="#00D4AA">$</tspan> build</text>
      <text x="28" y="96"><tspan fill="#00D4AA">✓</tspan> compiled</text>
      <rect class="cursor" x="28" y="108" width="8" height="15" fill="#00D4AA"/>
    </g>
    <g class="t3">
      <text x="28" y="70"><tspan fill="#00D4AA">$</tspan> verify</text>
      <text x="28" y="92"><tspan fill="#00D4AA">✓</tspan> checks passed</text>
      <text x="28" y="118"><tspan fill="#7C3AED">$</tspan> ship</text>
      <text x="28" y="142"><tspan fill="#00D4AA">✓</tspan> deployed</text>
      <rect class="cursor" x="28" y="154" width="8" height="15" fill="#00D4AA"/>
    </g>
    <g class="t4">
      <text x="28" y="88" fill="#C4B5FD"># AI has to be correct,</text>
      <text x="28" y="114" fill="#00D4AA"># not just confident.</text>
      <rect class="cursor" x="28" y="128" width="8" height="15" fill="#00D4AA"/>
    </g>
  </g>

  <!-- Agent graph + pipeline -->
  <g font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" transform="translate(348, 14)">
    <text x="0" y="18" fill="#00D4AA" font-size="10" letter-spacing="1.4">AGENT LOOP</text>
    <line class="edge" x1="12" y1="40" x2="12" y2="64" stroke="#00D4AA" stroke-width="1.5" stroke-dasharray="40"/>
    <line class="edge" x1="12" y1="80" x2="12" y2="104" stroke="#7C3AED" stroke-width="1.5" stroke-dasharray="40"/>
    <circle class="n1" cx="12" cy="36" r="6" fill="#00D4AA"/>
    <circle class="n2" cx="12" cy="72" r="6" fill="#7C3AED"/>
    <circle class="n3" cx="12" cy="108" r="6" fill="#00D4AA"/>
    <text x="26" y="40" fill="#FFFFFF" font-size="12">Agent</text>
    <text x="26" y="76" fill="#FFFFFF" font-size="12">Tool</text>
    <text x="26" y="112" fill="#FFFFFF" font-size="12">Verifier</text>
    <text class="ok" x="118" y="116" fill="#00D4AA" font-size="14" font-weight="700">✓</text>

    <text x="0" y="148" fill="#FFFFFF" opacity="0.45" font-size="10" letter-spacing="1.2">PIPELINE</text>
    <text x="0" y="172" fill="#00D4AA" font-size="12" font-weight="700">BUILD</text>
    <text x="58" y="172" fill="#C4B5FD" font-size="12" font-weight="700">VERIFY</text>
    <text x="122" y="172" fill="#00D4AA" font-size="12" font-weight="700">SHIP</text>
    <rect x="0" y="182" width="42" height="4" rx="2" fill="#0E1020"/>
    <rect x="58" y="182" width="42" height="4" rx="2" fill="#0E1020"/>
    <rect x="122" y="182" width="42" height="4" rx="2" fill="#0E1020"/>
    <rect x="0" y="182" height="4" rx="2" fill="#00D4AA">
      <animate attributeName="width" values="6;42;42;6" keyTimes="0;0.58;0.88;1" dur="10s" repeatCount="indefinite"/>
    </rect>
    <rect x="58" y="182" height="4" rx="2" fill="#7C3AED">
      <animate attributeName="width" values="6;42;42;6" keyTimes="0;0.58;0.88;1" dur="10s" begin="1.6s" repeatCount="indefinite"/>
    </rect>
    <rect x="122" y="182" height="4" rx="2" fill="#00D4AA">
      <animate attributeName="width" values="6;42;42;6" keyTimes="0;0.58;0.88;1" dur="10s" begin="3.2s" repeatCount="indefinite"/>
    </rect>
  </g>
</svg>
'''


def main() -> None:
    b64, w, h = prepare_portrait()
    hero = ASSETS / "hero.svg"
    terminal = ASSETS / "hero-terminal.svg"
    hero.write_text(hero_svg(b64, w, h), encoding="utf-8")
    if not terminal.exists():
        terminal.write_text(terminal_svg(), encoding="utf-8")
    print(f"hero.svg        {hero.stat().st_size / 1024:6.1f} KB  {w}x{h}")
    print(f"hero-terminal.svg {terminal.stat().st_size / 1024:6.1f} KB")


if __name__ == "__main__":
    main()
