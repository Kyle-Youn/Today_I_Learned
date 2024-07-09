'''
[Reference]
https://wikidocs.net/237265
'''

'''
[CMD]
pip install git+https://github.com/suno-ai/bark.git
'''

from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio

# download and load all models
preload_models()

# generate audio from text
text_prompt = "실행이 완료되었습니다."
audio_array = generate_audio(text_prompt)

# save audio to disk
write_wav("C:/Users/Administrator/Downloads/bark_generation.wav", SAMPLE_RATE, audio_array)

# play text in notebook
Audio(audio_array, rate=SAMPLE_RATE)
