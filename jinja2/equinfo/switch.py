import yaml
from jinja2 import Template, FileSystemLoader, Environment
import os

j2_loader = FileSystemLoader('./')
env = Environment(loader=j2_loader)
j2_tmpl = env.get_template('./templates/huawei.jinja2')
# 加载变量文件，解析成列表/字典
with open('huawei.yaml') as f:
    vars = yaml.safe_load(f.read())
result = j2_tmpl.render(vars)
f=open(r'results/info.json','w')
print(result,file=f)
f.close()



#删除逗号
# 在文本文件中，若没有使用b模式选项打开的文件，只允许从文件头开始计算相对位置，从文件尾计算时就会引发异常
file_old = open(r'results/info.json','rb+')
m = 100
# 1.定位文件末尾的前m个字符的位置，大小可根据每一行的字符数量修改，为一估计值，但不能超过文件总字符数
# 若要删除最后一行，要确保m比最后一行的字符数大
# 若要删除后N行，要确保后N行的总字符数比m小
# 若文件很小或无法大体估计每一行的字符数，可以删除这行代码
file_old.seek(-m, os.SEEK_END)	 

# 2.从步骤1定位的位置开始读取接下来的每一行数据，若步骤1的代码删除，则会从文件头部开始读取所有行
lines = file_old.readlines()	

# 3.定位到最后一行的行首，若要删除后N行，将lines[-1]改为lines[-N:]即可
file_old.seek(-len(lines[-6]), os.SEEK_END)	

file_old.truncate()  # 截断之后的数据 


file = open(r'results/info.json','a')   #再次打开文件添加 ']'方括号闭合json文件数据
file.seek(0)
file.write(']')
file_old.close()
print('登录信息生成完毕!!')

