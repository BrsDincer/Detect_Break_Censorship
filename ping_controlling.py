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
