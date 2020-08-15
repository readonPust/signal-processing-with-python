from pylab import *

# x(n)=(1 2 3 4 5 6 7 6 5 4 3 2 1), x1(n)=2x(n-5)-3x(n+4), -2<=n<=10
x = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
n = arange(-2, 11, 1)
subplot(2, 1, 1)
stem(n, x, use_line_collection=True)
title('Plot for x(n)');
axis([-15, 15, -15, 15])
grid()


def sigshift(n, k):
    n1 = [i - k for i in n]
    return n1


def amMultiplyer(x, k):
    x1 = [i * k for i in x]
    return x1


def add(x1, n1, x2, n2):
    n3 = sorted(set(n1 + n2))
    s1 = zeros(len(n3))
    s2 = zeros(len(n3))
    for i, j in zip(range(len(n1)), range(len(n2))):
        s1[n3.index(min(n1)) + i] = x1[i]
        s2[n3.index(min(n2)) + j] = x2[j]
    z = s1 + s2
    return n3, z


n1, x1 = add(amMultiplyer(x, 2), sigshift(n, -5), amMultiplyer(x, -3), sigshift(n, 4))
subplot(2, 1, 2)
stem(n1, x1, use_line_collection=True)
title('Plot for x1(n)')
axis([-15, 20, -30, 20])
grid()
tight_layout()
show()
