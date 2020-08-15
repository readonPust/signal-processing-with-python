from pylab import *

A = 5
f = 50.0  # Frequency of sinusoid
fs = 100 * f  # Very high sampling rate
nCycle = 5  # generate five cycles of sinusoid
t = arange(0, nCycle * 1 / f, 1 / fs)  # time index
y = A * sin(2 * pi * f * t)

subplot(3, 1, 1)
plot(t, y)
title("Continuous sinusoidal signal")
xlabel("Time(s)")
ylabel("Amplitude")
grid()

fs1 = 17 * f
t1 = arange(0, nCycle * 1 / f, 1 / fs1)
y1 = A * sin(2 * pi * f * t1)
subplot(3, 1, 2)
stem(t1, y1, use_line_collection=True)
title('Sampling of a sinusoidal signal')
xlabel('Time(s)')
ylabel('Amplitude')
grid()

# quantization
y2 = np.round(y1)
subplot(3, 1, 3)
stem(t1, y2, use_line_collection=True)
title('Quantization of a sinusoidal signal')
xlabel('Time(s)')
ylabel('Amplitude')
grid()
tight_layout()
show()
for x in y2:
    print(bin(int(A + x)))
