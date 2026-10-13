# 主題 sports-3（籃球場）的場景圖：俯視的球場＋右側籃框特寫，viewBox 400×250，編號依單字順序。


def person(x, y, shirt, tall=1.0, stripes=False, sit=False):
    """站著（或坐著）的人：(x, y) 是腳底中心。"""
    h = 24 * tall
    top = y - h
    s = '<circle cx="%g" cy="%g" r="3.6" fill="#8d5a3b"/>' % (x, top + 3.6)
    s += '<rect x="%g" y="%g" width="9" height="%g" rx="2" fill="%s"/>' % (x - 4.5, top + 7.5, h * 0.42, shirt)
    if stripes:
        for i in range(3):
            s += '<rect x="%g" y="%g" width="9" height="1.4" fill="#fff"/>' % (x - 4.5, top + 9 + i * 3)
    leg_top = top + 7.5 + h * 0.42
    if sit:
        s += '<rect x="%g" y="%g" width="9" height="3" fill="#333"/>' % (x - 4.5, leg_top)
    else:
        s += '<g stroke="#333" stroke-width="2.4"><line x1="%g" y1="%g" x2="%g" y2="%g"/><line x1="%g" y1="%g" x2="%g" y2="%g"/></g>' % (
            x - 2, leg_top, x - 2.6, y, x + 2, leg_top, x + 2.6, y)
    return s


BLUE, RED = "#2f6fd6", "#d6453d"
LINE = 'fill="none" stroke="#fff" stroke-width="2"'

SVG = (
    # 球館地板與牆
    '<rect width="400" height="250" fill="#2e3440"/>'
    '<rect y="40" width="400" height="210" fill="#4a5262"/>'
    # 計分板
    '<rect x="150" y="4" width="100" height="30" rx="3" fill="#111" stroke="#666"/>'
    '<text x="170" y="15" font-size="7" fill="#ccc" text-anchor="middle">HOME</text>'
    '<text x="230" y="15" font-size="7" fill="#ccc" text-anchor="middle">GUEST</text>'
    '<text x="170" y="30" font-size="13" font-weight="800" fill="#ff5a3c" text-anchor="middle">52</text>'
    '<text x="230" y="30" font-size="13" font-weight="800" fill="#ff5a3c" text-anchor="middle">48</text>'
    '<text x="200" y="27" font-size="8" fill="#ffd34d" text-anchor="middle">4:12</text>'
    # 木地板
    '<rect x="20" y="50" width="280" height="150" fill="#e2b77a"/>'
    + ''.join('<line x1="20" y1="%d" x2="300" y2="%d" stroke="#d3a566" stroke-width="0.6"/>' % (y, y) for y in range(58, 200, 8))
    # 禁區（塗色）
    + '<rect x="20" y="100.5" width="57" height="49" fill="#c0392b"/>'
    '<rect x="243" y="100.5" width="57" height="49" fill="#c0392b"/>'
    # 中圈
    '<circle cx="160" cy="125" r="18" fill="#c0392b" opacity=".35"/>'
    # 線：邊線、底線、中線、中圈
    '<rect x="20" y="50" width="280" height="150" %s/>' % LINE
    + '<line x1="160" y1="50" x2="160" y2="200" %s/>' % LINE
    + '<circle cx="160" cy="125" r="18" %s/>' % LINE
    # 禁區框線與罰球圈
    + '<rect x="20" y="100.5" width="57" height="49" %s/><rect x="243" y="100.5" width="57" height="49" %s/>' % (LINE, LINE)
    + '<circle cx="77" cy="125" r="18" %s stroke-dasharray="4 3"/><circle cx="243" cy="125" r="18" %s stroke-dasharray="4 3"/>' % (LINE, LINE)
    # 三分線
    + '<path d="M20,59 L50,59 A67.5,67.5 0 0 1 50,191 L20,191" %s/>' % LINE
    + '<path d="M300,59 L270,59 A67.5,67.5 0 0 0 270,191 L300,191" %s/>' % LINE
    # 俯視的籃板與籃框
    + '<line x1="31" y1="115" x2="31" y2="135" stroke="#222" stroke-width="3"/><circle cx="36" cy="125" r="4" fill="none" stroke="#ff7a1a" stroke-width="2"/>'
    '<line x1="289" y1="115" x2="289" y2="135" stroke="#222" stroke-width="3"/><circle cx="284" cy="125" r="4" fill="none" stroke="#ff7a1a" stroke-width="2"/>'
    # 籃框特寫
    '<rect x="308" y="50" width="86" height="118" rx="8" fill="#dfe6ee"/>'
    '<text x="351" y="162" font-size="8" fill="#5a6472" text-anchor="middle">籃框特寫</text>'
    '<rect x="377" y="82" width="6" height="68" fill="#7d8794"/><rect x="368" y="148" width="24" height="5" fill="#5a6472"/>'
    '<rect x="361" y="86" width="18" height="4" fill="#7d8794"/>'
    '<rect x="322" y="60" width="58" height="40" fill="#fff" stroke="#333" stroke-width="1.5"/>'
    '<rect x="341" y="80" width="20" height="16" fill="none" stroke="#d6453d" stroke-width="1.6"/>'
    '<g stroke="#bbb" stroke-width="0.9"><line x1="338" y1="101" x2="344" y2="124"/><line x1="343" y1="101" x2="347" y2="124"/>'
    '<line x1="349" y1="101" x2="350" y2="124"/><line x1="354" y1="101" x2="353" y2="124"/><line x1="359" y1="101" x2="356" y2="124"/>'
    '<line x1="364" y1="101" x2="358" y2="124"/><line x1="340" y1="109" x2="362" y2="109"/><line x1="342" y1="117" x2="360" y2="117"/>'
    '<line x1="344" y1="124" x2="358" y2="124"/></g>'
    '<ellipse cx="351" cy="101" rx="13.5" ry="3" fill="none" stroke="#ff7a1a" stroke-width="2.4"/>'
    # 板凳與教練
    '<rect x="70" y="226" width="110" height="6" rx="2" fill="#8b5a2b"/>'
    '<g stroke="#5c3b1c" stroke-width="2"><line x1="76" y1="232" x2="76" y2="242"/><line x1="174" y1="232" x2="174" y2="242"/></g>'
    + person(92, 229, BLUE, sit=True) + person(112, 229, BLUE, sit=True) + person(132, 229, BLUE, sit=True)
    + person(205, 238, "#3d3d3d")
    # 場上球員：藍隊進攻右邊籃框
    + person(118, 160, BLUE) + '<circle cx="124" cy="158" r="3.6" fill="#e86a1c" stroke="#7a3300" stroke-width=".8"/>'
    + person(214, 88, BLUE) + person(262, 182, BLUE, tall=1.25)
    + person(150, 160, RED) + person(236, 98, RED) + person(276, 176, RED, tall=1.15)
    # 裁判（黑白條紋）
    + person(178, 66, "#222", stripes=True)
)

# 單字 slug → 編號圓點位置 (x, y)：圓點放在物件旁或物件上，不蓋住人物
POS = {
    "scoreboard": (262, 18),
    "coach": (219, 220),
    "bench-player": (148, 214),
    "sideline": (100, 200),
    "centerline": (160, 186),
    "dribble": (132, 166),
    "forward": (226, 72),
    "three-point-line": (95, 91),
    "referee": (191, 50),
    "foul-line": (77, 145),
    "free-throw-line": (243, 108),
    "center": (248, 176),
    "guard": (106, 140),
    "key": (55, 108),
    "backboard": (330, 68),
    "rim": (369, 103),
    "net": (351, 118),
    "baseline": (20, 172),
}
