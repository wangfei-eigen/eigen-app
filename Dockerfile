# Description: wf-test
# Base images
FROM registry-vpc.cn-hangzhou.aliyuncs.com/eigenlab/ai-base

COPY . /root/testwf
WORKDIR /root/testwf
RUN pip3 install -r /root/requirements.txt

EXPOSE 5000
ENTRYPOINT ["python3","-m","wangfei.py"]
