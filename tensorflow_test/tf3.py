import tensorflow as tf

#定义变量用Variable

state = tf.Variable(0, name='counter')
# print(state.name)
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)

#设定变量就必须initialize
init = tf.initialize_all_variables()

# session = tf.Session()
# session.run(init)
# for i in range(10):
#     session.run(update)
#     print(session.run(state))
#session.close()


with tf.Session() as session:
    session.run(init)
    for i in range(3):
        # session.run(new_value)这一行可省略

        session.run(update)

        print(session.run(state))

























