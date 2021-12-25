def read_file_doc(file_name=str): # GLOBAL x_file
    try:
        global x_file
        with open(file_name,"r") as file_tar:
            x_file = []
            for line_x in file_tar:
                try:
                    ext_tar = line_x.strip()
                    x_file.append(ext_tar)
                except:
                    pass
    except:
        print("[X] \033[1;31m%s\x1b[0m" % ("CHECK YOUR FILE AND TRY AGAIN"))
        pass
