import time,socket,os,json,requests,random
from bs4 import BeautifulSoup
from optparse import OptionParser as OPTp


def split_att(target_params=str): # GLOBAL new_main_url,split_list
    try:    
        global new_main_url,split_list
        split_list = target_params.split("/")
        new_main_url = split_list[0]+"//"+split_list[2]
    except:
        print("[X] \033[1;31m%s\x1b[0m" % ("SOMETHING IS WRONG"))
        pass


# def reading_csv_att(target_doc=str): # GLOBAL reading_doc,https_list,http_list,main_body_url
#     try:
#         global reading_doc,https_list,http_list,main_body_url
#         https_list = []
#         http_list = []
#         main_body_url = []
#         reading_doc = pd.read_csv(target_doc)
#         for x_att_url in reading_doc["url"]:
#             get_new_url = x_att_url.replace("www.","")
#             if "https://" in get_new_url:
#                 split_att(get_new_url)
#                 https_list.append(new_main_url)
#                 main_body_url.append(split_list[2])
#             elif "http://" in get_new_url:
#                 split_att(get_new_url)
#                 http_list.append(new_main_url)
#                 main_body_url.append(split_list[2])
#             else:
#                 pass
#     except:
#         print("[X] \033[1;31m%s\x1b[0m" % ("CHECK YOUR FILE AND TRY AGAIN"))
#         pass

def get_ip_and_site(target_site=str): # GLOBAL --> target_ip_from_url,new_url
    try:
        global target_ip_from_url,new_url
        if "https://" in target_site or "http://" in target_site  or "www." in target_site or target_site.endswith("/") == True:
            new_url = target_site.replace("https://","").replace("http://","").replace("/","").replace("www.","")
            target_ip_from_url = socket.gethostbyname(new_url)
        else:
            new_url = target_site
            target_ip_from_url = socket.gethostbyname(new_url)
    except:
        print("[X] \033[1;31m%s\x1b[0m" % ("CHECK YOUR INTERNET CONNECTION AND TRY AGAIN"))
        pass


def find_ipv4(target_url=str,ip_list=list,dom_list=list): # GLOBAL ip_res
    try:
        global ip_res
        print(target_url)
        ip_res = socket.gethostbyname(target_url)
        dom_list.append(target_url)
        ip_list.append(ip_res)
    except:
        print("[!] \033[1;33m%s\x1b[0m" % ("NOT ADDING - CONNECTION DIED"))
        pass
    
def loop_ip_list(target_list=list):
    try:
        global ip_res_list,dom_res_list
        ip_res_list=[]
        dom_res_list=[]
        for x_url in target_list:
            find_ipv4(x_url,ip_res_list,dom_res_list)
    except:
        pass
        

# def create_data(target_att_one,target_att_two): # GLOBAL main_data
#     try:    
#         global main_data
#         first_series = pd.Series(target_att_one,name="DOMAIN")
#         second_series = pd.Series(target_att_two,name="IP")
#         main_data = pd.concat([first_series,second_series],axis=1)
#     except Exception as err:
#         print(str(err))
#         print("[X] \033[1;31m%s\x1b[0m" % ("SOMETHING IS WRONG"))
#         pass
    

def connect_res(target_ip=str,target_port=int):
    try:
        new_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        res_connection = new_socket.connect_ex((target_ip,target_port))
        new_socket.settimeout(15)
        if res_connection == 0:
            print("[+] %s --> \033[1;32m%s\x1b[0m : PORT %s" % (target_ip,"OPEN PORT",str(target_port)))
            new_socket.close()
        else:
            print("[!] %s --> \033[1;33m%s\x1b[0m : PORT %s" % (target_ip,"NO ACCESS",str(target_port)))
            new_socket.close()
            pass
    except:
        print("[X] \033[1;31m%s\x1b[0m" % ("TIME - OUT"))
        pass


