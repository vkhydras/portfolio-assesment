import numpy as np
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x.ndim)
print(x.size)
print(x.shape)
print(type(x))
y=np.array([2,1,3])
y=np.append(y,4)
r=y.reshape(2,2)
z=x.reshape(9)

print(y)
print(r)
print(x)
print(z)