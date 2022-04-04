# SpeechSynthesisServer
# 语音合成服务，支持docker部署

```shell 

git submodule init
git submodule update

# python3 

pip3 install -r requirement.txt
pip3 install -r speech_synthesis/requirement.txt
python3 app.py
```

```docker
docker build -t speech_synthesis_server:latest .
docker run -d --name speech_syntheis_server -p 8888:8888 speech_synthesis_server:latest
```

# 使用docker镜像
```
docker pull registry.cn-beijing.aliyuncs.com/wxxhub/speech_synthesis:latest
docker run -d --name speech_synthesis -p 8888:8888 registry.cn-beijing.aliyuncs.com/wxxhub/speech_synthesis:latest
```
