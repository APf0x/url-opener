import subprocess
import time

f = open("urls.txt")
for url in f.readlines():
    urls = url.strip()
    print(urls)
    subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "-incognito", urls])

#subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "-incognito", urls]])




'''
import subprocess
import time

f = open("urls.txt")
urls = [url.strip() for url in f.readlines()]

print(urls)



# subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "-incognito", urls]])
'''
