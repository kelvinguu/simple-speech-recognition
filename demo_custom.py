import os
import cmu_sphinx4

def from_cwd(relative_path):
    return os.path.join(os.getcwd(), relative_path.lstrip('\/'))

# path parameters passed into Transcriber must be full paths, not relative
lang_model = from_cwd('lib/models/language_model.arpaformat.DMP')
accoustic_model = from_cwd('lib/models/hub4opensrc.cd_continuous_8gau')
dictionary = from_cwd('lib/models/cmudict.0.7a_SPHINX_40')
filler = from_cwd('lib/models/wsj_noisedict')

# note that numbers must be expressed as strings
parameters = {
    'absoluteBeamWidth': '500',
    'absoluteWordBeamWidth': '100',
    'relativeBeamWidth': '1E-80',
    'relativeWordBeamWidth': '1E-60',
    'wordInsertionProbability': '0.2',
    'silenceInsertionProbability': '.1',
    'languageWeight': '10.5',
    'languageModelLocation': lang_model,
    'acousticModelLocation': accoustic_model,
    'dictionaryPath': dictionary,
    'fillerPath': filler
}

# WARNING: the audio file specified MUST be 16 kHz 16 bit mono files in
# MS WAV format.
audio_URL = 'file://localhost' + from_cwd('audio/npr_short.wav')
transcriber = cmu_sphinx4.Transcriber(audio_URL, parameters)

# due to some initialization in Sphinx4, it may take 30 - 60 seconds before you
# start seeing any transcriptions
for line in transcriber.transcript_stream():
    print line

transcriber.close()
