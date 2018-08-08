#adding accompaniant
"""
instr:
    bass 33~40
"""
import mido

def acc(chord, instr, type, resolution=960):
    if instr>=33 and instr<=40:
        msg=_add_bass(chord, instr, type, int(resolution/4))
    elif instr>=1 and instr<=8:
        print(chord)
        msg=_add_piano(chord, instr, type, int(resolution/4))

    return msg

def _add_bass(chord, instr, type, tick_s):
    #channel 1
    #midi note range: 40(E2)~60(C4)
    #48~59
    last=-1
    note=[mido.Message('program_change', program=instr, channel=1, time=0)]
    for i, c in enumerate(chord):
        if last!=c:
            note.append(mido.Message('note_on', note=chord[i]%12+48, channel=1, time=0))
            note.append(mido.Message('note_off', note=chord[i]%12+48, channel=1, time=tick_s))
        elif i%16==0:
            note.append(mido.Message('note_on', note=chord[i]%12+48, channel=1, time=0))
            note.append(mido.Message('note_off', note=chord[i]%12+48, channel=1, time=tick_s))
        else:
            note.append(mido.Message('note_off', note=chord[i]%12+48, channel=1, time=tick_s))
        last=c
    return note

def _add_piano(chord, instr, type, tick_s):
    #channel 2
    #
    print('tick_s:%d'%tick_s)
    
    note=[mido.Message('program_change', program=instr, channel=2, time=0)]

    for i in range(0, len(chord), 4):
        note.append(mido.Message('note_on', note=chord[i]%12+60, channel=2, time=0))
        
        if chord[i]<12:
            note.append(mido.Message('note_on', note=chord[i]%12+60+4, channel=2, time=0))
            note.append(mido.Message('note_on', note=chord[i]%12+60+7, channel=2, time=0))
            note.append(mido.Message('note_off', note=chord[i]%12+60+4, channel=2, time=4*tick_s))
            note.append(mido.Message('note_off', note=chord[i]%12+60+7, channel=2, time=0))
        elif chord[i]>=12:
            note.append(mido.Message('note_on', note=chord[i]%12+60+3, channel=2, time=0))
            note.append(mido.Message('note_on', note=chord[i]%12+60+7, channel=2, time=0))
            note.append(mido.Message('note_off', note=chord[i]%12+60+3, channel=2, time=4*tick_s))
            note.append(mido.Message('note_off', note=chord[i]%12+60+7, channel=2, time=0))
        
        #note.append(mido.Message('note_off', note=chord[i]%12+60, channel=2, time=4*tick_s))
        note.append(mido.Message('note_off', note=chord[i]%12+60, channel=2, time=0))

    return note


