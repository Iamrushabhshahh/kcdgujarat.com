#!/usr/bin/env python3
"""Generate the Women in Cloud Native mixer banner as an original SVG.

Brand vocabulary comes from this repo's own assets, not from any other site:
the gold gradient, jali lattice, cusped arch, pilasters and kalash finial are
the language of public/images/jharokha.svg, and the palette is
tailwind.config.ts `theme.extend.colors.kcd`.
"""

import pathlib
import sys

W, H = 1200, 630

NAVY_A, NAVY_B = '#0A111E', '#1A2A46'
PANEL = '#111D33'
CREAM = '#F6F4ED'
SUBTLE = '#E2DCCE'

SKIN = ['#8D5524', '#C68642', '#E0AC69', '#F1C27D', '#A9714B', '#6B4423']
HAIR = ['#17202E', '#3B2314', '#5C3A21', '#0F172A', '#2B1B10', '#4A2C17']
# Brand clothing only — terracotta, heritage green, tech blue, gold, cream, slate.
WEAR = ['#E05F36', '#557B3E', '#4285F4', '#E8B321', '#EDE7DA', '#7C8AA5']

# ── geometry ────────────────────────────────────────────────────────────────
NICHE = 'M270 512 L270 300 Q282 168 600 118 Q918 168 930 300 L930 512 Z'
SPRING, FLOOR = 300, 512
TABLE = dict(cx=600, cy=452, rx=232, ry=58)


def hair_shape(style, c):
    """Silhouettes, so no two neighbours read as the same person."""
    if style == 'bun':
        return (f'<circle cx="2" cy="-148" r="13" fill="{c}"/>'
                f'<path d="M-28 -110 Q-30 -139 0 -141 Q30 -139 28 -110 Q22 -129 0 -127 Q-22 -129 -28 -110 Z" fill="{c}"/>')
    if style == 'long':
        return ('<path d="M-31 -104 Q-34 -141 0 -143 Q34 -141 31 -104 L31 -54 Q23 -70 21 -104 '
                f'Q11 -119 0 -119 Q-11 -119 -21 -104 Q-23 -70 -31 -54 Z" fill="{c}"/>')
    if style == 'bob':
        return (f'<path d="M-30 -99 Q-32 -141 0 -142 Q32 -141 30 -99 L30 -90 Q20 -111 0 -111 Q-20 -111 -30 -90 Z" fill="{c}"/>')
    if style == 'braid':
        return (f'<path d="M-29 -106 Q-31 -140 0 -142 Q31 -140 29 -106 Q20 -125 0 -123 Q-20 -125 -29 -106 Z" fill="{c}"/>'
                f'<path d="M-5 -121 Q-15 -84 -9 -50 Q1 -56 5 -84 Q7 -109 7 -121 Z" fill="{c}"/>')
    if style == 'curls':
        base = f'<path d="M-30 -104 Q-32 -141 0 -143 Q32 -141 30 -104 Q22 -123 0 -121 Q-22 -123 -30 -104 Z" fill="{c}"/>'
        pops = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>'
                       for x, y, r in ((-29, -117, 11), (-16, -135, 12), (0, -141, 12), (16, -135, 12), (29, -117, 11)))
        return base + pops
    # 'pony'
    return (f'<path d="M-29 -105 Q-31 -141 0 -143 Q31 -141 29 -105 Q21 -124 0 -122 Q-21 -124 -29 -105 Z" fill="{c}"/>'
            f'<path d="M24 -124 Q46 -112 44 -84 Q40 -60 30 -56 Q36 -84 26 -104 Z" fill="{c}"/>')


