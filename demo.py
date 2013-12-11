import os
import cmu_sphinx4
import pexpect

def from_cwd(relative_path):
    return os.path.join(os.getcwd(), relative_path.lstrip('\/'))

# path parameters passed into Transcriber must be full paths, not relative
lang_model = from_cwd('models/language_model.arpaformat.DMP')
accoustic_model = from_cwd('models/hub4opensrc.cd_continuous_8gau')
dictionary = from_cwd('models/cmudict.0.7a_SPHINX_40')
filler = from_cwd('models/wsj_noisedict')

parameters = {
    'absoluteBeamWidth': '700',
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

audio_URL = 'file://localhost' + from_cwd('audio/npr_short.wav')
transcriber = cmu_sphinx4.Transcriber(audio_URL, parameters)

for line in transcriber.transcript_stream():
    print line

transcriber.close()
