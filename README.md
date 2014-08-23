mpvid
==========

Create a video from a series of matplotlib figures, using [avconv](https://libav.org/avconv.html).

Useful for quick and dirty movies of complex plots not easily animated with `matplotlib.animation`, such as plots with error-bars, subplots etc.

Compatible with python 2 and 3.

Requirements
====

*avconv*

in Ubuntu/Debian: 
sudo apt-get install libav-tools

Example 1
====
```python
''' An example matplotvid script '''
import numpy as np
import matplotlib.pyplot as plt
import matplotvid

mov = mpvid.Vided() 


for i in range(25):
    fig = plt.figure()
    sig=np.random.rand(100)
    plt.plot(sig)
    mov.add(fig)
    plt.close()

mov.encode('random_stuff')
print "done"
```

Example 2
==========

```python
import matplotlib.pyplot as plt
from mpvid import Video
from numpy.random import randn


def create_figure(data1, data2):
    """ a nonsense example plot with many features """
    fig = plt.figure()
    plt.suptitle(str(sum(data1)))
    ax1 = plt.subplot(211)
    plt.errorbar(data1, data2, data1**2, data2**2)
    plt.ylim((-3, 3))
    plt.subplot(212, sharex=ax1)
    plt.hist(data1, alpha=.5)
    plt.hist(data2, alpha=.5)
    plt.xlim((-3, 3))
    return fig


vid = Video(encoder='mp4')
for i in range(50):
    data1 = randn(20)
    data2 = randn(20)
    vid.add(create_figure(data1, data2))
    plt.close()
vid.encode('output')
```

