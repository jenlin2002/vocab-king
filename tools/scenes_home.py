"""居家主題 2～10 的場景圖（自己畫的簡單 SVG，viewBox 400×250）。
POS[slug] = (x, y)      → 編號圓點直接放在圖上的那個物件上
POS[slug] = (x, y, 'e') → 在該處放該單字的 emoji，編號圓點貼在右上角
物件很多的主題（盥洗用品、廚房用具、工具）用 grid() 排成架子。"""


def grid(n, cols, x0=34, dx=57, y0=48, dy=70):
    pos, rows = {}, []
    for i in range(n):
        r, c = divmod(i, cols)
        rows.append((x0 + c * dx, y0 + r * dy + 12))
    return rows


def shelves(rows_n, color="#9b6b3a"):
    s = '<rect width="400" height="250" fill="#f3ead6"/>'
    for r in range(rows_n):
        y = 78 + r * 70
        s += '<rect x="10" y="%d" width="380" height="7" fill="%s"/><rect x="10" y="%d" width="380" height="3" fill="#00000022"/>' % (y, color, y + 7)
    return s


ROOM = '<rect width="400" height="250" fill="#f1e4c8"/><rect width="400" height="16" fill="#fafafa"/><rect y="170" width="400" height="80" fill="#c58f55"/><g stroke="#a8763f"><line x1="0" y1="190" x2="400" y2="190"/><line x1="0" y1="212" x2="400" y2="212"/><line x1="0" y1="234" x2="400" y2="234"/></g>'

SCENES = {}

# ---- home-2 客廳（一）
SCENES["home2"] = dict(svg=ROOM + """
<rect x="16" y="70" width="40" height="100" fill="#8b5a2b"/><circle cx="48" cy="122" r="3" fill="#ffd966"/>
<rect x="62" y="36" width="26" height="32" fill="#fff" stroke="#999"/><rect x="62" y="36" width="26" height="8" fill="#d6453d"/>
<rect x="62" y="96" width="8" height="12" fill="#fff" stroke="#999"/>
<rect x="105" y="40" width="40" height="30" fill="#8ec5e8" stroke="#8b5a2b" stroke-width="3"/><polygon points="105,70 120,55 135,66 145,58 145,70" fill="#6aa84f"/>
<circle cx="200" cy="48" r="11" fill="#fff" stroke="#555" stroke-width="2"/><line x1="200" y1="48" x2="200" y2="41" stroke="#333"/><line x1="200" y1="48" x2="206" y2="50" stroke="#333"/>
<line x1="255" y1="70" x2="255" y2="170" stroke="#555" stroke-width="3"/><polygon points="240,70 270,70 262,48 248,48" fill="#f7e08a" stroke="#b8a04a"/>
<rect x="270" y="135" width="60" height="32" fill="#6b4a2a"/><rect x="275" y="98" width="50" height="34" fill="#222" stroke="#555"/><rect x="279" y="102" width="42" height="26" fill="#3b6fa0"/>
<rect x="340" y="60" width="52" height="110" fill="#9b6b3a"/><g stroke="#6b4a2a"><line x1="340" y1="97" x2="392" y2="97"/><line x1="340" y1="134" x2="392" y2="134"/></g><g><rect x="346" y="68" width="8" height="26" fill="#d6453d"/><rect x="356" y="72" width="8" height="22" fill="#2f5fb3"/><rect x="346" y="106" width="8" height="26" fill="#6aa84f"/></g>
<ellipse cx="190" cy="214" rx="100" ry="24" fill="#b23a3a"/><ellipse cx="190" cy="214" rx="78" ry="17" fill="#c95757"/>
<rect x="70" y="108" width="130" height="30" rx="6" fill="#2f5199"/><rect x="70" y="128" width="130" height="42" rx="8" fill="#3a63b5"/><rect x="172" y="120" width="22" height="20" fill="#fff" stroke="#bbb"/>
<rect x="120" y="190" width="70" height="8" fill="#6b4a2a"/><rect x="126" y="198" width="5" height="14" fill="#6b4a2a"/><rect x="180" y="198" width="5" height="14" fill="#6b4a2a"/>
""", pos={"ceiling": (200, 8), "wall": (92, 88), "clock": (200, 48), "painting": (125, 55), "television": (300, 115), "tv-stand": (300, 152),
          "bookcase": (366, 112), "floor-lamp": (255, 110), "hardwood-floor": (360, 222), "rug": (112, 224), "headphones": (222, 222, 'e'),
          "coffee-table": (155, 194), "throw-pillow": (183, 130), "sofa": (95, 152), "chair": (265, 192, 'e'), "calendar": (75, 52),
          "light-switch": (66, 102), "door": (36, 120)})

