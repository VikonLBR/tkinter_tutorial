import numpy as np
import tensorflow as tf

#create a Variable
def tt():
    w=tf.Variable(initial_value=[[1,2],[3,4]],dtype=tf.float32)
    x=tf.Variable(initial_value=[[1,1],[1,1]],dtype=tf.float32)
    y=tf.matmul(w,x)
    z=tf.sigmoid(y)


tt()
tt()
init_op=tf.global_variables_initializer()


with tf.Session() as session:
    session.run(init_op)
    z=session.run(z)
    print(z)