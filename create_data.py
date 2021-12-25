def create_data(target_att_one,target_att_two): # GLOBAL main_data
    try:    
        global main_data
        first_series = pd.Series(target_att_one,name="DOMAIN")
        second_series = pd.Series(target_att_two,name="IP")
        main_data = pd.concat([first_series,second_series],axis=1)
    except Exception as err:
        print(str(err))
        print("[X] \033[1;31m%s\x1b[0m" % ("SOMETHING IS WRONG"))
        pass
