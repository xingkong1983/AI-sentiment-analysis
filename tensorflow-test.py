import tensorflow as tf
a = tf.constant(10)
b = tf.constant(32)
print (tf.add(a,b))

g = lambda x,y,z : x + y + z + 1 
print(g(3,4,5))

def g2(x,y, z):
    return x +y + z+1
print(g2(3,4,5))
