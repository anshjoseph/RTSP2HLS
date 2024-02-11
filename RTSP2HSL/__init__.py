from typing import Dict
from .Server import HLS_SERVER
from .Logging import Process_Logging
import subprocess


class RTSP:
    def __init__(self,rtsp_url:str,name:str,port:int) -> None:
        self.rtsp:str = rtsp_url
        self.name = name
        self.port = port 
        self.stream:subprocess.Popen = None
        self.pid:int = -9999
        self.processStart:bool = False
        self.command:str = f"""ffmpeg -i "{self.rtsp}" -y -c:a aac -b:a 160000 -ac 2 -s 854x480 -c:v libx264 -b:v 800000 -hls_time 10 -hls_list_size 10 -start_number 1 ./Stream/{self.name}/playlist.m3u8""" 
    def start(self)->None:
        subprocess.run(["mkdir",f"./Stream/{self.name}"])
        self.stream = subprocess.Popen(self.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.logger = Process_Logging(self.name,self.stream)
        self.logger.run_logger()
        self.pid = self.stream.pid
        self.processStart = True
    def kill(self)->bool:
        if self.processStart:
            self.processStart = False
            self.stream.terminate()
            return True
        else:
            return False
    def getURL(self)->str:
        return f"http://127.0.0.1:{self.port}/Stream/{self.name}/playlist.m3u8"
    def clean(self)->None:
        subprocess.run(["rm","-rf",f"./Stream/{self.name}/"]) 
    def __eq__(self, __value: object) -> bool:
        if type(self) == type(__value):
            return False
        if self.rtsp == __value.rtsp and self.name == __value.name:
            return True
        return False
class RTSP_MANAGER:
    def __init__(self,port) -> None:
        self.rtsp:Dict[str,RTSP] = dict()
        self.port = port
        self.hls_server = HLS_SERVER(self.port)

    def add(self,rtsp_url:str,name:str):
        if self.rtsp.get(name) == None:
            self.rtsp[name] = RTSP(rtsp_url,name,self.port)
            self.rtsp[name].start()
            return True 
        return False
    
    def getURL(self,name:str)->str:
        return self.rtsp.get(name).getURL()
    
    def getAllUrl(self)->list:
        return {i:self.rtsp[i].getURL() for i in self.rtsp.keys()}
    
    def remove(self,name:str):
        self.rtsp.get(name).kill()
        self.rtsp.get(name).clean()
        return self.rtsp.pop(name)

