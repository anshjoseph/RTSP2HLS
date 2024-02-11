from RTSP2HSL import RTSP_MANAGER



class RTSP2HSL_MANAGER:
    def __init__(self,port) -> None:
        self.rtsp_manager:RTSP_MANAGER = RTSP_MANAGER(port)
    def add(self,rtsp_url,id):
        self.rtsp_manager.add(rtsp_url,id)
    def getAll(self):
        return self.rtsp_manager.getAllUrl()
    def get(self,id):
        return self.rtsp_manager.get(id)
    def delete(self,id):
        return self.rtsp_manager.remove(id)