# ---- home-3 客廳（二）
SCENES["home3"] = dict(svg=ROOM + """
<rect x="30" y="28" width="96" height="30" rx="4" fill="#fff" stroke="#9aa" /><g stroke="#bcd"><line x1="38" y1="46" x2="118" y2="46"/><line x1="38" y1="52" x2="118" y2="52"/></g><circle cx="108" cy="38" r="3" fill="#6c6"/>
<rect x="298" y="150" width="44" height="34" fill="#8b5a2b"/><rect x="302" y="184" width="5" height="22" fill="#6b4a2a"/><rect x="333" y="184" width="5" height="22" fill="#6b4a2a"/>
<rect x="36" y="196" width="80" height="8" fill="#6b4a2a"/><rect x="42" y="204" width="5" height="14" fill="#6b4a2a"/><rect x="105" y="204" width="5" height="14" fill="#6b4a2a"/>
<rect x="60" y="150" width="46" height="34" rx="6" fill="#b5651d"/>
""", pos={"air-conditioner": (78, 42), "armchair": (84, 168, 'e'), "recliner": (170, 170, 'e'), "rocking-chair": (245, 176, 'e'),
          "end-table": (320, 172), "vase": (320, 138, 'e'), "telephone": (370, 160, 'e'), "lighter": (56, 190, 'e'), "matches": (96, 190, 'e'),
          "waste-basket": (160, 228, 'e'), "vacuum-cleaner": (235, 228, 'e')})

# ---- home-4 浴室
SCENES["home4"] = dict(svg="""
<rect width="400" height="250" fill="#cdeaf5"/><g stroke="#a6d0e0"><line x1="0" y1="40" x2="400" y2="40"/><line x1="0" y1="80" x2="400" y2="80"/><line x1="0" y1="120" x2="400" y2="120"/><line x1="0" y1="160" x2="400" y2="160"/><line x1="50" y1="0" x2="50" y2="170"/><line x1="100" y1="0" x2="100" y2="170"/><line x1="150" y1="0" x2="150" y2="170"/><line x1="200" y1="0" x2="200" y2="170"/><line x1="250" y1="0" x2="250" y2="170"/><line x1="300" y1="0" x2="300" y2="170"/><line x1="350" y1="0" x2="350" y2="170"/></g>
<rect y="170" width="400" height="80" fill="#dfe6ea"/><g stroke="#c1ccd2"><line x1="0" y1="210" x2="400" y2="210"/><line x1="100" y1="170" x2="100" y2="250"/><line x1="200" y1="170" x2="200" y2="250"/><line x1="300" y1="170" x2="300" y2="250"/></g>
<rect x="55" y="45" width="60" height="50" fill="#e8f6ff" stroke="#8aa" stroke-width="3"/>
<rect x="140" y="70" width="70" height="6" fill="#9b6b3a"/><rect x="146" y="76" width="22" height="30" fill="#f2a1b3"/><rect x="170" y="52" width="10" height="18" fill="#7fb77e"/>
<rect x="50" y="125" width="70" height="14" rx="5" fill="#fff" stroke="#9ab"/><rect x="74" y="139" width="22" height="40" fill="#fff" stroke="#9ab"/><rect x="82" y="112" width="6" height="13" fill="#999"/>
<rect x="148" y="108" width="34" height="26" fill="#fff" stroke="#9ab"/><ellipse cx="165" cy="164" rx="22" ry="14" fill="#fff" stroke="#9ab"/><rect x="152" y="150" width="26" height="14" fill="#fff"/>
<rect x="248" y="40" width="140" height="70" fill="#bfe8c8" opacity=".85" stroke="#6a9"/><line x1="248" y1="36" x2="388" y2="36" stroke="#777" stroke-width="3"/><rect x="262" y="38" width="18" height="6" rx="3" fill="#888"/>
<rect x="244" y="140" width="148" height="60" rx="14" fill="#fff" stroke="#9ab" stroke-width="2"/><circle cx="320" cy="186" r="4" fill="#9ab"/>
<rect x="212" y="206" width="64" height="12" rx="3" fill="#6bb36b"/>
""", pos={"tile": (125, 112), "bath-towel": (157, 92), "bathroom-shelves": (192, 62), "mirror": (85, 70), "washcloth": (112, 122, 'e'),
          "sink": (85, 152), "faucet": (85, 118), "toilet-paper": (205, 128, 'e'), "drain": (320, 187), "toilet-tank": (165, 120),
          "toilet": (165, 168), "bath-mat": (244, 212), "shower-curtain": (330, 75), "shower-head": (270, 38), "bathtub": (360, 168)})

