#!/usr/bin/env python3
# author: jorge.gil

from pyhpeimc.objects import *
from helpers.auth import *
from helpers.alarms import *
from helpers.object import *
import sys, os
from time import sleep
import datetime

# variables

username = ""
password = ""
url = ""
port = ""

#Color Class
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'


# Function
def my_get_alarms(auth_stuff):
    """

    :type auth_stuff: object
    """
    alarms = get_realtime_alarm(auth_stuff.username, auth_stuff.creds, auth_stuff.url)

    count = 0

    for alarm in alarms:
        alarm_details = get_alarm_byId(alarm['id'], auth_stuff.creds, auth_stuff.url)
        if (alarm_details['deviceIp'] == '127.0.0.1'):
            continue
        else:
            count += 1
        print("Date: " + datetime.datetime.fromtimestamp(time.time()).strftime('%c'))
        print(bcolors.HEADER + '-----------------------------------' + bcolors.ENDC)
        print("Alarm Time: " + alarm_details['faultTimeDesc'])
        print("Alarm Level: " + alarm_details['alarmLevelDesc'] + " Alarm")
        print("Device Name: " + alarm_details['deviceName'])
        print("Device IP: " + alarm_details['deviceIp'])
        print("Alarm Description: " + alarm_details['alarmDesc'])



    if (count == 0):
        print("Date: " + datetime.datetime.fromtimestamp(time.time()).strftime('%c'))
        print("No Real Time Alarms Found!")
    else:
        print(bcolors.HEADER + '-----------------------------------' + bcolors.ENDC)
    sleep(60 * 1)

    os.system('cls')
    return;




#main Program
def main():


    os.system('cls')

    auth = IMCAuth("http://", url, port, username, password)
    try:
        while True:
            my_get_alarms(auth)
    except requests.exceptions.ConnectionError as e:
        print("Error connecting to server: " + url)
        sys.exit(0)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Program Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
