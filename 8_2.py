import re


RE_REMOTE_ADDR = re.compile(r'^(\b\d+\.\d+\.\d+\.\d+).+\[(.+)\].+"(\w+)\s(/\w+/\w+).+"\s(\d+)\s(\d+)')
with open("nginx_logs.txt") as f:
    for line in f:
        try:
            print(RE_REMOTE_ADDR.findall(line)[0])
        except IndexError:
            pass

