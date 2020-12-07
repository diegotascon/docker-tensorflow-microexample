# Building a TensorFlow 1 image from the official TensorFlow image
# https://hub.docker.com/r/tensorflow/tensorflow
FROM tensorflow/tensorflow:1.15.4-py3

RUN mkdir /app
WORKDIR /app

# Consider commenting all lines below if you prefer to execute manually
# the micro example
COPY tf1-microexample.py tf1-microexample.py

CMD ["python", "tf1-microexample.py"]
