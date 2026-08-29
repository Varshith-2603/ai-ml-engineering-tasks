#1
x = 2
y = 3
df1_dx = 2*x
df1_dy = 1
df2_dx = y
df2_dy = x
jacobian = [
    [df1_dx,df1_dy],
    [df2_dx,df2_dy]
]
print("df1_dx:",df1_dx)
print("df1_dy:",df1_dy)
print("df2_dx:",df2_dx)
print("df2_dy:",df2_dy)
print("Jacobian:",jacobian)

#2
x = 2
y = 4
df1_dx = 6*x
df1_dy = 2
df2_dx = 4*y
df2_dy = 4*x
jacobian = [
    [df1_dx,df1_dy],
    [df2_dx,df2_dy]
]
print("Jacobian:",jacobian)


#3
import numpy as np
x = np.array([1,2,3])
y = np.array([2,3,4])
df1_dx = 2*x
df1_dy = 1
df2_dx = y
df2_dy = x
print("X:",x)
print("Y:",y)
print("df1_dx:",df1_dx)
print("df1_dy:",df1_dy)
print("df2_dx:",df2_dx)
print("df2_dy:",df2_dy)


#4
w1 = 2
w2 = 3
df1_dw1 = 2*w1
df1_dw2 = 3
df2_dw1 = 2*w2
df2_dw2 = 2*w1
jacobian = [
    [df1_dw1,df1_dw2],
    [df2_dw1,df2_dw2]
]
print("df1_dw1:",df1_dw1)
print("df1_dw2:",df1_dw2)
print("df2_dw1:",df2_dw1)
print("df2_dw2:",df2_dw2)
print("Jacobian:",jacobian)

#5
w1 = 2
w2 = 3
df1_dw1 = 6*w1
df1_dw2 = 2*w2
df2_dw1 = w2
df2_dw2 = w1
jacobian = [
    [df1_dw1,df1_dw2],
    [df2_dw1,df2_dw2]
]
print("Jacobian:",jacobian)

#6
import numpy as np
df1_dx1 = 2
df1_dx2 = -4
df1_dx3 = 3
df2_dy1 = 5
df2_dy2 = 1
df2_dy3 = -2
jacobian = np.array([
    [df1_dx1,df1_dx2,df1_dx3],
    [df2_dy1,df2_dy2,df2_dy3]

])
print("Jacobian:",jacobian)
inputs = df1_dx1,df1_dx2,df1_dx3
outputs = df2_dy1,df2_dy2,df2_dy3
print("Number of inputs:",(len(inputs)))
print("Number of outputs:",(len(outputs)))


#JACOBIAN FOR VECTOR VALUED FUNCTION
#1
x = 2
y = 3
df1_dx = 2*x
df1_dy = 1
df2_dx = y
df2_dy = x
jacobian = [
    [df1_dx,df1_dy],
    [df2_dx,df2_dy]
]
print("df1_dx:",df1_dx)
print("df1_dy:",df1_dy)
print("df2_dx:",df2_dx)
print("df2_dy:",df2_dy)
print("Jacobian:",jacobian)

#2
x = 2
y = 4
df1_dx = 6*x
df1_dy = 2
df2_dx = y
df2_dy = 2*y
jacobian = [
    [df1_dx,df1_dy],
    [df2_dx,df2_dy]
]
print("Jacobian:",jacobian)

#3
import numpy as np
x = np.array([1,2,3])
y = np.array([2,3,4])
df1_dx = 2*x
df1_dy = 1
df2_dx = y
df2_dy = x
print("X:",x)
print("Y:",y)
print("df1_dx:",df1_dx)
print("df1_dy:",df1_dy)
print("df2_dx:",df2_dx)
print("df2_dy:",df2_dy)


#4
w1 = 2
w2 = 3
df1_dw1 = 2*w1
df1_dw2 = 3
df2_dw1 = w2
df2_dw2 = w1
jacobian = [
    [df1_dw1,df1_dw2],
    [df2_dw1,df2_dw2]
]
print("df1_dw1:",df1_dw1)
print("df1_dw2:",df1_dw2)
print("df2_dw1:",df2_dw1)
print("df2_dw2:",df2_dw2)
print("Jacobian:",jacobian)

#5
w1 = 2
w2 = 3
df1_dw1 = 4*w1
df1_dw2 = 2*w2
df2_dw1 = 3*w2
df2_dw2 = 0
jacobian = [
    [df1_dw1,df1_dw2],
    [df2_dw1,df2_dw2]
]
print("Jacobian:",jacobian)

#6
x1 = 2
x2 = 3
x3 = 4
df1_dx1 = 2*x1
df1_dx2 = 2
df1_dx3 = 3
df2_dx1 = x2
df2_dx2 = x1
df2_dx3 = 2*x3
jacobian = [
    [df1_dx1,df1_dx2,df1_dx3],
    [df2_dx1,df2_dx2,df2_dx3]
]
print("df1_dx1:",df1_dx1)
print("df1_dx2:",df1_dx2)
print("df1_dx3:",df1_dx3)
print("df2_dx1:",df2_dx1)
print("df2_dx2:",df2_dx2)
print("df2_dx3:",df2_dx3)
print("Jacobian:",jacobian)


