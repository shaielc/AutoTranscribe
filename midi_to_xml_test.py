import os
import re
from music21 import converter

midi_ext= re.compile("\.midi?$")
xml_ext = ".xml"
lily_ext = ".ly"

filepath = r"C:\Users\Shaiel Cohen\Documents\MuseScore3\Scores"

midi_files = [ os.path.join(filepath, entry) for entry in os.listdir(filepath) if midi_ext.search(entry)]
print(midi_files)
for midi_file in midi_files:
    print(midi_file)
    score = converter.parse(midi_file)
    print("out to: ", re.sub(midi_ext, xml_ext, midi_file))
    score.write("MusicXML", fp=re.sub(midi_ext, xml_ext, midi_file))
    score.write("lily", fp=re.sub(midi_ext, lily_ext,midi_file ))
    # score.write("lily.pdf",fp=re.sub(midi_ext, ".pdf", midi_file))
    
    score.write("musicxml.png",fp=re.sub(midi_ext, ".png", midi_file))
