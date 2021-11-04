#执行主模块
from bin import Main
import sys

#第一个参数的名字：-p1，这个参数是模块名称，以这个值作为config文件的文件名去configure目录找对应的文件，如：p1Value.properties
p1NameIndex = -1
#第一个参数的值，参数索引是-p1的index+1
p1Value = ""
#第二个参数的名字：-p2，这个参数是模块名称，以这个值作为config文件的文件名去configure目录找对应的文件，如：p2Value.properties
p2NameIndex = -1
#第二个参数的值，参数索引是-p2的index+1
p2Value = ""

#执行参数
args = sys.argv

#获取第一个参数
try:
    p1NameIndex = args.index('-p1')
    p1Value = args[p1NameIndex + 1]
except Exception :
    p1NameIndex = -1
    p1Value = ""

#获取第二个参数
try:
    p2NameIndex = sys.argv.index('-p2')
    p2Value = args[p2NameIndex + 1]
except Exception:
    p2NameIndex = -1
    p2Value = ""

if len(p1Value) == 0 :
    print("[Error]: You need to config the first mode.")
elif len(p2Value) == 0:
    print("[Error]: You need to config the second mode.")
else:
    Main.main(p1Value,p2Value)

