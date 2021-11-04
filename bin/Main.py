#主执行过程
#1、执行数据加载模块：加载两个模块用于对比
#2、执行对比模块：TODO 过程待定

#执行函数
from bin.configure import ConfMain
from bin.database import DataMain


def main(p1,p2):
    configs = []

    #执行配置模块
    try:
        configs = ConfMain.execute(p1,p2)
        print("加载模块配置成功: ",len(configs))
        print("模块一:%s"%configs[0]["host"])
        print("模块二:%s"%configs[1]["host"])
    except Exception:
        print("加载模块配置失败")
        return 1

    DataMain.execute(configs[0])
    