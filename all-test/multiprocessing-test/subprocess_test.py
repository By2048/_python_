import subprocess

print("$ nslookup www.baidu.com")
r = subprocess.call(['nslookup', 'www.baidu.com'])
print("Exit code: ", r)
