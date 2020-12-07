import tensorflow as tf
import random

print('--- Creating a single perceptron...')
graph = tf.Graph()
with graph.as_default():
    # https://www.tensorflow.org/api_docs/python/tf/compat/v1/placeholder
    x = tf.compat.v1.placeholder(tf.float32, shape=[], name="x")
    # https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable
    A = tf.compat.v1.get_variable('A', shape=[], dtype=tf.float32,
     initializer=tf.initializers.random_normal())
    # b = tf.random_normal(shape=[], dtype=tf.float32, name='b')
    b = tf.random.normal(shape=[], dtype=tf.float32, name='b')
    y = A * x
    z = y + b

print('--- Using the perceptron with x == 4')
# https://www.tensorflow.org/api_docs/python/tf/compat/v1/Session
sess = tf.compat.v1.Session(graph=graph)
with sess:
    # https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables_initializer
    sess.run(tf.compat.v1.global_variables_initializer())
    result = sess.run(z, feed_dict={x: 4})

print('--- Result', result)
