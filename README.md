matplotvid
==========

Create a video from a series of matplotlib figures.
Currently supports only POSIX compliant systems (Mac, Linux). Windows support is planned.

Requirements
==

*avconv*

in Ubuntu/Debian: 
sudo apt-get install libav-tools

Example
==
```python
''' An example matplotmov script '''
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