def port_check(target_url=str):
    try:
        get_ip_and_site(target_url)
        print("[>] TARGET IP: \033[1;32m%s\x1b[0m" % (target_ip_from_url))
        print("[>] TARGET HOST: \033[1;32m%s\x1b[0m" % (new_url))
        print("[>] \033[1;32m%s\x1b[0m" % ("PLEASE WAIT"))
        print("\n")
        Port_List = [7,11,13,20,21,22,23,25,37,42,
                     43,53,67,68,69,77,79,80,95,101,
                     113,119,123,137,138,139,160,165,
                     170,175,180,200,210,223,443]
        for x_port in Port_List:
            try:
                connect_res(target_ip_from_url,x_port)
            except:
                print("[X] \033[1;31m%s\x1b[0m" % ("TIME - OUT"))
                pass
    except:
        print("[X] \033[1;31m%s\x1b[0m" % ("CHECK YOUR CONNECTION AND TRY AGAIN"))
        pass


# def read_file_doc(file_name=str): # GLOBAL x_file
#     try:
#         global x_file
#         with open(file_name,"r") as file_tar:
#             x_file = []
#             for line_x in file_tar:
#                 try:
#                     ext_tar = line_x.strip()
#                     x_file.append(ext_tar)
#                 except:
#                     pass
#     except:
#         print("[X] \033[1;31m%s\x1b[0m" % ("CHECK YOUR FILE AND TRY AGAIN"))
#         pass
    
    
def user_agent_get(): # GLOBAL all_list_agent
    try:
        global all_list_agent
        Json_Tar="user_agent_all.json"
        f_op = open(Json_Tar)
        j_op = json.loads(f_op.read())
        all_list_agent = []
        for x_value in j_op["user_agents"]:
            for ix_values in j_op["user_agents"][x_value]:
                for ixl_values in j_op["user_agents"][x_value][ix_values]:
                    for ixlp_values in j_op["user_agents"][x_value][ix_values][ixl_values]:
                        all_list_agent.append(ixlp_values)
    except:
        print("[X] \033[1;31m%s\x1b[0m" % ("CHECK YOUR FILE DIRECTORY AND TRY AGAIN"))
        pass


def get_proxies(): # GLOBAL IP_L,PR_L
    try:
        global IP_L,PR_L
        Rand_Url_Main = "https://free-proxy-list.net/"
        user_agent_get()
        user_agent_all = {"User-Agent":f"{random.choice(all_list_agent)}"}
        Soup_Main = BeautifulSoup(requests.get(Rand_Url_Main,headers=user_agent_all).content, "html.parser")
        IP_L = []
        PR_L = []
        i_count_spoof = 0
        for tab_all in Soup_Main.find("table",class_="table table-striped table-bordered"):
            tr_all = tab_all.find_all("tr")
            for x_tr in tr_all:
                td_all = x_tr.find_all("td")
                for x_td in td_all:
                    i_count_spoof += 1
                    if i_count_spoof == 1:
                        IP_M = x_td.text
                        IP_L.append(str(IP_M))
                    elif i_count_spoof == 2:
                        PR_M = x_td.text
                        PR_L.append(str(PR_M))
                i_count_spoof = 0
    except:
        print("[X] \033[1;31m%s\x1b[0m" % ("CHECK YOUR CONNECTION AND TRY AGAIN"))
        pass


