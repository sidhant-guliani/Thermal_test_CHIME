pl.clf()
npts=1024
a=7.
b=3.
z=1.*np.arange(npts)/npts
line=a+b*z

c=.7
d=.3



signal= line+np.random.random(size=npts) +c*np.cos(17.3*z) +d*np.sin(62.*z)
                                           
zsignal=signal-signal.mean()           # zsignal has 0 mean.
sft=np.fft.fft(zsignal-b*(z-.5))      # sft is the signal fft
df=0.03
f1=np.exp(-z**2/(2.*df**2))
f2=np.exp(-(1.-z)**2/(2.*df**2))
filter=f1+f2

lpsft= sft*filter        # lpsft is a low-pass sft

lpinv=np.fft.ifft(lpsft)           # lpinv is the inv ft of lpsft

pl.plot(z,signal)
pl.plot(z,lpinv+signal.mean()+b*(z-.5))  # notice factor of 2!!

pl.plot(z,lpinv+signal.mean()+b*(z-.5),'r')

pl.plot(z,signal-(lpinv+signal.mean()+b*(z-.5)),'g')

pl.plot(z,2.*lpinv,'r') 
