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
