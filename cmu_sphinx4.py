import pexpect
import os
import inspect

def from_lib_dir(relative_path):
    """
    Return a full canonical path, by resolving relative_path as if the current
    directory was the directory of lib
    """
    # TODO: may not work for every OS
    module_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    lib_dir = os.path.join(module_dir, 'lib')
    abs_path =  os.path.join(lib_dir, relative_path.lstrip('\/'))
    return abs_path

class Transcriber(object):
    lang_model = from_lib_dir('models/language_model.arpaformat.DMP')
    accoustic_model = from_lib_dir('models/hub4opensrc.cd_continuous_8gau')
    dictionary = from_lib_dir('models/cmudict.0.7a_SPHINX_40')
    filler = from_lib_dir('models/wsj_noisedict')

    default_params = {
        'absoluteBeamWidth': '1000',
        'absoluteWordBeamWidth': '100',
        'relativeBeamWidth': '1E-80',
        'relativeWordBeamWidth': '1E-60',
        'wordInsertionProbability': '0.2',
        'silenceInsertionProbability': '.1',
        'languageWeight': '8',
        'languageModelLocation': lang_model,
        'acousticModelLocation': accoustic_model,
        'dictionaryPath': dictionary,
        'fillerPath': filler
        }

    def __init__(self, audio_URL, parameters=default_params):
        """
        Create Sphinx-4 config file with specified parameters.
        WARNING: the audio file specified MUST be 16 kHz 16 bit mono files in
        MS WAV format.
        """
        self.audio_URL = audio_URL
        self.config_path = from_lib_dir('config_{}.xml'.format(id(self)))

        # load text from config_template.xml
        template_path = from_lib_dir('config_template.xml')
        with open(template_path, 'r') as input_file:
            text = input_file.read()

        # insert appropriate values
        for param, value in parameters.iteritems():
            placeholder = '${' + param + '}'
            text = text.replace(placeholder,value)

        # write text to config.xml
        with open(self.config_path,'w+') as output_file:
            output_file.write(text)

    def close(self):
        """
        Deletes Sphinx-4 config file associated with this object.
        """
        try:
            os.remove(self.config_path)
        except OSError:
            pass

    def transcript_stream(self):
        """
        Launch Sphinx-4 and pass it the target audio.
        """
        # construct class_path
        sphinx_jar_path = from_lib_dir('sphinx4.jar')
        class_path = from_lib_dir('') + ":" + sphinx_jar_path
        config_URL = 'file://localhost' + self.config_path

        # execute CMU Sphinx
        command_list = ['java', '-cp', class_path, 'StreamingTranscriber', self.audio_URL, config_URL]
        command = ' '.join(command_list)

        proc = pexpect.spawn(command)

        while True:
            try:
                proc.expect('\n')
                output = proc.before
                if 'WARNING dictionary' in output and 'Missing word:' in output:
                    continue
                if 'Falling back to non-recursive partition' in output:
                    continue
                yield output
            except pexpect.EOF:
                break
