from pylab import *

t = arange(-20, 20, 1)

unitstep = (t >= 0)
impulse = (t == 0)
unitramp = t * unitstep

subplot(3, 1, 1)
stem(t, unitstep, use_line_collection=True)
title('Unitstep')
xlabel('Time')
ylabel('Amplitude')

subplot(3, 1, 2)
stem(t, impulse, use_line_collection=True)
title('Impulse')
xlabel('Time')
ylabel('Amplitude')

subplot(3, 1, 3)
stem(t, unitramp, use_line_collection=True)
title('Unitramp')
xlabel('Time')
ylabel('Amplitude')
tight_layout()
show()
