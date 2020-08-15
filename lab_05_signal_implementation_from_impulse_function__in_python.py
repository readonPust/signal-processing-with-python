from pylab import *


# x(n)=2d(n+2)-d(n-4), -5<=n<=5;

def sigshift(a, n, k):
    n1 = n + k
    impulse = (n1 == 0)
    return impulse * a


n = arange(-5, 6, 1)
x = sigshift(2, n, 2) - sigshift(1, n, -4)
stem(n, x, use_line_collection=True)
tight_layout()
show()
