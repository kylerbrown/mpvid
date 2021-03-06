''' mpvid.py
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

containers = {'compatibility': 'avi',
               'win': 'wmv',
               'mac': 'mov',
               'browser': 'mp4',
               'broswer-free': 'webm',
               'avi': 'avi',
               'wmv': 'wmv',
               'mp4': 'mp4',
               'webm': 'webm'}


class Video:
    """Organizes saving figures to temporary files and compiling
    the figures into a movie"""
    def __init__(self, framerate=25, quality=1, encoder='compatibility'):
        self.framerate = framerate
        self.quality = quality
        self.encoder_options = ['compatibility',
                                'win', 'mac', 'free']
        self.frame_dir = tempfile.mkdtemp(prefix='matplotvid_')
        if encoder not in containers:
            raise KeyError('enoder must be one of {}'
                           .format(containers))
        self.encoder = encoder
        self.container = containers[encoder]
        self.nframes = 0

    def __del__(self):
        ''' deletes temporary directory containing frames '''
        rmtree(self.frame_dir)

    def add(self, frame):
        """adds a single figure as a frame in the movie
        by printing the figure to a temporary file"""
        if frame.canvas is None:
            FigureCanvas(frame)
            frame.canvas.draw()
        filename = 'frame_{:07d}.png'.format(self.nframes)
        print(filename)
        frame.savefig(os.path.join(self.frame_dir, filename))
        self.nframes += 1

    def encode(self, filename=None):
        """feeds the saved image files from Video.add()
        to avconv to construct a movie"""
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
