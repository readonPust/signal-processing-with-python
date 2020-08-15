from pylab import *

w = arange(0, 501, 1) * pi / 500
H=(e**(1j*w))/((e**(1j*w))-0.9*ones(501))

magH=abs(H)
angH=angle(H)

subplot(2,1,1)
plot(w/pi,magH)
grid()
xlabel('frequency in pi units')
ylabel('|H|')
title('Magnitude Response')
subplot(2,1,2)
plot(w/pi,angH/pi)
grid()
xlabel('frequency in pi units')
ylabel('phase in pi radians')
title('phase response')

tight_layout()
show()

