import tensorflow as tf

input_a = tf.placeholder(tf.float32, [1, 2])
input_b = tf.placeholder(tf.float32, [2, 1])

output = tf.matmul(input_a, input_b)

with tf.Session() as session:
    #seesion.run()的时候填入，用feed_dict装填
    result = session.run(output, feed_dict={input_a: [[1., 1.]], input_b: [[2.], [3.]]})
    print(result)





