def figure(x, y, s, skin, hair, wear, style, lean=0, flip=False, back=False):
    """One seated figure, drawn upward from the seat centre (x, y).

    `back=True` turns the figure away from the viewer — near-side seats show
    hair and shoulders, no face, which is what you actually see across a table.
    """
    hairc, skinc, wearc = HAIR[hair], SKIN[skin], WEAR[wear]
    f = -1 if flip else 1
    o = [f'<g transform="translate({x} {y}) rotate({lean}) scale({s * f} {s})">']
    # Torso — rounded shoulders; the table edge crops it below.
    o.append(f'<path d="M-48 52 L-48 -4 Q-48 -60 0 -66 Q48 -60 48 -4 L48 52 Z" fill="{wearc}"/>')
    if not back:
        # Collar reads as a kurta placket.
        o.append(f'<path d="M-13 -62 Q0 -39 13 -62 Q6 -66 0 -66 Q-6 -66 -13 -62 Z" fill="{CREAM}" opacity="0.9"/>')
        o.append(f'<rect x="-11" y="-89" width="22" height="27" rx="9" fill="{skinc}"/>')
        o.append(f'<circle cx="0" cy="-109" r="27" fill="{skinc}"/>')
    else:
        o.append(f'<rect x="-11" y="-89" width="22" height="27" rx="9" fill="{skinc}"/>')
        o.append(f'<circle cx="0" cy="-109" r="27" fill="{hairc}"/>')
    o.append(hair_shape(style, hairc))
    o.append('</g>')
    return ''.join(o)


def chair(x, y, s):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<rect x="-58" y="-46" width="116" height="104" rx="32" fill="#20304B"/>'
            f'<rect x="-48" y="-36" width="96" height="90" rx="26" fill="#2A3B58"/>'
            f'</g>')


svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" fill="none" '
    'role="img" aria-label="Illustration of seven women gathered around a table inside a Gujarati jharokha arch">',
    f'''  <defs>
    <linearGradient id="gold" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#F6D673"/>
      <stop offset="0.5" stop-color="#E8B321"/>
      <stop offset="1" stop-color="#B8860B"/>
    </linearGradient>
    <linearGradient id="ground" x1="0.15" y1="0" x2="0.7" y2="1">
      <stop offset="0" stop-color="{NAVY_B}"/>
      <stop offset="1" stop-color="{NAVY_A}"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.5" cy="0.55" r="0.5">
      <stop offset="0" stop-color="#E8B321" stop-opacity="0.20"/>
      <stop offset="1" stop-color="#E8B321" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="tabletop" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{CREAM}"/>
      <stop offset="1" stop-color="{SUBTLE}"/>
    </linearGradient>
    <pattern id="jali" width="16" height="16" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <path d="M0 8H16 M8 0V16" stroke="url(#gold)" stroke-width="2.2" fill="none"/>
    </pattern>
    <clipPath id="niche"><path d="{NICHE}"/></clipPath>
  </defs>''',
    f'  <rect width="{W}" height="{H}" fill="url(#ground)"/>',
    f'  <rect width="{W}" height="{H}" fill="url(#glow)"/>',
    # Scaled about a point below centre: the card renders this ~576px wide, and
    # at that size the scene needs to fill the frame or it reads as a stamp on
    # an empty field. 1.13 is the most it takes before the kalash meets the border.
    '  <g transform="translate(600 355) scale(1.13) translate(-600 -355)">',
]

# ── the niche: a panel one step lighter than the ground, carrying the jali ──
svg.append(f'  <path d="{NICHE}" fill="{PANEL}"/>')
svg.append('  <g clip-path="url(#niche)" opacity="0.11">')
svg.append(f'    <rect width="{W}" height="{H}" fill="url(#jali)"/>')
svg.append('  </g>')

# ── cusped arch: double outline + kalash finial ─────────────────────────────
svg.append('  <g stroke-linejoin="round" stroke-linecap="round">')
svg.append('    <path d="M256 512 L256 298 Q268 156 600 104 Q932 156 944 298 L944 512" stroke="url(#gold)" stroke-width="4" fill="none"/>')
svg.append('    <path d="M272 512 L272 302 Q284 172 600 122 Q916 172 928 302 L928 512" stroke="url(#gold)" stroke-width="2" fill="none" opacity="0.7"/>')
svg.append('    <path d="M600 60 L608 82 L600 94 L592 82 Z" fill="url(#gold)"/>')
svg.append('    <circle cx="600" cy="100" r="7" fill="url(#gold)"/>')
svg.append('  </g>')

