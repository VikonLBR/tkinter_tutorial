import tensorflow as tf

#添加神经层
def add_layer(inputs, input_size, output_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([input_size, output_size]))
    biases = tf.Variable(tf.zeros([1,output_size])+0.1)#推荐的biases不为零
    Wx_plus_b = tf.matmul(inputs*Weights)+biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return  outputs





