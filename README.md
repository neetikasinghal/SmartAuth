# SmartAuth

This project is used for performing voice authentication for the pre-existing users with the bank.

We want to put the latest technology into use and replace the stereotype of user login into the system with the pin. Hence, we introduce voice authentication which would rather use user’s voice print in order to login into the system.

The project comprises of two flows:
1.	Registration: The process of user registration begins by entering the pre-existing unique user ID to SmartAuth. If the user Id exists, the user would then be prompted with set of text samples three times, in order to make our machine learn about the user’s voice. These text samples are unique in nature and comprise of words that cover all the possible phonetic sounds.
	Once the user prompts the given text, the audio signal processing happens in two folds:
•	Silence removal: The pauses and breaks while speaking are removed.
•	Noise removal: The background noise is removed from the signal.
The audio processed signal is then used for spectral feature extraction. Two set of features are used:
•	MFCC
•	Spectogram
Both the features combined gives us a feature vector of dimension [1X168]
This feature vector is then used to train the Gaussian Mixture Model(GMM).

2.	Authentication: The process of authentication begins again by entering the pre-existing unique user ID to SmartAuth. The user is again prompted to voice over a text sample, the voice print is captured, processed for noise and silence removal, then calculated for a feature vector. The GMM model is then made and compared with the log likelihood of the pre-existing models. The model returning the maximum likelihood is recognized as the user’s model, already registered. In case, the model doesn’t match in the first go, the user is given a maximum of three attempts in order to authenticate himself.

Dataset: SmartAuth uses 950 samples from open-source VoxForge.
Testing samples comprise of 30 samples comprising the real-time voices collected by us.

Accuracy: 83%

Technology Stack: Python, Librosa, Sox, Scikit-learn

Run: To run the project, follow the setup.sh.
