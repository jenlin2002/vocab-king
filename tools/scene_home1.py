# 主題 home-1 的場景圖（自己畫的簡單 SVG，viewBox 400×250），編號依單字順序。
SVG = """
<rect width="400" height="165" fill="#bfe3f7"/><circle cx="360" cy="30" r="16" fill="#ffe27a"/>
<rect y="160" width="400" height="90" fill="#8fcf72"/>
<rect x="240" y="48" width="18" height="40" fill="#a0522d"/><rect x="236" y="44" width="26" height="6" fill="#7a3f1d"/>
<rect x="100" y="90" width="190" height="92" fill="#f6ead0" stroke="#b9a77d"/>
<polygon points="92,92 195,32 298,92" fill="#3b5ba5"/>
<polygon points="136,76 150,58 164,76" fill="#e9dcc0" stroke="#7a6a45"/><rect x="142" y="66" width="16" height="10" fill="#cfe8ff" stroke="#6b7a8a"/>
<rect x="215" y="62" width="20" height="13" fill="#cfe8ff" stroke="#6b7a8a" transform="rotate(-24 225 68)"/>
<rect x="304" y="108" width="76" height="74" fill="#efe3c6" stroke="#b9a77d"/><polygon points="298,110 342,78 386,110" fill="#3b5ba5"/>
<rect x="312" y="136" width="60" height="46" fill="#d3d3d3" stroke="#8a8a8a"/><g stroke="#aaa"><line x1="312" y1="148" x2="372" y2="148"/><line x1="312" y1="160" x2="372" y2="160"/><line x1="312" y1="172" x2="372" y2="172"/></g>
<polygon points="312,182 372,182 392,250 296,250" fill="#b5b5b5"/>
<rect x="108" y="116" width="46" height="38" fill="#cfe8ff" stroke="#6b7a8a"/><rect x="110" y="118" width="9" height="34" fill="#d6453d"/><rect x="143" y="118" width="9" height="34" fill="#d6453d"/>
<rect x="159" y="112" width="34" height="40" fill="#cfe8ff" stroke="#6b7a8a"/><g stroke="#8a97a6"><line x1="159" y1="120" x2="193" y2="120"/><line x1="159" y1="128" x2="193" y2="128"/><line x1="159" y1="136" x2="193" y2="136"/><line x1="159" y1="144" x2="193" y2="144"/></g>
<rect x="152" y="112" width="7" height="40" fill="#2f5fb3"/><rect x="193" y="112" width="7" height="40" fill="#2f5fb3"/>
<rect x="208" y="130" width="26" height="52" fill="#8b5a2b"/><circle cx="228" cy="158" r="2" fill="#ffd966"/>
<rect x="202" y="182" width="38" height="8" fill="#c8b890" stroke="#9d8c60"/>
<rect x="244" y="124" width="36" height="58" fill="#cfe8ff" stroke="#6b7a8a"/><line x1="262" y1="124" x2="262" y2="182" stroke="#6b7a8a"/>
<rect x="238" y="108" width="48" height="6" fill="#8b5a2b"/><g stroke="#8b5a2b"><line x1="241" y1="114" x2="241" y2="124"/><line x1="283" y1="114" x2="283" y2="124"/></g>
<g fill="#4c8f3a"><circle cx="292" cy="186" r="11"/><circle cx="276" cy="190" r="9"/><circle cx="104" cy="186" r="10"/><circle cx="90" cy="190" r="8"/></g>
<rect x="38" y="196" width="34" height="22" fill="#c98b4a" stroke="#7a4a1d"/><polygon points="34,196 55,178 76,196" fill="#8a4b2a"/><ellipse cx="55" cy="212" rx="7" ry="6" fill="#3a2a20"/>
<g><rect x="118" y="206" width="28" height="12" rx="3" fill="#d6453d"/><circle cx="124" cy="220" r="5" fill="#333"/><circle cx="142" cy="220" r="5" fill="#333"/><line x1="146" y1="206" x2="158" y2="190" stroke="#555" stroke-width="3"/></g>
<text x="82" y="224" font-size="16">🐕</text>
<text x="170" y="236" font-size="20">💦</text><rect x="178" y="226" width="14" height="5" fill="#ffcc00" stroke="#8a6d00"/>
<text x="265" y="76" font-size="20">📡</text>
<rect x="336" y="200" width="30" height="14" rx="4" fill="#d6453d"/><circle cx="342" cy="216" r="3" fill="#333"/><circle cx="360" cy="216" r="3" fill="#333"/>
"""
# 單字 slug → 編號圓點的位置（x, y）
POS = {
    "chimney": (249, 48), "dormer": (150, 70), "satellite-dish": (277, 68), "skylight": (226, 62),
    "garage": (342, 160), "venetian-blind": (176, 124), "bay-window": (131, 152), "dog-house": (55, 205),
    "shutters": (197, 148), "front-step": (221, 186), "curtains": (114, 122), "sliding-glass-door": (262, 150),
    "balcony": (262, 108), "lawn-mower": (132, 212), "driveway": (345, 230), "bushes": (96, 178), "sprinkler": (185, 232),
}
