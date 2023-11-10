import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split

# Generate some example data
np.random.seed(0)
X = np.random.rand(100, 2)  # Random values for lectures attended and hours spent studying
y = np.random.randint(2, size=100)  # Binary labels (0: fail, 1: pass)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(2, input_shape=(2,), activation='relu'),  # Input layer with 2 neurons
    tf.keras.layers.Dense(1, activation='sigmoid')  # Output layer with 1 neuron (sigmoid for binary classification)
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test))

# Evaluate the model
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")
