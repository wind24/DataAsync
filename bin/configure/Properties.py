import os

class Properties:
    fileName = ''
    def __init__(self, fileName):
        self.fileName = fileName
    def getProperties(self):
        try:
            pro_file = open(self.fileName, 'r')
            properties = {}
            for line in pro_file:
                if line.find('=') > 0:
                    strs = line.replace('\n', '').split('=')
                    properties[strs[0]] = strs[1]
        except Exception :
            raise Exception
        else:
            pro_file.close()
        return properties