def method_controlling(tar_url=str):
    print("\n")
    print("[>] CHECKING FOR \033[1;32m%s\x1b[0m" % (tar_url))
    met_all_list = ["GET","POST","PUT",
                 "CONNECT","COPY","PATCH",
                 "TRACE","HEAD","UPDATE",
                 "LABEL","OPTIONS","MOVE",
                 "SEARCH","ARBITRARY","CHECKOUT",
                 "UNCHECKOUT","UNLOCK","MERGE",
                 "BASELINE-CONTROL","ACL"]
    try:
        if "https://" in tar_url or "http://" in tar_url or "www." in tar_url:
            tar_url = tar_url.replace("https://","").replace("http://","").replace("www.","")
            print("[>] TARGET \033[1;32m%s\x1b[0m" % (tar_url))
            print("[>] \033[1;32m%s\x1b[0m" % ("PLEASE WAIT"))
            print("\n")
            for x_method in met_all_list:
                command_curl = "curl -sIX %s %s -m %s" % (x_method,tar_url,30)
                openning_func = os.popen(command_curl)
                try:
                    status_reading = openning_func.read().split()[1]
                    if int(status_reading) == 200:
                        print("[+] %s --> \033[1;32m%s\x1b[0m OK" % (x_method,status_reading))
                    else:
                        print("[?] %s --> \033[1;33m%s\x1b[0m NOT ACTIVE" % (x_method,status_reading))
                except:
                    print("[!] \033[1;31m%s\x1b[0m" % ("TIME OUT - IT MAY BE BLOCKED"))
                    pass
        else:
            print("[>] TARGET \033[1;32m%s\x1b[0m" % (tar_url))
            print("[>] \033[1;32m%s\x1b[0m" % ("PLEASE WAIT"))
            print("\n")
            for x_method in met_all_list:
                command_curl = "curl -sIX %s %s -m %s" % (x_method,tar_url,30)
                openning_func = os.popen(command_curl)
                try:
                    status_reading = openning_func.read().split()[1]
                    if int(status_reading) == 200:
                        print("[+] %s --> \033[1;32m%s\x1b[0m OK" % (x_method,status_reading))
                    else:
                        print("[?] %s --> \033[1;33m%s\x1b[0m NOT ACTIVE" % (x_method,status_reading))
                except:
                    print("[!] \033[1;31m%s\x1b[0m" % ("TIME OUT - IT MAY BE BLOCKED"))
                    pass
    except:
        print("[X] \033[1;31m%s\x1b[0m" % ("CHECK YOUR CONNECTION AND TRY AGAIN"))
        pass


def ping_controlling(tar_url=str):
    print("\n")
    print("[>] CHECKING FOR \033[1;32m%s\x1b[0m" % (tar_url))
    try:
        if "https://" in tar_url or "http://" in tar_url or "www." in tar_url:
            tar_url = tar_url.replace("https://","").replace("http://","").replace("www.","")
            print("[>] TARGET \033[1;32m%s\x1b[0m" % (tar_url))
            print("[>] \033[1;32m%s\x1b[0m" % ("PLEASE WAIT"))
            print("\n")
            tar_url = tar_url.replace("https://","").replace("http://","").replace("www.","")
            command_ping = "ping %s" % (tar_url)
            command_nt = os.popen(command_ping)
            for x_command_line in command_nt.readlines():
                if x_command_line.count("TTL"):
                    print(x_command_line)
                else:
                    print(x_command_line)
                    pass
            print("[i] %s --> \033[1;33m%s\x1b[0m" % (tar_url,"CHECK RESPONSE"))
        else:
            print("[>] TARGET \033[1;32m%s\x1b[0m" % (tar_url))
            print("[>] \033[1;32m%s\x1b[0m" % ("PLEASE WAIT"))
            print("\n")
            command_ping = "ping %s" % (tar_url)
            command_nt = os.popen(command_ping)
            for x_command_line in command_nt.readlines():
                if x_command_line.count("TTL"):
                    print(x_command_line)
                else:
                    print(x_command_line)
                    pass
                print("[i] %s --> \033[1;33m%s\x1b[0m" % (tar_url,"CHECK RESPONSE"))
    except:
        print("[X] \033[1;31m%s\x1b[0m" % ("CHECK YOUR CONNECTION AND TRY AGAIN"))
        pass
            


def curl_get_prox(tar_url=str,prox_dom=str): # GLOBAL status_reading
    try:
        global status_reading
        command_prob = os.popen("curl -sk --proxy %s %s -m %s" % (prox_dom, tar_url, 30))
        status_reading = command_prob.read()
    except:
        pass


def curl_get_norm(tar_url=str): # GLOBAL status_reading
    try:
        global status_reading
        command_prob = os.popen("curl -k -s %s -m %s" % (tar_url,30))
        status_reading = command_prob.read()
    except:
        pass


