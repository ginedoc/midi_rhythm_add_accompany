import mido
import midiscore as ms

if __name__ == "__main__":
    midsong = ms.song('resources/melody.mid')
    chord = midsong.chord_estimation('./model/model2_05.h5')
    midsong.add_accompaniant(chord, 35) # bass
    midsong.add_accompaniant(chord, 4)  # piano

