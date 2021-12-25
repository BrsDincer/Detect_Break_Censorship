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
