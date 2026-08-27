#1
x = 2
y = 3
partial_x = 2*x
partial_y = 6*y
gradient = [partial_x,partial_y]
print("Gradient:",gradient)


#2
x = 4
y = 2
partial_x = 6*x
partial_y = 10*y
gradient = [partial_x,partial_y]
print("Gradient:",gradient)

#3
import numpy as np
x = np.array([1,2,3,4])
y = np.array([2,3,4,5])
gradient_x = [2*x]
gradient_y = [8*y]
gradient_vector = [gradient_x,gradient_y]
print("X:",x)
print("Y:",y)
print("Gradient w.r.t x:",gradient_x)
print("Gradient w.r.t y:",gradient_y)
print("Gradient vector for every pair:",gradient_vector)

#4
import math
w1 = 3
w2 = 4
partial_w1 = 2*w1
partial_w2 = 6*w2
gradient = [partial_w1,partial_w2]
magnitude = math.sqrt(gradient[0]**2+gradient[1]**2)
direction = [gradient[0]/magnitude,gradient[1]/magnitude]
print("Partial Derivative w.r.t w1:",partial_w1)
print("Partial Derivative w.r.t w2:",partial_w2)
print("Gradient:",gradient)
print("Gradient Magnitude:",magnitude)
print("Gradient Direction:",direction)

#5
w1 = 1
w2 = 2
w3 = 3
partial_w1 = 4*w1
partial_w2 = 8*w2
partial_w3 = 12*w3
gradient = [partial_w1,partial_w2,partial_w3]
weights = [w1,w2,w3]
index = np.argmax(np.abs(gradient))
print("Partial Derivative w.r.t w1:",partial_w1)
print("Partial Derivative w.r.t w2:",partial_w2)
print("Gradient:",gradient)
print("Largest absoulte gradient component:",gradient[index])
print("Corresponding Weight:",weights[index])

#6
import math
w1 = 2
w2 = 1
w3 = 3
partial_w1 = 6*w1 + 2*w2
partial_w2 = 2*w1 + 8*w2
partial_w3 = 10*w3
gradient = [partial_w1,partial_w2,partial_w3]
magnitude = math.sqrt(gradient[0]**2+gradient[1]**2)
direction = [gradient[0]/magnitude,gradient[1]/magnitude]
print("Partial Derivative w.r.t w1:",partial_w1)
print("partial Derivative w.r.t w2:",partial_w2)
print("Gradient:",gradient)
print("Gradient Magnitude:",magnitude)
print("Gradient Direction:",direction)