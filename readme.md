# RTSP 2 HSL
- why we doing this?
  
    Because rtsp is didn't support by web browser so i convert rtsp to hsl stream via ffmpeg 
    i make a module around the rtsp to convert hsl 

- command 
  ``` shell
  docker build . -t rtsp2hls

  docker run -p 7123:7123 -p 4123:4123 --network bridge  --name rtsp2hls rtsp2hls

  
  ``` 






















