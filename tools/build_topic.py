"""把主題資料寫成 topics/<id>.js（window.TOPIC = {...}），並重建 topics/catalog.js（目錄頁用的主題清單）。
資料來源（二選一）：
  tools/data_<名稱>.py  （居家 10 個主題，TOPIC 字典）
  tools/txt/<名稱>.txt  （其餘主題，簡易文字格式，見 tools/txt/README.txt）
用法：python tools/build_topic.py <名稱> [<名稱> ...]      例：python tools/build_topic.py school1
      python tools/build_topic.py                          只重建 topics/catalog.js
場景圖：scene_<名稱>.py（home-1）、scenes_home.py（居家 2～10）；沒有的主題自動把單字 emoji 排成架子。"""
import os, sys, json, re, glob, importlib.util, math

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)


def slug(w):
    return re.sub(r"[^a-z0-9]+", "-", w.lower()).strip("-")


def load_py(path):
    spec = importlib.util.spec_from_file_location("d", path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def parse_txt(path):
    """格式：開頭 key: value 幾行，接著 --words 區（單字|中文|詞性|emoji|例句|例句中文），再 --dialogue 區（角色|英文|中文）。"""
    meta, words, dlg, mode = {}, [], [], "meta"
    for raw in open(path, encoding="utf-8").read().split("\n"):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line == "--words": mode = "words"; continue
        if line == "--dialogue": mode = "dlg"; continue
        if mode == "meta":
            k, v = line.split(":", 1); meta[k.strip()] = v.strip()
        elif mode == "words":
            p = [x.strip() for x in line.split("|")]
            assert len(p) == 6, "單字行要有 6 欄：%s" % line
            words.append(tuple(p))
        else:
            p = [x.strip() for x in line.split("|")]
            assert len(p) == 3, "對話行要有 3 欄：%s" % line
            dlg.append(tuple(p))
    sp = {}
    for item in meta["speakers"].split(";"):
        key, val = item.strip().split("=")
        name, zh, avatar, voice = val.split("|")
        sp[key.strip()] = dict(name=name, zh=zh, avatar=avatar, voice=voice)
    return dict(id=meta["id"], cat=meta["cat"], title=meta["title"], titleEn=meta["titleEn"], emoji=meta["emoji"],
                words=words, speakers=sp, dialogueTitle=meta["dialogueTitle"], dialogue=dlg)


def shelves(rows_n):
    h = 40 + rows_n * 70
    s = '<rect width="400" height="%d" fill="#f3ead6"/>' % h
    for r in range(rows_n):
        y = 78 + r * 70
        s += '<rect x="10" y="%d" width="380" height="7" fill="#9b6b3a"/><rect x="10" y="%d" width="380" height="3" fill="#00000022"/>' % (y, y + 7)
    return s, h


def build(name):
    py = os.path.join(HERE, "data_%s.py" % name)
    tx = os.path.join(HERE, "txt", "%s.txt" % name)
    T = load_py(py).TOPIC if os.path.isfile(py) else parse_txt(tx)
    seen = set()
    for w in T["words"]:
        assert slug(w[0]) not in seen, "單字重複：%s" % w[0]
        seen.add(slug(w[0]))
    out = dict(
        id=T["id"], cat=T["cat"], title=T["title"], titleEn=T["titleEn"], emoji=T["emoji"],
        words=[dict(w=w, slug=slug(w), zh=zh, pos=pos, emoji=em, ex=ex, exzh=exzh) for w, zh, pos, em, ex, exzh in T["words"]],
        speakers=T["speakers"], dialogueTitle=T["dialogueTitle"],
        dialogue=[dict(s=s, en=en, zh=zh) for s, en, zh in T["dialogue"]],
    )
    slugs = [w["slug"] for w in out["words"]]
    scene = None
    sc = os.path.join(HERE, "scene_%s.py" % name)
    if os.path.isfile(sc):
        m = load_py(sc)
        scene = dict(svg=m.SVG.strip(), pos={k: list(v) for k, v in m.POS.items()}, h=250)
    else:
        try:
            import scenes_home as SH
            s = SH.SCENES.get(name)
        except ImportError:
            s = None
        if s and s["pos"]:
            scene = dict(svg=s["svg"].strip(), pos={k: list(v) for k, v in s["pos"].items()}, h=250)
        else:   # 自動排成架子（居家 5、9、10 與其餘所有主題）
            n = len(slugs)
            cols = 6 if n <= 18 else 7 if n <= 21 else 8 if n <= 24 else 9
            rows_n = math.ceil(n / cols)
            svg, h = shelves(rows_n)
            dx = 350 / cols
            pos = {}
            for i, sl in enumerate(slugs):
                r, c = divmod(i, cols)
                pos[sl] = [round(30 + c * dx + dx / 2 - 14), 48 + r * 70 + 12, "e"]
            scene = dict(svg=svg, pos=pos, h=h)
    miss = [k for k in slugs if k not in scene["pos"]]
    extra = [k for k in scene["pos"] if k not in slugs]
    assert not miss and not extra, "場景圖位置不符：缺 %s、多 %s" % (miss, extra)
    out["scene"] = scene
    os.makedirs(os.path.join(ROOT, "topics"), exist_ok=True)
    with open(os.path.join(ROOT, "topics", T["id"] + ".js"), "w", encoding="utf-8", newline="\n") as f:
        f.write("window.TOPIC = " + json.dumps(out, ensure_ascii=False, indent=1) + ";\n")
    print("wrote topics/%s.js：%d 個單字、%d 句對話" % (T["id"], len(out["words"]), len(out["dialogue"])))


def catalog():
    cat = {}
    for p in glob.glob(os.path.join(ROOT, "topics", "*.js")):
        if os.path.basename(p) == "catalog.js":
            continue
        src = open(p, encoding="utf-8").read()
        T = json.loads(src[src.index("=") + 1:].strip().rstrip(";"))
        cat.setdefault(T["cat"], []).append(dict(id=T["id"], e=T["emoji"], t=T["title"], en=T["titleEn"], n=len(T["words"])))
    for k in cat:
        cat[k].sort(key=lambda x: int(x["id"].rsplit("-", 1)[1]))
    with open(os.path.join(ROOT, "topics", "catalog.js"), "w", encoding="utf-8", newline="\n") as f:
        f.write("window.CATALOG = " + json.dumps(cat, ensure_ascii=False, indent=1) + ";\n")
    print("wrote topics/catalog.js：%d 類、%d 個主題" % (len(cat), sum(len(v) for v in cat.values())))


if __name__ == "__main__":
    for a in [a for a in sys.argv[1:] if not a.startswith("--")]:
        build(a)
    catalog()
