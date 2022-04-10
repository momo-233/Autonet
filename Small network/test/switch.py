from jinja2 import Environment,FileSystemLoader
import yaml

env = Environment(loader=FileSystemLoader('.\\'))
template = env.get_template('1.jinja2')

with open('.\\1.yaml') as f:
    sws = yaml.safe_load(f)

for sw in sws:
    swx_conf = sw['name'] + '.txt'
    with open(f'.\\{swx_conf}', 'w') as f:
        f.write(template.render(sw))


print("文件生成完毕！") 