FROM python:3.8-alpine

#将当前目录所有文件copy到app目录下
ADD . /app  

# 进入到app目录
WORKDIR /app
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
RUN apk add --no-cache g++
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirement.txt
RUN pip install -r speech_synthesis/requirement.txt

# 对外暴露端口
EXPOSE 8888

#ENTRYPOINT ["python"]
CMD ["python","app.py"]
