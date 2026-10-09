import subprocess, sys
for i in range(2, 11):
    subprocess.run([sys.executable, 'tools/make_audio.py', 'home-%d' % i])

