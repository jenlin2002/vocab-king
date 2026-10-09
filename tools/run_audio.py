import subprocess, sys
flags = [a for a in sys.argv[1:] if a.startswith("--")]
for tid in [a for a in sys.argv[1:] if not a.startswith("--")]:
    subprocess.run([sys.executable, "tools/make_audio.py", tid] + flags)
