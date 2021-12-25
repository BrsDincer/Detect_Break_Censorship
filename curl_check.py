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
