from RTSP2HSL import RTSP_MANAGER
from BaseModel import RTSP_add, RTSP_item
from fastapi import FastAPI
from uuid import uuid4
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import sys


hls_port, server_port = sys.argv[1],sys.argv[2]

app = FastAPI()
rtsp_manager:RTSP_MANAGER = RTSP_MANAGER()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# server = subprocess.Popen("python3 CROS.py 4123", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


@app.post("/add_rtsp/")
def add_rtsp_job(data:RTSP_add):
    id_ = str(uuid4())
    rtsp_manager.add(data.rtsp_url,id_)
    print(rtsp_manager.rtsp)
    return {"url":rtsp_manager.getURL(id_),"id":id_}


@app.get("/get_urls/")
def get_rtsp():
    return rtsp_manager.getAllUrl()    

@app.delete("/rm_rtsp/")
def rm_rtsp_job(data:RTSP_item):
    rtsp_manager.remove(data.rtsp_id)
    return {"rm":True}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", reload=True, port=7123)
