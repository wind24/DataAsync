#根据传递进来的参数请求数据，这里封装一个抽象类，具体实现根据配置实现，每个配置实现一个请求对象

from abc import abstractmethod,ABCMeta


class BaseDataRequest(metaclass=ABCMeta):
    def __init__(self,pro):pass

    @abstractmethod
    def request():pass