def socket_checking(target_site=str,target_port=80):
    try:
        get_ip_and_site(target_site)
        print("\n")
        print("[>] SEARCHING FOR \033[1;32m%s\x1b[0m" % (new_url))
        print("[>] IP: \033[1;32m%s\x1b[0m" % (target_ip_from_url))
        print("\n")
        print("[i] \033[1;33m%s\x1b[0m" % ("FOR HTTP"))
        print("[>] PORT: \033[1;32m%s\x1b[0m" % (target_port))
        print("\n")
        time.sleep(2.2)
        new_url_www = "www."+new_url
        send_packet_http = "GET / HTTP/1.1\r\nHost: %s\r\n\r\n" % (new_url_www)
        sc_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sc_socket.connect((target_ip_from_url,target_port))
        sc_socket.settimeout(35)
        if sc_socket.sendto(send_packet_http.encode(),(target_ip_from_url,target_port)):
            print("[i] \033[1;33m%s\x1b[0m" % ("MESSAGE FORWARDED"))
            print("\n")
            time.sleep(3.2)
            recv_mess = sc_socket.recv(1024)
            print(recv_mess.decode())
            sc_socket.shutdown(1)
            print("[i] \033[1;33m%s\x1b[0m" % ("CHECK RESPONSE"))
        else:
            sc_socket.shutdown(1)
        print("\n")
        print("[i] \033[1;33m%s\x1b[0m" % ("FOR HTTPS"))
        print("[>] PORT: \033[1;32m%s\x1b[0m" % (str(443)))
        print("\n")
        time.sleep(2.2)
        send_packet_https = "GET / HTTPS/1.1\r\nHost: %s\r\n\r\n" % (new_url_www)
        sc_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sc_socket.connect((target_ip_from_url,443))
        sc_socket.settimeout(35)
        if sc_socket.sendto(send_packet_https.encode(),(target_ip_from_url,443)):
            print("[i] \033[1;33m%s\x1b[0m" % ("MESSAGE FORWARDED"))
            print("\n")
            time.sleep(3.2)
            recv_mess = sc_socket.recv(1024)
            print(recv_mess.decode())
            sc_socket.shutdown(1)
            print("[i] \033[1;33m%s\x1b[0m" % ("CHECK RESPONSE"))
            print("\n")
        else:
            sc_socket.shutdown(1)
    except:
        print("[X] \033[1;31m%s\x1b[0m" % ("TIME-OUT / MAY BE BLOCKED IN YOUR COUNTRY"))
        pass
    

