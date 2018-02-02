import random
import numpy as np

def create_dataset(hm, variance, step=2, correlation=False):
    val = 1
    ys = []
    for i in range(hm):
        y = val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation and correlation == 'pos':
            val+=step
        elif correlation and correlation == 'neg':
            val-=step
    xs = [i for i in range(hm)]
    return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)

cor = 'neg'
print(cor and cor == 'neg')

print(create_dataset(10, 2, 2, False))