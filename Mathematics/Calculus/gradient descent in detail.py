#1
w = 5
gradient = 10
learning_rate = 0.1
new_w = w-learning_rate*gradient
print("Old Weight:",w)
print("Gradient:",gradient)
print("Learning Rate:",learning_rate)
print("New Weight:",new_w)

#2
w = 4
gradient = -6
learning_rate = 0.2
new_w = w-learning_rate*gradient
print("Old Weight:",w)
print("Gradient:",gradient)
print("Learning Rate:",learning_rate)
print("New weight:",new_w)

#3
import numpy as np
weights = np.array([2.0,4.0,6.0])
gradient = np.array([4.0,6.0,8.0])
learning_rate = 0.1
new_weights = weights-learning_rate*gradient
print("Weights:",weights)
print("Gradient:",gradient)
print("Learning Rate:",learning_rate)
print("New Weights:",new_weights)

#4
w1 = 3
w2 = 2
learning_rate = 0.1
partial_w1 = 2*w1
partial_w2 = 6*w2
gradient = np.array([partial_w1,partial_w2])
new_w1 = w1-learning_rate*gradient[0]
new_w2 = w2-learning_rate*gradient[1]
print("Partial Derivative w.r.t W1:",partial_w1)
print("Partial Derivative w.r.t W2:",partial_w2)
print("Gradient:",gradient)
print("New W1:",new_w1)
print("New W2:",new_w2)


#5
import numpy as np
w1 = 2
w2 = 3
learning_rate = 0.05
partial_w1 = 4*w1
partial_w2 = 8*w2
gradient = np.array([partial_w1,partial_w2])
new_w1 = w1-learning_rate*gradient[0]
new_w2 = w2-learning_rate*gradient[1]
print("Partial Derivative w.r.t w1:",partial_w1)
print("Partial Derivative w.r.t w2:",partial_w2)
print("Gradient:",gradient)
print("New W1:",new_w1)
print("New W2:",new_w2)

#6
w1 = 2
w2 = 1
w3 = 3
learning_rate = 0.1
partial_w1 = 2*w1+2*w2
partial_w2 = 2*w1+6*w2
partial_w3 = 10*w3
gradient = np.array([partial_w1,partial_w2,partial_w3])
new_w1 = w1-learning_rate*gradient[0]
new_w2 = w2-learning_rate*gradient[1]
new_w3 = w3-learning_rate*gradient[2]
print("Partial Derivative w.r.t w1:",partial_w1)
print("Partial Derivative w.r.t w2:",partial_w2)
print("Partial Derivative w.r.t w3:",partial_w3)
print("gradient:",gradient)
print("New W1:",new_w1)
print("New W2:",new_w2)
print("New W3:",new_w3)