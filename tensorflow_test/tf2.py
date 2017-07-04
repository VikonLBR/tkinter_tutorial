import tensorflow as tf


#以矩阵乘法为例
#constant 为常量

matrix_a = tf.constant([[1, 2], [3, 4]])
matrix_b = tf.constant([[1, 3],
                        [1, 3]])
produce = tf.matmul(matrix_a, matrix_b)


# #method 1
# session = tf.Session()
# result = session.run(produce)
# print(result)
# session.close()


#method 2
#用with不需要close，是局部使用，自动关闭，类似于存在于for中的变量
with tf.Session() as session:
    result = session.run(produce)
    print(result)




