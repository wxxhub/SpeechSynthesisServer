FROM python:3.8-alpine

#将当前目录所有文件copy到app目录下
ADD . /app  

# 进入到app目录
WORKDIR /app
RUN pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r requirement.txt
RUN pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r speech_synthesis/requirement.txt

# 对外暴露端口
EXPOSE 8888

#ENTRYPOINT ["python"]
CMD ["python","app.py"]
