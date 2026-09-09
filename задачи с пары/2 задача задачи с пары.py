import scipy.special as sc
import math
from scipy.integrate import quad

print("1.37", round(1 / sc.factorial(7), 4))

print("1.38", sc.factorial(2)**3*sc.factorial(3)/sc.factorial(10))

print("1.39a", round(sc.comb(15, 4)/sc.comb(25, 4), 4))

print("1.39б", round(sc.comb(15, 10)/sc.comb(25, 4), 4))

print("1.42", round((sc.comb(20, 3)*sc.comb(10, 2) +
      sc.comb(20, 4)*sc.comb(10, 1)+sc.comb(20, 5))/sc.comb(30, 5), 4))

print("1.45", round((sc.comb(19, 2)*sc.comb(5, 1)+sc.comb(19, 3))/sc.comb(24, 3), 4))

print("1.47", round(sc.factorial(8) * sc.factorial(3) / sc.factorial(10), 4))
c = 0
for q in range(1, 7):
    for w in range(1, 7):
        for e in range(1, 7):
            if q+w+e == 11:
                c += 1

print("1.48a", round(c / (6 * 6 * 6), 4))
# print(c)
c = 0
for q in range(1, 7):
    for w in range(1, 7):
        for e in range(1, 7):
            if q+w+e > 10:
                c += 1
# print(c)
print("1.48б", round(c / (6 * 6 * 6), 4))


def f1(x):
    return min(x+1/3, 1)


def f2(x):
    return max(x-1/3, 0)


r1 = quad(f1, 0, 1)

r2 = quad(f2, 0, 1)

print("Геом", round(r1[0]-r2[0], 4))
