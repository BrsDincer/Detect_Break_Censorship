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