#JACOBIAN IN ML
#1
x1 = 2
x2 = 3
dy1_dx1 = 2
dy1_dx2 = 3
dy2_dx1 = 4
dy2_dx2 = 1
jacobian = [
    [dy1_dx1,dy1_dx2],
    [dy2_dx1,dy2_dx2]
]
print("dy1_dx1:",dy1_dx1)
print("dy1_dx2:",dy1_dx2)
print("dy2_dx1:",dy2_dx1)
print("dy2_dx2:",dy2_dx2)
print("Jacobian:",jacobian)

#2
x1 = 2
x2 = 3
dy1_dx1 = 2*x1
dy1_dx2  = 1
dy2_dx1 = x2
dy2_dx2 = x1
jacobian = [
    [dy1_dx1,dy1_dx2],
    [dy2_dx1,dy2_dx2]
]
print("Jacobian:",jacobian)

#3
import numpy as np
x1 = np.array([1,2,3])
x2 = np.array([2,3,4])
dy1_dx1 = 2*x1
dy1_dx2 = 1
dy2_dx1 = x2
dy2_dx2 = x1
print("X1:",x1)
print("X2:",x2)
print("dy1_dx1:",dy1_dx1)
print("dy1_dx2:",dy1_dx2)
print("dy2_dx1:",dy2_dx1)
print("dy2_dx2:",dy2_dx2)


#4
dy1_dx1 = 2
dy1_dx2 = 4
dy1_dx3 = 6
dy2_dx1 = 1
dy2_dx2 = 3
dy2_dx3 = 5
inputs = 2,4,6
outputs = 2,1
jacobian = [
    [dy1_dx1,dy1_dx2,dy1_dx3],
    [dy2_dx1,dy2_dx2,dy2_dx3]
]
print("Jacobian:",jacobian)
print("Number of Inputs:",len(inputs))
print("Number of Outputs:",len(outputs))

#5
x1 = 2
x2 = 3
dy1_dx1 = 2*x1 
dy1_dx2 = 2*x1
dy2_dx1 = 3*x2
dy2_dx2 = 2*x2
jacobian = [
    [dy1_dx1,dy1_dx2],
    [dy2_dx1,dy2_dx2]
]
print("Jacobian:",jacobian)

#6
x1 = 2
x2 = 1
dy1_dx1 = 4*x1
dy1_dx2 = x1
dy2_dx1 = 3
dy2_dx2 = 4*x2
jacobian = [
    [dy1_dx1,dy1_dx2],
    [dy2_dx1,dy2_dx2]
]
print("dy1_dx1:",dy1_dx1)
print("dy1_dx2:",dy1_dx2)
print("dy2_dx1:",dy2_dx1)
print("dy2_dx2:",dy2_dx2)
print("Jacobian:",jacobian)


#HESSIAN
#1
fxx = 2
fxy = 0
fyy = 2
fyx = 0
hessian = [
    [fxx,fxy],
    [fyx,fyy]
]
print("Hessian:",hessian)

#2
fxx = 6
fxy = 0
fyy = 10
fyx = 0
hessian = [
    [fxx,fxy],
    [fyx,fyy]
]
print("Hessian:",hessian)

#3
import numpy as np
fxx = 2
fxy = 4
fyx = 4
fyy = 6
hessian = np.array([
    [fxx,fxy],
    [fyx,fyy]
])
print("Hessian:",hessian)

#4
w1 = 2
w2 = 4
w3 = 3
partial_w1 = 2*w1
partial_w2 = 6*w2
second_partial_dw1 = 2
mixed_partial_w1 = 0
mixed_partial_w2 = 0
second_partial_dw2 = 6
hessian = [
    [second_partial_dw1,mixed_partial_w1],
    [mixed_partial_w2,second_partial_dw2]

]
print("∂L/∂w1:",partial_w1)
print("∂L/∂w2:",partial_w2)
print("∂²L/∂w1²:",second_partial_dw1)
print("∂²L/∂w1∂w2:",mixed_partial_w1)
print("∂²L/∂w2∂w1:",mixed_partial_w2)
print(" ∂²L/∂w2²:",second_partial_dw2)
print("Hessian:",hessian)

#5
partial_w1 = 4*w1+4*w2
partial_w2 = 4*w1+6*w2
second_partial_dw1 = 8*w2
mixed_partial_w1 = 8*w1
mixed_partial_w2 = 10*w2
second_partial_dw2 = 10*w1
hessian = [
    [second_partial_dw1,mixed_partial_w1],
    [mixed_partial_w2,second_partial_dw2]

]
print("Hessian:",hessian)

#6
partial_dw1 = 2*w1+2*w2
partial_dw2 = 2*w1+6*w2+4*w3
partial_dw3 = 4*w2+10*w3
second_partial_dw1 = 4*w2
second_partial_dw2 = 8*w1+4*w3
second_partial_dw3 = 14*w2
mixed_partial_w1_w2 = 4*w1
mixed_partial_w2_w1 = 8*w2+4*w3
mixed_partial_w1_w3 = 0
mixed_partial_w2_w3 = 2*w1+10*w2
mixed_partial_w3_w1 = 0
mixed_partial_w3_w2 = 14*w3
hessian = [
    [second_partial_dw1,mixed_partial_w1_w2,mixed_partial_w1_w3],
    [mixed_partial_w2_w1,second_partial_dw2,mixed_partial_w2_w3],
    [mixed_partial_w3_w1,mixed_partial_w3_w2,second_partial_dw3]
]
print("Hessian:",hessian)
