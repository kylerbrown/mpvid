"""Main test class for matplotvid"""

import os
import pytest
from matplotvid import Vid
from matplotlib import pyplot as plt


class TestMatplotvidVid:
    """Base class for all matplotvid test classes."""
    def test_Vid_format_input(self):
        with pytest.raises(KeyError):
            Vid(encoder='foo')

    def test_Vid_add(self):
        mov = Vid()
        N = 10
        for i in range(N):
            mov.add(plt.Figure())
        assert mov.nframes == N
        assert len(os.listdir(mov.frame_dir)) == N
