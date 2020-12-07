import tensorflow as tf
import random

print('--- Creating a single perceptron...')
graph = tf.Graph()
with graph.as_default():
    x = tf.placeholder(tf.float32, shape=[], name="x")
    A = tf.get_variable('A', shape=[], dtype=tf.float32,
     initializer=tf.initializers.random_normal())
    b = tf.random_normal(shape=[], dtype=tf.float32, name='b')
    y = A * x
    z = y + b

print('--- Using the perceptron with x == 4')
sess = tf.Session(graph=graph)
with sess:
    sess.run(tf.global_variables_initializer())
    result = sess.run(z, feed_dict={x: 4})

print('--- Result', result)
