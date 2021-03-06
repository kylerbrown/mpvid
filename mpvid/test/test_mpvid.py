"""Main test class for matplotvid"""

import os
import pytest
from mpvid import Video
import matplotlib.pyplot as plt


class TestMatplotvidVid:
    """Base class for all matplotvid test classes."""
    def test_Vid_format_input(self):
        with pytest.raises(KeyError):
            Video(encoder='foo')

    def test_Vid_add(self):
        mov = Video()
        N = 10
        for i in range(N):
            mov.add(plt.Figure())
        assert mov.nframes == N
        assert len(os.listdir(mov.frame_dir)) == N

    def test_Vid_del(self):
        mov = Video()
        mov.add(plt.Figure())
        frame_dir = mov.frame_dir
        del mov
        assert not os.path.isdir(frame_dir)
