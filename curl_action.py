def curl_get_prox(tar_url=str,prox_dom=str): # GLOBAL status_reading
    try:
        global status_reading
        command_prob = os.popen("curl -sk --proxy %s %s -m %s" % (prox_dom, tar_url, 30))
        status_reading = command_prob.read()
    except:
        pass


def curl_get_norm(tar_url=str): # GLOBAL status_reading
    try:
        global status_reading
        command_prob = os.popen("curl -k -s %s -m %s" % (tar_url,30))
        status_reading = command_prob.read()
    except:
        pass
