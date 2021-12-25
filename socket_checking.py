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
