import mido
import midiscore as ms

if __name__ == "__main__":
    midsong = ms.song('resources/melody.mid')
    #chord = midsong.chord_estimation()
    midsong.add_accompaniant(chord, 35) # bass
    midsong.add_accompaniant(chord, 4)  # piano

