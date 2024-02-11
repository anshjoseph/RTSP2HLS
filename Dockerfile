FROM ubuntu

RUN apt update
RUN apt install -y python3 python3-pip
RUN apt install -y ffmpeg
WORKDIR /app
COPY . .
RUN pip install -r requirement.txt

CMD [ "python3","app.py","4000","5000" ]