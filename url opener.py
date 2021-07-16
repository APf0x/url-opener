import subprocess
import time

f = open("urls.txt")
for url in f.readlines():
    urls = url.strip()
    print(urls)
    subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "-incognito", urls])
