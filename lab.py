import numpy as np
import tensorflow as tf
x = np.random.randint(1,100)
y = np.random.randint(0,100)
model = tf.keras.Sequential([tf.keras.layers.Dense(units =4,activation='relu',input_shape=())])

