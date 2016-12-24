FROM ubuntu:xenial
RUN apt-get update && apt-get install -y \
  software-properties-common
RUN add-apt-repository ppa:fkrull/deadsnakes
RUN apt-get update && apt-get install -y \
  python3.5 \
  python3.5-dev \
  python3-pip
RUN pip3 install flask
WORKDIR /app
COPY app /app
CMD ["python3", "app.py"]
