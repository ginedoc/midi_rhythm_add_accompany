import mido
import pyace.pyace.pyace as pyace
from midi2audio import FluidSynth
from pydub import AudioSegment
import os
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
        self.bpm = _get_bpm(self.resolution)
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
        pyace.simpleace(self.mp3path, 'resources/time_domain.txt')
        return 0

    def _mid2mp3(self):
        #mid2wav
        fs=FluidSynth()
        fs.midi_to_audio(self.track_name, self.wavpath)
        #wav2mp3
        mp3=AudioSegment.from_wav(self.wavpath).export(self.mp3path, format="mp3")
        os.remove(self.wavpath)

    def _get_bpm(resolution):
        _get_tempo()

    def _get_tempo():
        for m in self.track:
            for mm in m:
                if mm.is_meta and mm.type=='set_tempo':
                    return mm.tempo
