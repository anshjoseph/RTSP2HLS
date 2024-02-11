from threading import Thread
import time

class Process_Logging:
    def __init__(self,id,process) -> None:
        self.path = f"./logs/{id}.txt"
        self.file = open(self.path,'+a')
        self.process = process
    def __logger(self,file,process):
        for line in process.stdout.readlines():
            file.write(line.decode())
            time.sleep(0.200)
    def run_logger(self):
        self.thread = Thread(target=self.__logger,args=(self.file,self.process))
        self.thread.start()


    