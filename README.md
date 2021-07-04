# SpeechSynthesisServer
# 语音合成服务，支持docker部署

```shell
# python3

pip3 install -r requirement.txt
pip3 install -r speech_synthesis/requirement.txt
python3 app.py
```

```docker
docker build -t speech_synthesis_server:latest .
docker run -d --name speech_syntheis_server -p 8888:8888 speech_synthesis_server:latest
```
