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
