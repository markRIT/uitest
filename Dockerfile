FROM python:3.7.4
RUN mkdir -p /uitest
COPY /* /uitest/
RUN pip install --upgrade pip -i http://mirrors.aliyun.com/pypi/simple/ \
&& pip install configparser schedule setuptools urllib3 -i http://mirrors.aliyun.com/pypi/simple/
WORKDIR /uitest

CMD ["/bin/bash","run.sh"]