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
