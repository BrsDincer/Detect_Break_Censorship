def running_process():
    try:
        QT_F = OPTp(add_help_option=False,epilog="ANTI-CENSORSHIP TOOL")
        QT_F.add_option("-H",
                        "--help",
                        help="HOW TO USE",
                        action="store_true",
                        dest="x_help")
        QT_F.add_option("-c",
                        "--control",
                        help="CONTROL THE SITE",
                        type="string",
                        dest="x_control")
        QT_F.add_option("-a",
                        "--access",
                        help="GET ACCESS TO SITE",
                        type="string",
                        dest="x_access")
        
        op_qt,op_arg = QT_F.parse_args()
        if op_qt.x_access:
            site_target = str(op_qt.x_access).replace(" ","")
            print("\n")
            print("[>>>] \033[1;32m%s\x1b[0m" % ("STARTING THE PROCESS"))
            print("\n")
            time.sleep(2.2)
            print("[STEP] \033[1;32m%s\x1b[0m" % ("WAIT FOR REQUESTS PROCESS"))
            print("\n")
            time.sleep(1.2)
            requests_with_proxy(site_target)
            print("\n")
            print("[>] \033[1;32m%s\x1b[0m" % ("PROCESS OF REQUESTS COMPLETED"))
            print("\n")
            time.sleep(1.2)
            print("[STEP] \033[1;32m%s\x1b[0m" % ("WAIT FOR CURL PROCESS"))
            print("\n")
            time.sleep(1.2)
            curl_with_proxy(site_target)
            print("\n")
            print("[>] \033[1;32m%s\x1b[0m" % ("PROCESS OF CURL COMPLETED"))
            print("\n")
            time.sleep(1.2)
        elif op_qt.x_control:
            site_target = str(op_qt.x_control).replace(" ","")
            print("\n")
            print("[>>>] \033[1;32m%s\x1b[0m" % ("STARTING THE PROCESS"))
            print("\n")
            time.sleep(2.2)
            print("[STEP] \033[1;32m%s\x1b[0m" % ("WAIT FOR REQUESTS CONTROLLING"))
            print("\n")
            time.sleep(1.2)
            requests_check(site_target)
            print("\n")
            print("[>] \033[1;32m%s\x1b[0m" % ("REQUESTS COMPLETED"))
            print("\n")
            time.sleep(1.2)
            print("[STEP] \033[1;32m%s\x1b[0m" % ("WAIT FOR CURL CONTROLLING"))
            print("\n")
            time.sleep(1.2)
            curl_check(site_target)
            print("\n")
            print("[>] \033[1;32m%s\x1b[0m" % ("CURL COMPLETED"))
            print("\n")
            time.sleep(1.2)
            print("[STEP] \033[1;32m%s\x1b[0m" % ("WAIT FOR PORT CONTROLLING"))
            print("\n")
            time.sleep(1.2)
            port_check(site_target)
            print("\n")
            print("[>] \033[1;32m%s\x1b[0m" % ("PORT CONTROLLING COMPLETED"))
            print("\n")
            time.sleep(1.2)
            print("[STEP] \033[1;32m%s\x1b[0m" % ("WAIT FOR PING CONTROLLING"))
            print("\n")
            time.sleep(1.2)
            ping_controlling(site_target)
            print("\n")
            print("[>] \033[1;32m%s\x1b[0m" % ("PING CONTROLLING COMPLETED"))
            print("\n")
            time.sleep(1.2)
            print("[STEP] \033[1;32m%s\x1b[0m" % ("WAIT FOR SOCKET CONTROLLING"))
            print("\n")
            time.sleep(1.2)
            socket_checking(site_target)
            print("\n")
            print("[>] \033[1;32m%s\x1b[0m" % ("SOCKET CONTROLLING COMPLETED"))
            print("\n")
            time.sleep(1.2)
        else:
            show_info()
            pass
    except:
        print("[X] \033[1;31m%s\x1b[0m" % ("SOMETHING IS WRONG"))
        pass
        
        
if __name__ == "__main__":
    try:
        running_process()
    except:
        show_info()
        pass
