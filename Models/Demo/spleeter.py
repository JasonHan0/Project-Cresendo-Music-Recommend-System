from spleeter.separator import Separator
from spleeter.audio.adapter import AudioAdapter

def extract_vocal(in_path, out_path, option=2):
    separator = Separator(f"spleeter:{option}stems")
    separator.separate_to_file(in_path, out_path)


extract_vocal("./donttrustthedawm.mp3", "./thedawn/")
