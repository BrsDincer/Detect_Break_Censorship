def split_att(target_params=str): # GLOBAL new_main_url,split_list
    try:    
        global new_main_url,split_list
        split_list = target_params.split("/")
        new_main_url = split_list[0]+"//"+split_list[2]
    except:
        print("[X] \033[1;31m%s\x1b[0m" % ("SOMETHING IS WRONG"))
        pass
