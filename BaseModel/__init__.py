from pydantic import BaseModel


class RTSP_add(BaseModel):
    rtsp_url:str

class RTSP_item(BaseModel):
    rtsp_id:str

