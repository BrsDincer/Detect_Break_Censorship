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
