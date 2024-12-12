import numpy as np

def gradient_descent(starting_point, learning_rate, iterations):
    points = [starting_point]
    current_point = starting_point

    for _ in range(iterations):
        grad = np.array([2 * current_point[0], 2 * current_point[1]])
        next_point = current_point - learning_rate * grad
        points.append(next_point)
        current_point = next_point

    return np.array(points)

#Example
initial_point = np.array([4.0, 3.0])  
learning_rate = 0.1  
iterations = 50  
path = gradient_descent(initial_point, learning_rate, iterations)
print(path)