def requests_with_proxy(target_site=str):
    print("\n")
    print("[>] SEARCHING FOR \033[1;32m%s\x1b[0m" % (target_site))
    print("\n")
    try:
        user_agent_get()
        get_proxies()
        define_agent = {"User-Agent":str(random.choice(all_list_agent))}
        if "https://" in target_site or "http://" in target_site:
            print("[>] TARGET \033[1;32m%s\x1b[0m" % (target_site))
            print("[>] \033[1;32m%s\x1b[0m" % ("PLEASE WAIT"))
            print("\n")
            x_count = 0
            if x_count == 0:
                for x_ips,x_prox in zip(IP_L,PR_L):
                    try:
                        define_proxy = {"https":f"https://{str(x_ips)}:{x_prox}",
                                        "http":f"http://{str(x_ips)}:{x_prox}"}
                        req_s = requests.Session()
                        req_res = req_s.get(target_site,headers=define_agent,proxies=define_proxy,timeout=30)
                        if req_res.status_code == 200:
                            print("\n")
                            print("GOT RESPONSE AS \033[1;32m%s\x1b[0m" % (req_res.status_code))
                            print("TRUE-CONNECTION PROXY \033[1;32m%s\x1b[0m" % (f"{str(x_ips)}:{x_prox}"))
                            print("\n")
                            file_save = open(f"{random.randint(10, 100)}.html","w",errors="replace")
                            file_save.write(req_res.text)
                            file_save.close()
                            req_s.close()
                            x_count += 1
                            print("\n")
                            print("[+] \033[1;32m%s\x1b[0m" % ("FOUND, CHECK YOUR FOLDER"))
                            print("\n")
                            break
                        else:
                            req_s.close()
                            pass
                    except:
                        print("[?] \033[1;33m%s\x1b[0m" % ("SEARCHING"))
                        pass
        else:
            new_url = "http://"+target_site
            print("[>] TARGET \033[1;32m%s\x1b[0m" % (new_url))
            print("[>] \033[1;32m%s\x1b[0m" % ("PLEASE WAIT"))
            print("\n")
            x_count = 0
            if x_count == 0:
                for x_ips,x_prox in zip(IP_L,PR_L):
                    try:
                        define_proxy = {"https":f"https://{str(x_ips)}:{x_prox}",
                                        "http":f"http://{str(x_ips)}:{x_prox}"}
                        req_s = requests.Session()
                        req_res = req_s.get(new_url,headers=define_agent,proxies=define_proxy,timeout=30)
                        if req_res.status_code == 200:
                            print("\n")
                            print("GOT RESPONSE AS \033[1;32m%s\x1b[0m" % (req_res.status_code))
                            print("TRUE-CONNECTION PROXY \033[1;32m%s\x1b[0m" % (f"{str(x_ips)}:{x_prox}"))
                            print("\n")
                            file_save = open(f"{random.randint(10, 100)}.html","w",errors="replace")
                            file_save.write(req_res.text)
                            file_save.close()
                            req_s.close()
                            x_count += 1
                            print("\n")
                            print("[+] \033[1;32m%s\x1b[0m" % ("FOUND, CHECK YOUR FOLDER"))
                            print("\n")
                            break
                        else:
                            req_s.close()
                            pass
                    except:
                        print("[?] \033[1;33m%s\x1b[0m" % ("SEARCHING"))
                        pass
    except:
        print("[X] \033[1;31m%s\x1b[0m" % ("CHECK YOUR CONNECTION AND TRY AGAIN"))
        pass
            

def curl_with_proxy(target_site=str):
    print("\n")
    print("[>] SEARCHING FOR \033[1;32m%s\x1b[0m" % (target_site))
    try:
        user_agent_get()
        get_proxies()
        define_agent = {"User-Agent":str(random.choice(all_list_agent))}
        x_count = 0
        if x_count == 0:
            if "https://" in target_site or "http://" in target_site:
                print("[>] TARGET \033[1;32m%s\x1b[0m" % (target_site))
                print("\n")
                for x_ips,x_prox in zip(IP_L,PR_L):
                    try:
                        define_proxy = {"https":f"https://{str(x_ips)}:{x_prox}",
                                        "http":f"http://{str(x_ips)}:{x_prox}"}
                        req_s = requests.Session()
                        req_res = req_s.get(target_site,headers=define_agent,proxies=define_proxy,timeout=30)
                        if req_res.status_code == 200:
                            print("\n")
                            print("GOT RESPONSE AS \033[1;32m%s\x1b[0m" % (req_res.status_code))
                            print("TRUE-CONNECTION PROXY \033[1;32m%s\x1b[0m" % (f"{str(x_ips)}:{x_prox}"))
                            print("\n")
                            new_url = target_site.replace("https://","").replace("http://","").replace("www.","")
                            curl_get_prox(new_url,str(define_proxy['http']))
                            if "301" in status_reading:
                                print("\n")
                                print("[+] \033[1;32m%s\x1b[0m" % ("CODE 301 FOUND"))
                                print("\n")
                                print(status_reading)
                                req_s.close()
                                pass
                            elif status_reading != None and len(status_reading) != 0\
                                and "301" not in status_reading\
                                    and "Maximum number of open connections reached. " not in status_reading:
                                file_save = open("main.html","w",errors="replace")
                                file_save.write(status_reading)
                                file_save.close()
                                req_s.close()
                                x_count += 1
                                print("\n")
                                print("[+] \033[1;32m%s\x1b[0m" % ("FOUND, CHECK YOUR FOLDER"))
                                print("\n")
                                break
                            else:
                                req_s.close()
                                pass
                        else:
                            req_s.close()
                            pass
                    except:
                        print("[?] \033[1;33m%s\x1b[0m" % ("SEARCHING"))
                        pass
            else:
                target_site = "http://"+target_site
                print("[>] TARGET \033[1;32m%s\x1b[0m" % (target_site))
                print("\n")
                for x_ips,x_prox in zip(IP_L,PR_L):
                    try:
                        define_proxy = {"https":f"https://{str(x_ips)}:{x_prox}",
                                        "http":f"http://{str(x_ips)}:{x_prox}"}
                        req_s = requests.Session()
                        req_res = req_s.get(target_site,headers=define_agent,proxies=define_proxy,timeout=30)
                        if req_res.status_code == 200:
                            print("\n")
                            print("GOT RESPONSE AS \033[1;32m%s\x1b[0m" % (req_res.status_code))
                            print("TRUE-CONNECTION PROXY \033[1;32m%s\x1b[0m" % (f"{str(x_ips)}:{x_prox}"))
                            print("\n")
                            new_url = target_site.replace("https://","").replace("http://","").replace("www.","")
                            curl_get_prox(new_url,str(define_proxy['http']))
                            if "301" in status_reading:
                                print("\n")
                                print("[+] \033[1;32m%s\x1b[0m" % ("CODE 301 FOUND"))
                                print("\n")
                                print(status_reading)
                                req_s.close()
                                pass
                            elif status_reading != None and len(status_reading) != 0\
                                and "301" not in status_reading\
                                    and "Maximum number of open connections reached. " not in status_reading:
                                file_save = open("main.html","w",errors="replace")
                                file_save.write(status_reading)
                                file_save.close()
                                req_s.close()
                                x_count += 1
                                print("\n")
                                print("[+] \033[1;32m%s\x1b[0m" % ("FOUND, CHECK YOUR FOLDER"))
                                print("\n")
                                break
                            else:
                                req_s.close()
                                pass
                        else:
                            req_s.close()
                            pass
                    except:
                        print("[?] \033[1;33m%s\x1b[0m" % ("SEARCHING"))
                        pass
    except:
        print("[X] \033[1;31m%s\x1b[0m" % ("CHECK YOUR CONNECTION AND TRY AGAIN"))
        pass



