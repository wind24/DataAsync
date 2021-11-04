#请求数据的执行函数
from bin.database import HttpDataRequest

def execute(config):

    type = config["type"]
    if type == "testHttp":
        request = HttpDataRequest.TestHttpDataRequest(config)
        data = request.request()
        print(data)