''' matplotmov.py: an simple object-oriented video creation tool for a sequence of matplotlib figures, spefically for use in presentations '''

import matplotlib
import os

class Vid:
    def __init__(self, framerate=25, quality=1, encoder='compatibility'):
        #self.endict={'compatibility' : '.avi'}
        self.framerate = framerate
        self.quality = quality
        self.encoder_options=['compatibility', 'win', 'mac', 'free']
        self.dirname='matplotmov' + repr(self).split()[-1][0:-2]
        self.frame_dir = os.name == 'posix' and '/tmp/' + self.dirname + '/' or '.' + self.dirname
        if encoder not in self.encoder_options:
            raise Exception, 'enoder must be one of ' + str(self.encoder_options)
        self.encoder = encoder
        self.nframes = 0
        ''' prepare frame directory '''
        os.mkdir(self.frame_dir)
        
    def clean(self):
        ''' deletes temporary directory containing frames '''
        os.rmdir(self.frame_dir)

    def add(self, frame):
        if not frame.__class__ == matplotlib.figure.Figure:
            raise Exception, 'frame is not a matplotlib figure \
        i.e. frame.__class__ == matplotlib.figure.Figure \
        must be True'
        filename = 'frame_%05d.png'%self.nframes
        print('saving frame ' + str(self.nframes))
        frame.savefig(self.frame_dir + filename)
        self.nframes += 1

    def encode(self,filename=None):
        if filename==None:
            filename=self.dirname
        if os.name == 'posix':
            frames=self.frame_dir + 'frame_%05d.png'
            system_string="avconv -i " + '\'' + frames + '\'' \
              + " -r " + str(self.framerate) \
              + " -qscale " + str(self.quality) \
              + " " + filename + "." +  self.encode_postfix()
            os.system(system_string)
            print system_string
        else:
            print('doh!')
            
    def encode_postfix(self):
        if self.encoder == 'compatibility':
            return('avi')
        if self.encoder == 'win':
            return('wmv')
        if self.encoder == 'mac':
            return('mov')
        if self.encoder == 'free':
            return('x264')
            