def requests_check(target_site=str):
    print("\n")
    print("[>] CHECKING FOR \033[1;32m%s\x1b[0m" % (target_site))
    try:
        user_agent_get()
        get_proxies()
        define_agent = {"User-Agent":str(random.choice(all_list_agent))}
        if "http://" in target_site or "https://" in target_site:
            print("[>] TARGET \033[1;32m%s\x1b[0m" % (target_site))
            print("[>] \033[1;32m%s\x1b[0m" % ("PLEASE WAIT"))
            print("\n")
            try:
                req_s = requests.Session()
                req_res = req_s.get(target_site,headers=define_agent,timeout=30)
                if req_res.status_code == 200:
                    print(req_res.text)
                    print("\n")
                    print("[?] \033[1;33m%s\x1b[0m --> STATUS CODE: %s" % ("CHECK YOUR RESULT",req_res.status_code))
                    print("\n")
                    req_s.close()
                else:
                    print(req_res.text)
                    print("\n")
                    print("[?] \033[1;33m%s\x1b[0m --> STATUS CODE: %s" % ("CHECK YOUR RESULT",req_res.status_code))
                    print("\n")
                    req_s.close()
                    pass
            except:
                print("[X] \033[1;31m%s\x1b[0m" % ("NOT CONNECTED, MAY BE BLOCKED IN YOUR COUNTRY"))
                pass
        else:
            target_site = "http://"+target_site
            print("[>] TARGET \033[1;32m%s\x1b[0m" % (target_site))
            print("\n")
            try:
                req_s = requests.Session()
                req_res = req_s.get(target_site,headers=define_agent,timeout=30)
                if req_res.status_code == 200:
                    print(req_res.text)
                    print("\n")
                    print("[?] \033[1;33m%s\x1b[0m --> STATUS CODE: %s" % ("CHECK YOUR RESULT",req_res.status_code))
                    print("\n")
                    req_s.close()
                else:
                    print(req_res.text)
                    print("\n")
                    print("[?] \033[1;33m%s\x1b[0m --> STATUS CODE: %s" % ("CHECK YOUR RESULT",req_res.status_code))
                    print("\n")
                    req_s.close()
                    pass
            except:
                print("[X] \033[1;31m%s\x1b[0m" % ("NOT CONNECTED, MAY BE BLOCKED IN YOUR COUNTRY"))
                pass
    except:
        print("[X] \033[1;31m%s\x1b[0m" % ("CHECK YOUR CONNECTION AND TRY AGAIN"))
        pass


