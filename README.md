# Toy containers for a TensorFlow micro example

This is just a tiny project with 2 different examples showing how to create a docker image to execute a micro example of TensorFlow use. The code example was shown in the first Hands-On lecture in the [Artificial Intelligence with Deep Learning postgraduate course](https://www.talent.upc.edu/cat/estudis/formacio/curs/305502/postgrau-artificial-intelligence-deep-learning/).

## Why?
Up to this point in the course we've been working with [Google Colab](https://colab.research.google.com) notebooks. But production systems work different. From the lectures I have imagined that docker images are one of the possible choices to deploy a Deep Learning model in production.

## Two images
You'll find two docker images:
* TF1-image: derived from the official tensorflow/tensorflow:1.15.4 image, it deploys a TensorFlow 1 to run the micro example (which uses TF1)
* TF2-image: instead of using a pre-built tensorflow docker image, I have tried to build a latest-version TensorFlow image from a official Python image. I've adapted the micro example code to avoid TF2 complaining about TF1 code

## Building and running the images
Example intructions for a Linux host with docker are provided below:

### TF1-image
* Building: `docker image build -t tf1image -f tf1image-fromtf.dockerfile .`
* Running: `docker container run --rm tf1image`
* Run a container and get a bash shell: `docker container run -it --rm -v $(pwd):/app -u $(id -u):$(id -g) tf1image bash`
  * Once in bash: `python tf1-microexample.py`

### TF2-image
* Building: `docker image build -t tf2image -f tf2image-frompython.dockerfile .`
* Running: `docker container run --rm tf2image`
* Run a container and get a bash shell: `docker container run -it --rm -v $(pwd):/app tf2image bash`
  * Once in bash: `python tf2-microexample.py`

## Disclaimer
Take this content as just a possible way to do execute TensorFlow code. Don't consider it as a best practice example as I'm just a beginner.
