import time
from datetime import datetime as dt
hosts_temp="hosts"
hosts_path="/etc/hosts"
redirect="127.0.0.1"
website_list=["www.amazon.com","www.wish.com","www.ebay.com","www.goal.com","www.youtube.com"]
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,0) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23):
        print("Hello")
        with open(hosts_path,'r+') as file:
            contents=file.read()
            for website in website_list:
                if website in contents:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")

    else:
        print("not working")
        with open(hosts_path,'r+') as file:
            contents=file.readlines()
            file.seek(0)
            for line in contents:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
time.sleep(5)
