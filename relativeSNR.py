import matplotlib.pyplot as plt 
import numpy as np
s = np.arange(0, 10000, 1)
x=s

y0=np.sqrt(s)
plt.plot(x,y0/y0,'r',label='Perfect Camera')

y1=(0.72*s)/np.sqrt(0.72*s+2.5**2)
plt.plot(x,y1/y0,'b',label='Thorlabs Kiralux® CMOS 5 MP')

y2=(0.6*s)/np.sqrt(0.60*s+7.0**2)
plt.plot(x,y2/y0,'g',label='Thorlabs 1.4 MP CCD')

y3=(0.82*s)/np.sqrt(0.82*s+1.1**2)
plt.plot(x,y3/y0,'c',label='Andor Zyla 4.2 PLUS')

y4=(0.64*s)/np.sqrt(0.64*s+1.2**2)
plt.plot(x,y4/y0,'m',label='Andor Zyla 5.5')

y5=(0.95*s)/np.sqrt(0.95*s+1.8**2)
plt.plot(x,y5/y0,'y',label='Photometrics Prime 95B')

y6=(0.95*s)/np.sqrt(0.95*s+1.1**2)
plt.plot(x,y6/y0,'k',label='Photometrics Prime BSI Express')

y7=(0.95*s)/np.sqrt(0.95*s+0.7**2)
plt.plot(x,y7/y0,'darkorange',label='Hamamatsu ORCA-Fusion BT Digital CMOS camera')

y8=(0.70*s)/np.sqrt(0.70*s+6.6**2)
plt.plot(x,y8/y0,'lime',label='Hamamatsu ORCA-spark Digital CMOS camera')

y9=(0.78*s)/np.sqrt(0.78*s+7.0**2)
plt.plot(x,y9/y0,'deeppink',label='Thorlabs Kiralux® CMOS 2.3 MP')

y10=(0.61*s)/np.sqrt(0.61*s+1.0**2)
plt.plot(x,y10/y0,'yellow',label='Thorlabs Quantalux® sCMOS 2.1 MP')

plt.xscale("log")
plt.axis([1, 10000, 0, 1.1])
plt.legend(loc='lower right')
plt.xlabel('Input Signal Photon')
plt.ylabel('Relative SNR')
plt.show()