#测试用http请求类

from bin.database.DataRequest import BaseDataRequest
from bin.database import HttpUtils


class TestHttpDataRequest(BaseDataRequest):
    config = {}
    
    def __init__(self, pro):
        BaseDataRequest.__init__(self,pro)
        self.config = pro

    def request(self):
        return HttpUtils.doGet(self.config["host"])