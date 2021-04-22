import os
from audio_to_midi import audio_to_midi
fileext = ".wav"
filename = "twinkle_high-converted" 
filepath = os.path.join(r"C:\Users\Shaiel Cohen\Documents\MuseScore3\Scores", filename + fileext)
out_filepath = os.path.join(r"C:\Users\Shaiel Cohen\Documents\MuseScore3\Scores", filename + "-parsed" + ".mid")
audio_to_midi(filepath, out_filepath)

