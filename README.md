
# Python wrapper for CMU Sphinx-4
A complete speech recognition system configured and ready to use with just a few lines of Python:

```python
import cmu_sphinx4

# currently, the audio must be 16 kHz 16 bit mono in MS WAV format.
audio_URL = 'http://some.site.com/audio.wav'
transcriber = cmu_sphinx4.Transcriber(audio_URL)

for line in transcriber.transcript_stream():
    print line

transcriber.close()
```

## Usage

### Processing local files
To point the transcriber to a file on your computer, just prepend `file://localhost` to the front of your file path, which makes it a URL:

```python
audio_URL = 'file://localhost' + '/Users/Kelvin/audio.wav'
```

### Processing live/never-ending audio streams
The transcriber will output text as the audio is being read in, rather than waiting to read the whole file before processing. So, you can set the `audio_URL` to a never-ending or live audio stream and it will still work.

(`transcriber.transcript_stream()` is a [generator](https://wiki.python.org/moin/Generators) which will keep producing lines of transcribed text while the audio keeps playing.)

### A note on accuracy
The word error rate (WER) of the default configuration is roughly 0.48. This is still quite high due to the particular choice of parameters.

**If you have a better configuration, I would love to incorporate it (and of course credit you here).** You can let me know by creating an issue. (Click 'Issues' in the sidebar on the right.)

## About CMU Sphinx-4
[CMU Sphinx-4](http://cmusphinx.sourceforge.net/) is one of the most popular open source speech recognition systems, according to [Wikipedia](http://en.wikipedia.org/wiki/List_of_speech_recognition_software). However, it takes some effort to set up, and doesn't work on large vocabularies without some configuration. This Python wrapper has done all that work for you, so you can immediately start converting speech to text!

## Dependencies
- This project uses [**pexpect**](http://pexpect.sourceforge.net/pexpect.html) to interface with CMU Sphinx-4, which is written in Java.
- CMU Sphinx-4 is *already included in this repository* as `sphinx.jar`, so there is no need to download it. `sphinx.jar` is the latest version of Sphinx-4 provided on Sourceforge as of December 11, 2013.

## Install
- Install **pexpect** on the command line: `easy_install pexpect`
- Clone this repo: `git clone https://github.com/kelvinguu/simple-speech-recognition.git`
- Obtain the required language model file (which was too big to put in this repository):
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

- And you're done! Test that your setup works by running `demo_simple.py`:

```bash
# make sure that your current working directory is the root of this repo
cd simple-speech-recognition
# run the demo
python demo_simple.py
```

- You should see this output (at this point, not very good):

```
art or should require bonino streamers and maurice greene a university 
offering and lineman bruce slicks educate all course and embrace diverse
there it'll crabs sabina university is auckland esso buying a god he use less greedy

ott still there he taught that this land snow competence vote against the
government would seem to eye to eye think there'll also sulzer chamberlain on through
```

**IMPORTANT NOTE**: `cmu_sphinx4.py` depends on the files in `lib`.
- The files in `lib` should not be rearranged or renamed.
- The `lib` folder has to be placed next to `cmu_sphinx4.py`
