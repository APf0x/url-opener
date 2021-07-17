import subprocess
import time
import random

f = open("urls.txt")
lines = f.readlines()
num = 13 # how many to open
random.shuffle(lines)
for i in range(num):
    url = lines[i]
    url = url.strip()
    print(url)
    subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "-incognito", url])
    time.sleep(1)
