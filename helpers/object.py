import requests
import json
import time
from pyhpeimc.plat.vlanm import get_dev_vlans, get_device_access_interfaces, get_trunk_interfaces
from pyhpeimc.plat.device import get_dev_run_config, get_dev_start_config, get_dev_interface


HEADERS = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Accept-encoding': 'application/json'}




def get_all_devices(auth, url, headers=HEADERS):
    '''
    Function takes no inputs and returns list of dictionaries of all devices

    :param auth: requests auth object #usualy auth.creds from auth pyhpeimc.auth.class

    :param url: base url of IMC RS interface #usualy auth.url from pyhpeimc.auth.authclass

    :return: list of dictionaries where each element represents one operator

    :rtype: list

    >>> from pyhpeimc.auth import *

    >>> from pyhpeimc.plat.operator import *

    >>> auth = IMCAuth("http://", "10.101.0.203", "8080", "admin", "admin")

    >>> device_list = get all_devices(auth.creds, auth.url)

    >>> assert type(device_list) is list

    >>> assert 'name' in device_last[0]
    '''

    get_device_url = '/imcrs/plat/res/device?resPrivilegeFilter=false&start=0&size=100&orderBy=id&desc=false&total=false&exact=false'
    f_url = url + get_device_url
    try:
        r = requests.get(f_url, auth=auth, headers=headers)
        plat_dev_list = json.loads(r.text)['device']
        if type(plat_dev_list) is dict:
            dev_list = []
            dev_list.append(plat_dev_list)
            return dev_list
        return plat_dev_list
    except requests.exceptions.RequestException as e:
        print("Error:\n" + str(e) + ' get_all_devices: An Error has occured')
        return "Error:\n" + str(e) + ' get_all_devices: An Error has occured'



class IMCDev:

    def __init__(self, device, auth, url):

        self.ip = device['ip']
        self.description = device['sysDescription']
        self.location = device['location']
        self.contact = device['contact']
        self.type = device['typeName']
        self.name = device['sysName']
        self.status = device['statusDesc']
        self.devid = device['id']


#        self.vlans = get_dev_vlans(self.devid, auth, url)



        self.interfacelist = get_dev_interface(self.devid, auth, url)



#        self.accessinterfaces = get_device_access_interfaces(self.devid, auth, url)
#        self.numinterface = len(self.interfacelist)


#        self.trunkinterfaces = get_trunk_interfaces(self.devid, auth, url)


#        start_time = time.time()
#        self.runconfig = get_dev_run_config(self.devid, auth, url)
#        print("---Get running config: %s seconds---" % (time.time() - start_time))

#        start_time = time.time()
#        self.startconfig = get_dev_start_config(self.devid, auth, url)
#        print("---Get startup config: %s seconds---" % (time.time() - start_time))

