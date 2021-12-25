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
