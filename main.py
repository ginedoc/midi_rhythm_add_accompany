import mido
import chord_analysis

if __name__ == "__main__":
    midsong = chord_analysis.song('resources/melody.mid')
    
    midsong.chord_estimation()