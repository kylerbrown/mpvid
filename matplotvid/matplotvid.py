''' matplotmov.py
a simple object-oriented video creation
tool for a sequence of matplotlib figures,
spefically for use in presentations '''

from __future__ import print_function, unicode_literals
from subprocess import call
import tempfile
from shutil import rmtree
import os.path
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

__version__ = '0.1'

_containers = {'compatibility': 'avi',
               'win': 'wmv',
               'mac': 'mac',
               'free': 'x264'}


class Vid:
    def __init__(self, framerate=25, quality=1, encoder='compatibility'):
        self.framerate = framerate
        self.quality = quality
        self.encoder_options = ['compatibility',
                                'win', 'mac', 'free']
        self.frame_dir = tempfile.mkdtemp(prefix='matplotvid_')
        if encoder not in _containers:
            raise Exception('enoder must be one of {}'
                            .format(_containers))
        self.encoder = encoder
        self.container = _containers[encoder]
        self.nframes = 0

    def __del__(self):
        ''' deletes temporary directory containing frames '''
        rmtree(self.frame_dir)

    def add(self, frame):
        if frame.canvas is None:
            FigureCanvas(frame)
        filename = 'frame_{:07d}.png'.format(self.nframes)
        print(filename)
        frame.savefig(os.path.join(self.frame_dir, filename))
        self.nframes += 1

    def encode(self, filename=None):
        if filename is None:
            filename = os.path.split(self.frame_dir)[-1]
        frames = os.path.join(self.frame_dir, 'frame_%07d.png')
        call_lst = ['avconv', '-i',
                    '"{}"'.format(frames),
                    '-r', str(self.framerate),
                    '-qscale', str(self.quality),
                    '{filename}.{extention}'
                    .format(filename=filename,
                            extention=self.container)]
        call_str = " ".join(call_lst)
        print(call_str)
        # The quotes in the avconv command cause issues without
        # shell=True and a single command string.
        call(call_str, shell=True)
