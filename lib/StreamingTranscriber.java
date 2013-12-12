import edu.cmu.sphinx.frontend.util.AudioFileDataSource;
import edu.cmu.sphinx.recognizer.Recognizer;
import edu.cmu.sphinx.result.Result;
import edu.cmu.sphinx.util.props.ConfigurationManager;

import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.UnsupportedAudioFileException;
import java.io.IOException;
import java.net.URL;

public class StreamingTranscriber {

    public static void main(String[] args) throws Exception {

        String audioURLString = args[0];
        String configURLString = args[1];

        URL audioURL = new URL(audioURLString);
        URL configURL = new URL(configURLString);

        AudioInputStream in = getStream(audioURL);
        Recognizer recognizer = getRecognizer(configURL,in);

        int silenceCounter = 0;
        while (true) {
            Result result = recognizer.recognize();

            if (result != null) {
                silenceCounter = 0;
                String resultText = result.getBestResultNoFiller();
                System.out.println(resultText);
            } else {
                silenceCounter++;
                if (silenceCounter >= 5) {
                    break;
                }
            }
        }
    }

    public static Recognizer getRecognizer(URL configURL, AudioInputStream in) {

        ConfigurationManager cm = new ConfigurationManager(configURL);
        Recognizer recognizer = (Recognizer) cm.lookup("recognizer");
        recognizer.allocate();

        AudioFileDataSource dataSource = (AudioFileDataSource) cm.lookup("audioFileDataSource");
        dataSource.setInputStream(in, null);

        return recognizer;
    }

    public static AudioInputStream getStream(URL audioURL) throws IOException, UnsupportedAudioFileException {

        AudioInputStream in0 = AudioSystem.getAudioInputStream(audioURL);

        // TODO: get real conversion

        // change format to what Sphinx wants
        //AudioFormat format1 = new AudioFormat(AudioFormat.Encoding.PCM_SIGNED,
        //        (float) 16000.0,
        //        16,
        //        1,
        //        2,
        //        (float) 16000.0,
        //        false);
        //
        //AudioInputStream in1 = AudioSystem.getAudioInputStream(format1,in0);

        AudioInputStream in1 = in0;

        /*
        System.out.println("Original format: " + in0.getFormat());
        System.out.println("New format: " + in1.getFormat());
        */
        return in1;
    }
}
