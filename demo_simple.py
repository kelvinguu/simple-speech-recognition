import cmu_sphinx4
import os

def from_cwd(relative_path):
    return os.path.join(os.getcwd(), relative_path.lstrip('\/'))

# this must be a canonical URL, with no relative path symbols such as ..
# WARNING: the audio file specified MUST be 16 kHz 16 bit mono files in
# MS WAV format.
audio_URL = 'file://localhost' + from_cwd('audio/npr_short.wav')

transcriber = cmu_sphinx4.Transcriber(audio_URL)

# due to some initialization in Sphinx-4, it may take 30 - 60 seconds before you
# start seeing any transcriptions
for line in transcriber.transcript_stream():
    print line

transcriber.close()
