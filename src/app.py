import subprocess
from os import system, name
import os


from nix.models.TTS import NixTTSInference


import wave
from IPython.display import Audio
from playsound import playsound
#==================================CONFIG CRAP========================================

TimeBetweenSentences = 5  #time break between sentences



#==============================FUNCTION DEFINITIONS====================================

#get text from clipboard
def get_selected_text_clipboard():
    try:
        # Use xclip to get the selected text from the clipboard
        selected_text = subprocess.check_output(["xclip", "-o", "-selection", "primary"], universal_newlines=True)
        return selected_text
    except subprocess.CalledProcessError:
        return None


textRegister = get_selected_text_clipboard() #contains clipboard text



def speak(sentence):
    cwd = os.getcwd()
    nix = NixTTSInference(model_dir = cwd+"/models/deterministic")
    c, c_length, phoneme = nix.tokenize(sentence)
    xw = nix.vocalize(c, c_length)
    Audio(xw[0,0], rate=22050)







#===============================PROGRAM STARTS HERE=====================================


speak("ambata blow, don't cum don't cum!")

exit()












