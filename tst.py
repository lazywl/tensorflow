import tensorflow as tf
import numpy as np

#create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

#create tensorflow layer start
weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases =tf.Variable(tf.zeros([1]))

with tf.Session() as sess:
    print (sess.run(weights))
    print (sess.run(biases))
