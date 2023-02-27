from ncclient import manager
import sys
import xmltodict
import xml.dom.minidom

#from device_info import iosxe as device

device = {
    "address": "sandbox-iosxe-recomm-1.cisco.com",
    "netconf_port": 830,
    "restconf_port": 443,
    "ssh_port": 22,
    "username": "developer",
    "password": "C1sco12345"
}


netconf_filter = """
<filter>
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
<interface></interface>
</interfaces>
</filter>"""


print("Opening NETCONF Connection to {}".format(device["address"]))
with manager.connect(
    host = device["address"],
    port = device["netconf_port"],
    username = device["username"],
    password = device["password"],
    hostkey_verify = False
) as m:
    print("Sending a <get-config> operation to the device.\n")
    netconf_reply = m.get_config(source = 'running', filter = netconf_filter)
print("Here is the raw XML data returned from the device.\n")
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
print("")

netconf_data = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
interfaces = netconf_data["interfaces"]["interface"]
print("The interface of the device is: ")
for interface in interfaces:
    print("Interface {} enabled status is {}".format(
        interface["name"],
        interface["enabled"]
    )
)

print("\n")