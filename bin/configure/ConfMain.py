#加载模块配置的入口

from bin.configure.Properties import Properties

def execute(p1,p2):

    modeConfigs = []

    #加载第一个配置文件
    try:
        filename1 = "./confs/%s.properties"%p1
        print("加载模块文件：",filename1)
        p = Properties(fileName=filename1)
        properties = p.getProperties()
        modeConfigs.append(properties)
    except Exception:
        print("[Error]：read the first properties failure.")
        raise Exception

    try:
        #加载第二个配置文件
        filename2 = "./confs/%s.properties"%p2
        print("加载模块文件：",filename2)
        p = Properties(fileName=filename2)
        properties = p.getProperties()
        modeConfigs.append(properties)
    except Exception:
        print("[Error]：read the second properties failure.")
        raise Exception

    return modeConfigs