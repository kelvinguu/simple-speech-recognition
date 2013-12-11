import cmu_sphinx4

def from_cwd(relative_path):
    return os.path.join(os.getcwd(), relative_path.lstrip('\/'))

# this must be a canonical URL, with no relative path symbols such as ..
audio_URL = 'file://localhost' + from_cwd('audio/npr_short.wav')
transcriber = cmu_sphinx4.Transcriber(audio_URL, parameters)

# due to some initialization in Sphinx4, it may take 30 - 60 seconds before you
# start seeing any transcriptions
for line in transcriber.transcript_stream():
    print line

transcriber.close()
