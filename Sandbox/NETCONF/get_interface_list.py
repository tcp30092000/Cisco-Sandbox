from ncclient import manager
import sys
import xmltodict
import xml.dom.minidom

from device_info import iosxe as device

netconf_filter = """
<filter>
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
<interface></interface>
<interfaces>
</filter>"""

print("Opening RESTCONF Connection to {}".format(device["address"]))
with manager.connect(
    host = device['address'],
    port = device['netconf_port'],
    username = device['username'],
    password = device['password'],
    hostkeys_verify=False
    ) as m:
    print('Sending a <get-config> operation to the device.\n')
    netconf_reply = m.get_config(source = 'running', filter = netconf_filter)

print("Here is the raw XML data returned to the device.\n")
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
print("")

netconf_data = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
interfaces = netconf_data["interfaces"]["interface"]
print("The interface status of the device is: ")
for interface in interfaces:
    print("Interface {} enables status is {}".format(
        interface["name"],
        interface["enables"]
    )
)
print("\n")