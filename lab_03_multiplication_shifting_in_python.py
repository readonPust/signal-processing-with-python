from pylab import *

# Multiplication
n1 = list(arange(-2, 2, 1))
x = [1, 0, 3, 4]
subplot(3, 1, 1)
stem(n1, x, use_line_collection=True)
title("X")
axis([-3, 4, 0, 5])
grid()

n2 = list(arange(0, 4, 1))
y = [1, 1, 1, 1]
subplot(3, 1, 2)
stem(n2, y, use_line_collection=True)
title("Y")
axis([-3, 4, 0, 5])
grid()

# adding signal
# n3 = list(arange(min(min(n1), min(n2)), max(max(n1), max(n2)) + 1, 1))
n3 = sorted(set(n1 + n2))
s1 = zeros(len(n3))
s2 = zeros(len(n3))
for i, j in zip(range(len(n1)), range(len(n2))):
    s1[n3.index(min(n1)) + i] = x[i]
    s2[n3.index(min(n2)) + j] = y[j]
z = s1 * s2

subplot(3, 1, 3)
stem(n3, z, use_line_collection=True)
title("X * Y")
axis([-3, 4, 0, 8])
grid()
tight_layout()
show()

# signal shifting
k = 7
dn1 = [i + k for i in n1]
subplot(2, 1, 1)
stem(dn1, x, use_line_collection=True)
title("Delayed X")
grid()

k1 = 5
an1 = [i - k1 for i in n1]
subplot(2, 1, 2)
stem(an1, x, use_line_collection=True)
title("Advanced X")
grid()

tight_layout()
show()

print()
