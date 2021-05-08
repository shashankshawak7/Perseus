""" this code will perform all the networking needs without the fuss to learn them all from cloud"""
import json
import os

class networkingGCP:


    def __init__(self, config, version):
        self.config = config
        self.version = version
        self.initurl = f'https://www.googleapis.com/compute/{version}/projects/'

    def readconfig(self, what_to_create ):
        self.configfilename = f'create{what_to_create}.cfg'
        self.configlocation = os.path.join('./', 'configuration', self.configfilename)
        with open(self.configlocation,'r') as handler:
            data = handler.read()
        data_read = json.loads(data)
        return data_read

    def _createvpc(self,):
        pass

            
            