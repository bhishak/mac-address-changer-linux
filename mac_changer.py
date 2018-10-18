#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its mac")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac Adress")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please Specify an Interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please Specify a new mac, use --help for more info")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC adress for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_searches = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_searches:
        return mac_address_searches.group(0)
    else:
        print("[-] Sorry Could not Get MAC Address for given interface")
        print("[-] Exiting")
        exit()
        # return "00:00:00:00:00:00"



options =get_arguments()
init_mac=get_current_mac(options.interface)
change_mac(options.interface, options.new_mac)
curr_mac= get_current_mac(options.interface)
if(options.new_mac==curr_mac):
    print("[+] MAC Address is successfully changed to "+curr_mac)
else:
    print("[-] Error, Couldn't Change the MAC Address")