def curl_check(target_site=str):
    print("\n")
    print("[>] CHECKING FOR \033[1;32m%s\x1b[0m" % (target_site))
    target_site = target_site.replace("https://","").replace("http://","").replace("www.","")
    print("[>] TARGET \033[1;32m%s\x1b[0m" % (target_site))
    print("[>] \033[1;32m%s\x1b[0m" % ("PLEASE WAIT"))
    print("\n")
    try:
        curl_get_norm(target_site)
        print(status_reading)
        print("\n")
        print("[?] \033[1;33m%s\x1b[0m" % ("CHECK YOUR RESULT"))
        print("\n")
    except:
        print("[X] \033[1;31m%s\x1b[0m" % ("NOT CONNECTED, MAY BE BLOCKED IN YOUR COUNTRY"))
        pass


def show_info():
    try:
        print("""
              
              
         IIIIIIIIIIIIIIIIIIII        PPPPPPPPPPPPPPPPP        VVVVVVVV           VVVVVVVV
         I::::::::II::::::::I        P::::::::::::::::P       V::::::V           V::::::V
         I::::::::II::::::::I        P::::::PPPPPP:::::P      V::::::V           V::::::V
         II::::::IIII::::::II        PP:::::P     P:::::P     V::::::V           V::::::V
           I::::I    I::::I            P::::P     P:::::P      V:::::V           V:::::V 
           I::::I    I::::I            P::::P     P:::::P       V:::::V         V:::::V  
           I::::I    I::::I            P::::PPPPPP:::::P         V:::::V       V:::::V   
           I::::I    I::::I            P:::::::::::::PP           V:::::V     V:::::V    
           I::::I    I::::I            P::::PPPPPPPPP              V:::::V   V:::::V     
           I::::I    I::::I            P::::P                       V:::::V V:::::V      
           I::::I    I::::I            P::::P                        V:::::V:::::V       
           I::::I    I::::I            P::::P                         V:::::::::V        
         II::::::IIII::::::II        PP::::::PP                        V:::::::V         
         I::::::::II::::::::I ...... P::::::::P                         V:::::V          
         I01000110II00110100I .::::. P01000110P                          V:::V     --> CREATED FOR FREE NET 
         IIIIIIIIIIIIIIIIIIII ...... PPPPPPPPPP                           VVV      --> open-source culture
              
             ############################################################################################################
             ############################################################################################################
             -------------------------------------------------------------------------------------
             
             py IIPV_CC.py     -<TYPE> https://example.com      [or] py IIPV_CC.py     --<TYPE>  https://example.com 
             python IIPV_CC.py -<TYPE> https://example.com      [or] python IIPV_CC.py --<TYPE>  https://example.com
             -------------------------------------------------------------------------------------
             ############################################################################################################
             ############################################################################################################
              
              -------------------------------------------------------------------------------------
              ####   -H    --help             how to use   ####
              
              [ -c ]  --control          -> CONTROL THE SITE
              [ -a ]  --access           -> GET ACCESS TO SITE
              
              -------------------------------------------------------------------------------------
              
              
              <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
              -------------------------------------------------------------------------------------
              [NOTED - IMPORTANT]
              + TRY TO DETECT FAKE SERVERS.
              + ASSIGNED SCAM SERVERS ARE SIMILAR ON ALL CENSORED SITES.
              + FAKE SERVERS HAVE FIXED PORTS.
              -------------------------------------------------------------------------------------
              >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


              """)
    except:
        pass

