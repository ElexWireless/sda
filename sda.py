import random
import requests
import socket
import ctypes
import concurrent.futures

def xx(i):

    while True:

        try:
        
            p = random.randint(0,255)
            q= random.randint(0,255)
            r=random.randint(0,255)
            s=random.randint(0,255)
            
            ip = [str(p),str(q),str(r),str(s)]
            x = ".".join(ip)

            url = "http://"+x

            r1 = requests.get(url,timeout=2)

            if r1.status_code == 200 or r1.status_code == 201 or r1.status_code == 202 or r1.status_code == 203 or r1.status_code == 301:
                print(url+" [VALID WEBSITE]")

                xpsN.append(x)
                
                ctypes.windll.kernel32.SetConsoleTitleW(f"SDA HARVESTER | Total Websites Found: {len(xpsN)}")
                

                dd = open("valid websites.txt","a+")
                dd.writelines(url+"\n")
                dd.close()

                asd = open("valid websiteIP.txt","a+")
                asd.writelines(x+"\n")
                asd.close()


            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(2)
            result=sock.connect_ex((x,80))
            result1=sock.connect_ex((x,443))
            
            result2=sock.connect_ex((x,8080))
            result3=sock.connect_ex((x,3128))
            result4=sock.connect_ex((x,3389))
            result5=sock.connect_ex((x,2082))
            result6=sock.connect_ex((x,2083))
            result7=sock.connect_ex((x,2086))
            result8=sock.connect_ex((x,2087))

            host = x

            if result == 0:
                print(host+" | 80 OPEN |")

                proxy = host+":"+80
                proxy

                r = requests.get("http://httpbin.org/ip" , proxies={"http":proxy,"https":proxy},timeout=5)
                print(r)
                if r.status_code == "200":
                    print(host+"Valid Proxy")
                else:
                    print(host+" no proxy")

            if result1 ==0:
                print(host+" | 443 OPEN |")

                dd = open("https sites.txt","a+")
                dd.writelines(host+"\n")
                dd.close()
                
                proxy = host+":"+443

                r = requests.get("http://httpbin.org/ip" , proxy={http:proxy,https:proxy},timeout=5)
                if r.status_code == "200":
                    print(host+"Valid Proxy")

            if result2 ==0:
                print(host+" | 8080 OPEN |")
                proxy = host+":"+8080

                r = requests.get("http://httpbin.org/ip" , proxy={http:proxy,https:proxy},timeout=5)
                if r.status_code == "200":
                    print(host+"Valid Proxy")
            if result3 ==0:
                print(host+" | 3128 OPEN |")
                proxy = host+":"+3128

                r = requests.get("http://httpbin.org/ip" , proxy={http:proxy,https:proxy},timeout=5)
                if r.status_code == "200":
                    print(host+"Valid Proxy")

            if result4 == 0:
                print(host+" | RDP PORT OPEN")
                xd = open("RDP 3089 PORT OPEN.txt","a+")
                xd.writelines(host+"\n")
                xd.close()

            if result5 == 0 or result6 == 0 or result7==0 or result8==0:
                print(host+" cpanel found")
                sd = open("cpanels.txt","a+")
                sd.writelines(host+"\n")
                sd.close()

        except:pass
xpsN = []

with concurrent.futures.ThreadPoolExecutor(max_workers=700) as executor:

    output = [executor.submit(xx , i) for i in range(10000)]
    for f in concurrent.futures.as_completed(output):
        pass

                

            
