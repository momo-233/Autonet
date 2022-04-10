import netmiko
import json
from netmiko import ConnectHandler

# 存放认证失败的设备信息
switch_with_authentication_issue = []
# 存放网络不通的设备信息
switch_not_reachable = []
with open ('../../jinja2/equinfo/results/info.json') as f:
    dev_info = json.load(f)
    for i in range(len(dev_info)):
        try:       
            with ConnectHandler(**dev_info[i]['connection_info']) as conn:
                hostname = dev_info[i]['connection_info']["host"]
                print(f'已成功登陆交换机{hostname}')
                output = conn.send_command('display cur | inc sysname')
                print(output)    

        except netmiko.NetmikoAuthenticationException:
            print(hostname + "用户验证失败！")
            switch_with_authentication_issue.append(hostname)


        except netmiko.ssh_exception.NetmikoTimeoutException:
            print(hostname + "目标不可达！")
            switch_not_reachable.append(hostname)

print('\n ====结果输出====')
print('*下列交换机用户验证失败: ')
for i in switch_with_authentication_issue:
    print(f'  {i}')

print('*下列交换机不可达: ')
for i in switch_not_reachable:
    print(f'  {i}')