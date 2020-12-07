# https://hub.docker.com/_/python
# DTT 07/12/20 According to https://www.tensorflow.org/install,
#              TensorFlow 2 doesn't support Python 3.9 yet
FROM python:3.8.6-buster

RUN mkdir /app
WORKDIR /app

RUN apt-get update \
    # Latest pip asked by https://www.tensorflow.org/install
    && pip install --upgrade pip

# All Python required libraries are defined in the requirements.txt file
COPY tf2image-requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Consider commenting all lines below if you prefer to execute manually
# the micro example
COPY tf2-microexample.py tf2-microexample.py

CMD ["python", "tf2-microexample.py"]
