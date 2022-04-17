from jinja2 import Environment,FileSystemLoader
import yaml

env = Environment(loader=FileSystemLoader('.\\'))
template = env.get_template('external.jinja2')

with open('.\\external.yaml') as f:
    sws = yaml.safe_load(f)

for sw in sws:
    swx_conf = sw['name'] + '.txt'
    with open(f'..\\results\{swx_conf}', 'w') as f:
        f.write(template.render(sw))


print("文件生成完毕！") 