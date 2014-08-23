matplotvid
==========

Create a video from a series of matplotlib figures, using [avconv](https://libav.org/avconv.html).

Useful for quick and dirty movies of complex plots not easily animated with `matplotlib.animation`, such as plots with error-bars, subplots etc.

Requirements
==

*avconv*

in Ubuntu/Debian: 
sudo apt-get install libav-tools

Example
==
```python
''' An example matplotvid script '''
import numpy as np
import matplotlib.pyplot as plt
import matplotvid

mov = matplotvid.Vid() 


for i in range(25):
    fig = plt.figure()
    sig=np.random.rand(100)
    plt.plot(sig)
    mov.add(fig)
    plt.close()

mov.encode('random_stuff')
print "done"
```
