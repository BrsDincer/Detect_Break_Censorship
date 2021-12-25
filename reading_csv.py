def reading_csv_att(target_doc=str): # GLOBAL reading_doc,https_list,http_list,main_body_url
    try:
        global reading_doc,https_list,http_list,main_body_url
        https_list = []
        http_list = []
        main_body_url = []
        reading_doc = pd.read_csv(target_doc)
        for x_att_url in reading_doc["url"]:
            get_new_url = x_att_url.replace("www.","")
            if "https://" in get_new_url:
                split_att(get_new_url)
                https_list.append(new_main_url)
                main_body_url.append(split_list[2])
            elif "http://" in get_new_url:
                split_att(get_new_url)
                http_list.append(new_main_url)
                main_body_url.append(split_list[2])
            else:
                pass
    except:
        print("[X] \033[1;31m%s\x1b[0m" % ("CHECK YOUR FILE AND TRY AGAIN"))
        pass
