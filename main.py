import tensorflow as tf

# Create two constant tensors with values 5 and 7
a = tf.constant(5)
b = tf.constant(7)

# Perform addition
result = tf.add(a, b)

# Print the result
print("TensorFlow addition result:", result.numpy())
