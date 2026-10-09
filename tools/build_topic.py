"""把 tools/data_<名稱>.py 的 TOPIC 寫成 topics/<id>.js（window.TOPIC = {...}），並更新 topics/index.js 的主題清單。
用法：python tools/build_topic.py home1"""
import os, sys, json, re, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)


def slug(w):
    return re.sub(r"[^a-z0-9]+", "-", w.lower()).strip("-")


name = sys.argv[1]
spec = importlib.util.spec_from_file_location("d", os.path.join(HERE, "data_%s.py" % name))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
T = m.TOPIC
out = dict(
    id=T["id"], cat=T["cat"], title=T["title"], titleEn=T["titleEn"], emoji=T["emoji"],
    words=[dict(w=w, slug=slug(w), zh=zh, pos=pos, emoji=em, ex=ex, exzh=exzh) for w, zh, pos, em, ex, exzh in T["words"]],
    speakers=T["speakers"], dialogueTitle=T["dialogueTitle"],
    dialogue=[dict(s=s, en=en, zh=zh) for s, en, zh in T["dialogue"]],
)
sc = os.path.join(HERE, "scene_%s.py" % name)
if os.path.isfile(sc):   # 有場景圖的主題：附上 SVG 與各單字的編號位置
    sp = importlib.util.spec_from_file_location("s", sc); sm = importlib.util.module_from_spec(sp); sp.loader.exec_module(sm)
    miss = [w["slug"] for w in out["words"] if w["slug"] not in sm.POS]
    assert not miss, "場景圖缺少位置：%s" % miss
    out["scene"] = dict(svg=sm.SVG.strip(), pos={k: list(v) for k, v in sm.POS.items()})
if "scene" not in out:   # 居家 2～10：場景圖在 scenes_home.py
    import scenes_home as SH
    s = SH.SCENES.get(name)
    if s:
        pos = s["pos"]
        if not pos:   # 物件集合類：自動排成架子
            cols = {"home5": 7, "home9": 6, "home10": 7}[name]
            rows = SH.grid(len(out["words"]), cols)
            pos = {w["slug"]: (x, y, "e") for w, (x, y) in zip(out["words"], rows)}
        slugs = {w["slug"] for w in out["words"]}
        miss = [k for k in slugs if k not in pos]; extra = [k for k in pos if k not in slugs]
        assert not miss and not extra, "場景圖位置不符：缺 %s、多 %s" % (miss, extra)
        out["scene"] = dict(svg=s["svg"].strip(), pos={k: list(v) for k, v in pos.items()})
os.makedirs(os.path.join(ROOT, "topics"), exist_ok=True)
with open(os.path.join(ROOT, "topics", T["id"] + ".js"), "w", encoding="utf-8", newline="\n") as f:
    f.write("window.TOPIC = " + json.dumps(out, ensure_ascii=False, indent=1) + ";\n")
print("wrote topics/%s.js：%d 個單字、%d 句對話" % (T["id"], len(out["words"]), len(out["dialogue"])))