# ---- home-5 盥洗與個人用品（19）
# ---- home-6 臥室
SCENES["home6"] = dict(svg=ROOM + """
<rect x="12" y="50" width="62" height="122" fill="#8b5a2b"/><line x1="43" y1="50" x2="43" y2="172" stroke="#5e3b17"/><circle cx="38" cy="112" r="2" fill="#ffd966"/><circle cx="48" cy="112" r="2" fill="#ffd966"/>
<rect x="190" y="38" width="40" height="30" fill="#fff" stroke="#8b5a2b" stroke-width="3"/><circle cx="210" cy="52" r="7" fill="#f2c27a"/>
<rect x="118" y="82" width="152" height="60" rx="6" fill="#7a4b2a"/><rect x="108" y="138" width="172" height="30" rx="5" fill="#fff" stroke="#ccc"/>
<rect x="108" y="150" width="172" height="26" rx="5" fill="#4a8fd0"/><rect x="132" y="120" width="44" height="18" rx="6" fill="#fff" stroke="#ccc"/>
<rect x="288" y="152" width="36" height="32" fill="#8b5a2b"/><rect x="332" y="132" width="58" height="52" fill="#a8703b"/><g stroke="#6b4a2a"><line x1="332" y1="149" x2="390" y2="149"/><line x1="332" y1="166" x2="390" y2="166"/></g>
<rect x="18" y="204" width="72" height="8" fill="#6b4a2a"/><rect x="24" y="212" width="5" height="12" fill="#6b4a2a"/><rect x="80" y="212" width="5" height="12" fill="#6b4a2a"/><rect x="36" y="176" width="36" height="26" fill="#e8f6ff" stroke="#8aa"/>
""", pos={"alarm-clock": (306, 142, 'e'), "picture-frame": (210, 50), "lamp": (295, 120, 'e'), "headboard-cabinet": (230, 100), "nightstand": (306, 175),
          "pillow": (154, 129), "mattress": (121, 160), "bedsheet": (200, 148), "comforter": (250, 168), "chest-of-drawers": (361, 175),
          "bookends": (360, 118, 'e'), "wardrobe": (43, 90), "cosmetics": (36, 192, 'e'), "vanity-table": (54, 208), "footstool": (130, 222, 'e'),
          "undershirt": (200, 224, 'e'), "slippers": (260, 224, 'e')})

