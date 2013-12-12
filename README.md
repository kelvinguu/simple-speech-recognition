# Python wrapper for CMU Sphinx-4
A complete speech recognition system configured and ready to use with just a few lines of Python.

```python
import cmu_sphinx4

# currently, the audio must be 16 kHz 16 bit mono in MS WAV format.
audio_URL = 'http://some.site.com/audio.wav'
transcriber = cmu_sphinx4.Transcriber(audio_URL)

for line in transcriber.transcript_stream():
    print line

transcriber.close()
```

**NOTE**: the word error rate (WER) of the default configuration is roughly 0.48. This is still quite high due to the particular choice of parameters.

If you have a better configuration, I would love to hear about it! You can let me know by creating an issue. (Click 'Issues' in the sidebar on the right.)

# Dependencies
- This project uses [**pexpect**](http://pexpect.sourceforge.net/pexpect.html) to interface with CMU Sphinx-4, which is written in Java.

# Install
- On the command line, install **pexpect**: `easy_install pexpect`
- Clone this repo: `git clone git@github.com:ke1vin/simple-speech-recognition.git`
- Obtain the required language model file (which was too big to put in this repo):
    1. Download `HUB4_trigram_lm.zip` [here](http://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/US%20English%20HUB4%20Language%20Model/). This should be roughly 92 MB.
    2. Unzip `HUB4_trigram_lm.zip`. Inside, you will find `language_model.arpaformat.DMP`.
    3. Place `language_model.arpaformat.DMP` inside the `lib/models` folder of this repository.

- When you're done, the `lib/models` folder in your repository should contain the following files:

```
cmudict.0.7a_SPHINX_40
hub4opensrc.cd_continuous_8gau
language_model.arpaformat.DMP
wsj_noisedict
```

- And you're done! Test that your setup works by running `demo_simple.py`

```bash
# make sure that your current working directory is the root of this repo
cd simple-speech-recognition
# run the demo
python demo_simple.py
```

- You should see this output (at this point, not very good):

```
art or should require bonino streamers and maurice greene a university 
offering and lineman bruce slicks educate all course and embrace diverse there it'll crabs sabina university is auckland esso buying a god he use less greedy

ott still there he taught that this land snow competence vote against the government would seem to eye to eye think there'll also sulzer chamberlain on 
through
```

**IMPORTANT NOTE**: `cmu_sphinx4.py` depends on the files in `lib`.
- The files in `lib` should not be rearranged or renamed.
- The `lib` folder has to be placed next to `cmu_sphinx4.py`