def running_process():
    try:
        QT_F = OPTp(add_help_option=False,epilog="ANTI-CENSORSHIP TOOL")
        QT_F.add_option("-H",
                        "--help",
                        help="HOW TO USE",
                        action="store_true",
                        dest="x_help")
        QT_F.add_option("-c",
                        "--control",
                        help="CONTROL THE SITE",
                        type="string",
                        dest="x_control")
        QT_F.add_option("-a",
                        "--access",
                        help="GET ACCESS TO SITE",
                        type="string",
                        dest="x_access")
        
        op_qt,op_arg = QT_F.parse_args()
        if op_qt.x_access:
            site_target = str(op_qt.x_access).replace(" ","")
            print("\n")
            print("[>>>] \033[1;32m%s\x1b[0m" % ("STARTING THE PROCESS"))
            print("\n")
            time.sleep(2.2)
            print("[STEP] \033[1;32m%s\x1b[0m" % ("WAIT FOR REQUESTS PROCESS"))
            print("\n")
            time.sleep(1.2)
            requests_with_proxy(site_target)
            print("\n")
            print("[>] \033[1;32m%s\x1b[0m" % ("PROCESS OF REQUESTS COMPLETED"))
            print("\n")
            time.sleep(1.2)
            print("[STEP] \033[1;32m%s\x1b[0m" % ("WAIT FOR CURL PROCESS"))
            print("\n")
            time.sleep(1.2)
            curl_with_proxy(site_target)
            print("\n")
            print("[>] \033[1;32m%s\x1b[0m" % ("PROCESS OF CURL COMPLETED"))
            print("\n")
            time.sleep(1.2)
        elif op_qt.x_control:
            site_target = str(op_qt.x_control).replace(" ","")
            print("\n")
            print("[>>>] \033[1;32m%s\x1b[0m" % ("STARTING THE PROCESS"))
            print("\n")
            time.sleep(2.2)
            print("[STEP] \033[1;32m%s\x1b[0m" % ("WAIT FOR REQUESTS CONTROLLING"))
            print("\n")
            time.sleep(1.2)
            requests_check(site_target)
            print("\n")
            print("[>] \033[1;32m%s\x1b[0m" % ("REQUESTS COMPLETED"))
            print("\n")
            time.sleep(1.2)
            print("[STEP] \033[1;32m%s\x1b[0m" % ("WAIT FOR CURL CONTROLLING"))
            print("\n")
            time.sleep(1.2)
            curl_check(site_target)
            print("\n")
            print("[>] \033[1;32m%s\x1b[0m" % ("CURL COMPLETED"))
            print("\n")
            time.sleep(1.2)
            print("[STEP] \033[1;32m%s\x1b[0m" % ("WAIT FOR PORT CONTROLLING"))
            print("\n")
            time.sleep(1.2)
            port_check(site_target)
            print("\n")
            print("[>] \033[1;32m%s\x1b[0m" % ("PORT CONTROLLING COMPLETED"))
            print("\n")
            time.sleep(1.2)
            print("[STEP] \033[1;32m%s\x1b[0m" % ("WAIT FOR PING CONTROLLING"))
            print("\n")
            time.sleep(1.2)
            ping_controlling(site_target)
            print("\n")
            print("[>] \033[1;32m%s\x1b[0m" % ("PING CONTROLLING COMPLETED"))
            print("\n")
            time.sleep(1.2)
            print("[STEP] \033[1;32m%s\x1b[0m" % ("WAIT FOR SOCKET CONTROLLING"))
            print("\n")
            time.sleep(1.2)
            socket_checking(site_target)
            print("\n")
            print("[>] \033[1;32m%s\x1b[0m" % ("SOCKET CONTROLLING COMPLETED"))
            print("\n")
            time.sleep(1.2)
        else:
            show_info()
            pass
    except:
        print("[X] \033[1;31m%s\x1b[0m" % ("SOMETHING IS WRONG"))
        pass
        
        
if __name__ == "__main__":
    try:
        running_process()
    except:
        show_info()
        pass
