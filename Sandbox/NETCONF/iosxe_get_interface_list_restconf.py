import requests
import sys

requests.packages.urllib3.disable_warnings()

HOST = 'sandbox-iosxe-recomm-1.cisco.com'
PORT = '443'
USER = 'developer'
PASS = 'C1sco12345'

def get_configurd_interfaces():
    url = "https://{h}:{p}/restconf/data/ietf-interfaces:interfaces".format(h=HOST,p=PORT)
    header = {
        'Content-Type':'application/yang-data+json',
        'Accept':'application/yang-data+json'
    }
    response = requests.get(url, auth=(USER,PASS),headers=header, verify=False)
    return(response.text)

def main():
    interfaces = get_configurd_interfaces()
    print(interfaces)

if __name__ == "__main__":
    sys.exit(main())