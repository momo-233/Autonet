import yaml
from jinja2 import Template, FileSystemLoader, Environment

j2_loader = FileSystemLoader('./')
env = Environment(loader=j2_loader)
j2_tmpl = env.get_template('./templates/acl_comm.jinja2')
# 加载变量文件，解析成列表/字典
with open('acl.yaml') as f:
    vars = yaml.safe_load(f.read())
result = j2_tmpl.render(vars)
f=open(r'../../netmiko/command/acl.txt','w')
print(result,file=f)
f.close()
print('设备命令生成完毕!')

