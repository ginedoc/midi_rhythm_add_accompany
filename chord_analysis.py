import mido
import pyace.pyace.pyace as pyace
from midi2audio import FluidSynth
from pydub import AudioSegment
import os
import locale
from locale import atof
AudioSegment.converter = "/usr/bin/ffmpeg"

class song():
    resolution = 960
    bpm = 96
    tempo = 0
    track = ' '
    track_name = ' '
    mp3path = './resources/mymp3.mp3'
    wavpath = './resources/mywav.wav'
    def __init__(self, path):
        mid = mido.MidiFile(path)
        self.track_name = path
        self.track = mid
        self.resolution = mid.ticks_per_beat
        self.tempo = self._get_tempo()
        self.bpm = self._get_bpm()
    def note_ticks(self,type):
        if type==1:
            res=self.resolution*4
        elif type==2:
            res=self.resolution*2
        elif type==4:
            res=self.resolution
        elif type==8:
            res=self.resolution/2
        elif type==16:
            res=self.resolution/4
        return int(res)
    def chord_estimation(self):
        self._mid2mp3()
        info_timechord = pyace.simpleace(self.mp3path, 'resources/time_domain.txt')
        sixteenth_t = 1/(self.bpm/60)/16
        #tickchord - 16th
        tptr=0
        cptr=0
        info_16 = []
        info_16.append(info_timechord[0][2])

        while tptr<=self.track.length:
            if tptr>atof(info_timechord[cptr][1]):
                cptr += 1
            info_16.append(info_timechord[cptr][2])
            tptr += sixteenth_t
                
        return 0
    ##########################################



    ##########################################
    def _mid2mp3(self):
        #mid2wav
        fs=FluidSynth()
        fs.midi_to_audio(self.track_name, self.wavpath)
        #wav2mp3
        mp3=AudioSegment.from_wav(self.wavpath).export(self.mp3path, format="mp3")
        os.remove(self.wavpath)

    #### bpm
    def _get_bpm(self):
        bpm = mido.tempo2bpm(self.tempo)
        return bpm

    #tempo(midi): microseconds per beats
    def _get_tempo(self):
        for m in self.track:
            if m.is_meta and m.type=='set_tempo':
                return m.tempo
