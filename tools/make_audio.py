"""替主題產生語音（Kokoro TTS，不使用書附 MP3）。只產生缺少的檔案。
用法：python tools/make_audio.py home-1
檔案：audio/<主題>/w-<單字>.mp3（單字，稍慢）、e-<單字>.mp3（例句）、d-<序號>.mp3（對話，依角色聲音）
需要：pip install kokoro-onnx soundfile imageio-ffmpeg；模型放在 KOKORO_DIR（預設借用 ../daily_life_listening/tools/models）"""
import os, sys, json, subprocess, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
tid = sys.argv[1]
src = open(os.path.join(ROOT, "topics", tid + ".js"), encoding="utf-8").read()
T = json.loads(src[src.index("=") + 1:].strip().rstrip(";"))
outdir = os.path.join(ROOT, "audio", tid)
os.makedirs(outdir, exist_ok=True)

jobs = []   # (檔名, 文字, 聲音, 速度)
for w in T["words"]:
    jobs.append(("w-%s.mp3" % w["slug"], w["w"], "af_heart", 0.85))
    jobs.append(("e-%s.mp3" % w["slug"], w["ex"], "af_heart", 0.95))
for i, l in enumerate(T["dialogue"], 1):
    jobs.append(("d-%02d.mp3" % i, l["en"], T["speakers"][l["s"]]["voice"], 0.95))
todo = [j for j in jobs if not os.path.isfile(os.path.join(outdir, j[0]))]
print("需要 %d 個，缺少 %d 個" % (len(jobs), len(todo)))
if not todo:
    sys.exit(0)

import imageio_ffmpeg, soundfile as sf
from kokoro_onnx import Kokoro
FF = imageio_ffmpeg.get_ffmpeg_exe()
md = os.environ.get("KOKORO_DIR", os.path.join(ROOT, "..", "daily_life_listening", "tools", "models"))
k = Kokoro(os.path.join(md, "kokoro-v1.0.int8.onnx"), os.path.join(md, "voices-v1.0.bin"))
for n, (fn, text, voice, speed) in enumerate(todo, 1):
    samples, sr = k.create(text, voice=voice, speed=speed, lang="en-us")
    path = os.path.join(outdir, fn)
    sf.write(path + ".wav", samples, sr)
    subprocess.run([FF, "-y", "-loglevel", "error", "-i", path + ".wav", "-ac", "1", "-ar", "24000", "-b:a", "48k", path], check=True)
    os.remove(path + ".wav")
    print("[%d/%d] %s" % (n, len(todo), text[:50]), flush=True)
