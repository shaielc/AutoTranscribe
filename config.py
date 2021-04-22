from music21 import environment
config = environment.UserSettings()
config['lilypondPath'] = r'C:\Program Files (x86)\LilyPond\usr\bin\lilypond.exe'
config["musicxmlPath"] = r'C:\Program Files\MuseScore 3\bin\MuseScore3.exe'
config["musescoreDirectPNGPath"] = config["musicxmlPath"]