# ---- home-7 地下室洗衣
SCENES["home7"] = dict(svg="""
<rect width="400" height="250" fill="#d9d9d4"/><rect y="170" width="400" height="80" fill="#9a9a96"/>
<rect x="20" y="95" width="70" height="75" rx="4" fill="#fff" stroke="#999"/><circle cx="55" cy="138" r="20" fill="#cde" stroke="#889" stroke-width="3"/><rect x="28" y="101" width="22" height="6" fill="#bbb"/>
<rect x="96" y="95" width="70" height="75" rx="4" fill="#f4f4f4" stroke="#999"/><circle cx="131" cy="138" r="20" fill="#dde" stroke="#889" stroke-width="3"/><rect x="104" y="101" width="22" height="6" fill="#bbb"/>
<rect x="190" y="64" width="124" height="6" fill="#8b5a2b"/><rect x="198" y="70" width="5" height="12" fill="#6b4a2a"/><rect x="302" y="70" width="5" height="12" fill="#6b4a2a"/>
<line x1="320" y1="58" x2="392" y2="58" stroke="#666" stroke-width="3"/>
<rect x="196" y="150" width="108" height="8" fill="#9b6b3a"/><rect x="202" y="158" width="5" height="40" fill="#6b4a2a"/><rect x="293" y="158" width="5" height="40" fill="#6b4a2a"/>
<polygon points="296,205 392,205 396,212 292,212" fill="#c9c9a0" stroke="#887"/><line x1="320" y1="212" x2="312" y2="236" stroke="#666" stroke-width="3"/><line x1="372" y1="212" x2="380" y2="236" stroke="#666" stroke-width="3"/>
""", pos={"detergent": (205, 55, 'e'), "fabric-softener": (240, 55, 'e'), "bleach": (275, 55, 'e'), "sewing-machine": (218, 138, 'e'),
          "hanger": (335, 48, 'e'), "safety-pin": (365, 48, 'e'), "needle": (292, 138, 'e'), "cloth": (222, 186, 'e'), "clothes-pin": (385, 48, 'e'),
          "thread": (255, 138, 'e'), "scissors": (330, 138, 'e'), "ironing-board": (344, 218), "iron": (350, 192, 'e'), "yarn": (265, 190, 'e'),
          "dryer": (131, 138), "washing-machine": (55, 138)})

# ---- home-8 廚房
SCENES["home8"] = dict(svg="""
<rect width="400" height="250" fill="#fbf1d6"/><rect y="172" width="400" height="78" fill="#d8c7a0"/><g stroke="#c4b283"><line x1="0" y1="200" x2="400" y2="200"/><line x1="0" y1="228" x2="400" y2="228"/></g>
<rect x="95" y="24" width="70" height="56" fill="#b87a3a" stroke="#7a4a1d"/><line x1="130" y1="24" x2="130" y2="80" stroke="#7a4a1d"/>
<polygon points="176,60 236,60 226,28 186,28" fill="#c8ccd0" stroke="#889"/><rect x="198" y="14" width="16" height="14" fill="#c8ccd0" stroke="#889"/>
<rect x="246" y="24" width="82" height="56" fill="#b87a3a" stroke="#7a4a1d"/><line x1="287" y1="24" x2="287" y2="80" stroke="#7a4a1d"/>
<rect x="95" y="118" width="234" height="54" fill="#a8703b"/><rect x="95" y="112" width="234" height="8" fill="#e8e0cf"/>
<rect x="100" y="116" width="50" height="6" fill="#aab" /><rect x="176" y="112" width="60" height="6" fill="#444"/><rect x="180" y="136" width="52" height="32" fill="#333" stroke="#777"/><rect x="186" y="142" width="40" height="18" fill="#556"/>
<rect x="334" y="38" width="56" height="134" rx="4" fill="#e8ecef" stroke="#9aa"/><line x1="334" y1="86" x2="390" y2="86" stroke="#9aa"/>
""", pos={"apron": (30, 55, 'e'), "mop": (30, 150, 'e'), "broom": (60, 150, 'e'), "dust-pan": (92, 205, 'e'), "range-fan": (206, 46), "cupboard": (130, 52),
          "microwave-oven": (275, 100, 'e'), "dish-rack": (150, 102, 'e'), "ladle": (172, 86, 'e'), "cleaver": (243, 88, 'e'), "pan": (192, 100, 'e'),
          "wok": (222, 100, 'e'), "gas-stove": (206, 114), "sink": (118, 118), "counter": (112, 154), "cutting-board": (252, 102, 'e'),
          "oven": (206, 152), "cabinet": (287, 52), "blender": (305, 100, 'e'), "rice-cooker": (150, 222, 'e'), "toaster": (318, 126, 'e'),
          "refrigerator": (362, 105)})

# ---- home-9 廚房用具（18）、home-10 工具（20）：架子排列
SCENES["home5"] = dict(svg=shelves(3), pos={})
SCENES["home9"] = dict(svg=shelves(3), pos={})
SCENES["home10"] = dict(svg=shelves(3), pos={})