# ── pilasters: capital, shaft, base, so the arch lands on something ─────────
for cx in (264, 936):
    svg.append(f'  <g opacity="0.92">')
    svg.append(f'    <rect x="{cx - 17}" y="{SPRING - 10}" width="34" height="12" rx="3" fill="url(#gold)"/>')
    svg.append(f'    <rect x="{cx - 9}" y="{SPRING + 2}" width="18" height="{FLOOR - SPRING - 14}" fill="url(#gold)"/>')
    svg.append(f'    <rect x="{cx - 19}" y="{FLOOR - 12}" width="38" height="14" rx="3" fill="url(#gold)"/>')
    svg.append('  </g>')

# ── plinth the whole scene stands on ────────────────────────────────────────
svg.append(f'  <rect x="228" y="{FLOOR + 2}" width="744" height="11" rx="4" fill="url(#gold)" opacity="0.8"/>')
svg.append(f'  <rect x="252" y="{FLOOR + 13}" width="696" height="7" rx="3" fill="#B8860B" opacity="0.35"/>')
svg.append('  <ellipse cx="600" cy="508" rx="286" ry="24" fill="#000000" opacity="0.24"/>')

# ── far side of the table: five figures in a shallow arc, leaning inward ────
for spec in [
    # x,   y,   s,    skin hair wear style     lean  flip
    (402, 424, 0.90, 0, 0, 1, 'bun', -5, False),
    (500, 412, 0.95, 2, 1, 0, 'long', -3, False),
    (600, 404, 1.00, 4, 3, 2, 'bob', 0, False),
    (700, 412, 0.95, 1, 2, 3, 'curls', 3, True),
    (798, 424, 0.90, 3, 5, 5, 'pony', 5, True),
]:
    svg.append('  ' + figure(*spec))

# ── the table ───────────────────────────────────────────────────────────────
t = TABLE
svg.append(f'  <path d="M{t["cx"] - t["rx"]} {t["cy"]} L{t["cx"] - t["rx"]} {t["cy"] + 22} '
           f'Q{t["cx"]} {t["cy"] + 22 + t["ry"]} {t["cx"] + t["rx"]} {t["cy"] + 22} '
           f'L{t["cx"] + t["rx"]} {t["cy"]} Z" fill="#C9C1B0"/>')
svg.append(f'  <ellipse cx="{t["cx"]}" cy="{t["cy"]}" rx="{t["rx"]}" ry="{t["ry"]}" fill="url(#tabletop)"/>')
svg.append(f'  <ellipse cx="{t["cx"]}" cy="{t["cy"]}" rx="{t["rx"]}" ry="{t["ry"]}" fill="none" stroke="#B8860B" stroke-width="2" opacity="0.4"/>')

# A laptop and two cups — a working huddle, not a photo op.
svg.append('  <g>')
svg.append(f'    <path d="M506 414 L578 414 L585 440 L499 440 Z" fill="{WEAR[5]}"/>')
svg.append(f'    <path d="M496 440 L588 440 L595 449 L489 449 Z" fill="#94A1B8"/>')
for cx, col in ((632, WEAR[0]), (684, WEAR[3])):
    svg.append(f'    <path d="M{cx - 14} 432 Q{cx - 12} 452 {cx} 452 Q{cx + 12} 452 {cx + 14} 432 Z" fill="{col}"/>')
    svg.append(f'    <ellipse cx="{cx}" cy="432" rx="14" ry="6" fill="{CREAM}" opacity="0.85"/>')
svg.append('  </g>')

# ── near side: two figures with their backs to us, plus their chairs ────────
for x, y, s in ((444, 506, 0.88), (756, 506, 0.88)):
    svg.append('  ' + chair(x, y + 8, s))
for spec in [
    (444, 506, 0.88, 5, 4, 4, 'bun', 2, False, True),
    (756, 506, 0.88, 1, 0, 1, 'braid', -2, True, True),
]:
    svg.append('  ' + figure(*spec))

svg.append('  </g>')
svg.append(f'  <rect x="16" y="16" width="{W - 32}" height="{H - 32}" rx="26" stroke="url(#gold)" stroke-width="2" fill="none" opacity="0.3"/>')
svg.append('</svg>')

out = '\n'.join(svg) + '\n'
dest = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'wic.svg')
dest.write_text(out)
print(f'{dest} — {len(out)} bytes')
