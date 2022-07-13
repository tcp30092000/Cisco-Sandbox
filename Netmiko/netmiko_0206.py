import netmiko
SW3 = {
    'device_type' : 'cisco_ios',
    'ip' : '10.215.27.13',
    'username' : 'vnpro',
    'password' : 'vnpro@123',
    'secret' : 'vnpro@321'
}
connect = netmiko.ConnectHandler(**SW3)
connect.enable()
#list_command = ['vlan 10','name VnPro']
#print(connect.send_config_set(list_command))
for i in range(20,101,10):
    print(connect.send_config_set([f"vlan {i}"]))
#print(connect.send_config_set([""]))
print(connect.send_config_set(["do show vlan br"]))






