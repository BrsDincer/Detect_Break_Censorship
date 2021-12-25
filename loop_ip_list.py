def loop_ip_list(target_list=list):
    try:
        global ip_res_list,dom_res_list
        ip_res_list=[]
        dom_res_list=[]
        for x_url in target_list:
            find_ipv4(x_url,ip_res_list,dom_res_list)
    except:
        pass
