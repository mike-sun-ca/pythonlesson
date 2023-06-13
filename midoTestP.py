import mido
'''msg = mido.Message('note_on', note=60)
msg.type
msg.note
msg.bytes()
msg.copy(channel=2)

port = mido.open_output(mido.ports.BaseOutput)
#port.send(msg)
#portname=mido.get_output_names()
'''
from mido import Message, MidiFile, MidiTrack    #懒得说  
      
mid = MidiFile()       #给自己的文件定的.mid后缀  
track = MidiTrack()    #定义声部，一个MidoTrack()就是一个声部  

track.append(Message('program_change',channel=0,program= 2,time=0))   
track.append(Message('note_on', note=60, velocity=64, time=12,channel=0))   
track.append(Message('note_off', note=60, velocity=64, time=12,channel=0)) 