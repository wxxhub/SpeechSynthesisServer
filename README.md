# SpeechSynthesisServer
# 语音合成服务，支持docker部署

## 源码使用
```shell 

git submodule init
git submodule update

# python3 

pip3 install -r requirement.txt
pip3 install -r speech_synthesis/requirement.txt
python3 app.py
```

## 如何更新为remote submodule
```
git submodule update --remote --recursive
```


## 打包成docker镜像
```docker
docker build -t speech_synthesis_server:latest .
docker run -d --name speech_syntheis_server -p 8888:8888 speech_synthesis_server:latest
```

## 使用已经打包好的docker镜像
```
docker pull registry.cn-beijing.aliyuncs.com/wxxhub/speech_synthesis:latest
docker run -d --name speech_synthesis -p 8888:8888 registry.cn-beijing.aliyuncs.com/wxxhub/speech_synthesis:latest
```

## 语音合成使用
```
浏览器访问 127.0.0.1:8888

#或者终端使用curl,（windows终端因为编码不是utf-8问题可能失败, 将终端改为utf-8即可）
curl -X POST -F content="你好世界" 127.0.0.1:8889/speech_synthesis -o test.wav
```
