#*******************************************************************************************************
#************************** SETUP FOR SMARTAUTH *******************************************************
#*******************************************************************************************************

echo "Python Version required : 3.5 and above"
python --version

ret=`python -c 'import platform; print(platform.python_version())'`
echo "Current python version is: " $ret

pip install brew

brew install sox
brew install portaudio

pip install librosa
pip install pyaudio
pip install dill
pip install sox

#Clone the project
git clone https://github.com/poornimaarunp/SmartAuth.git

#Navigate to the path
cd SmartAuth

# create directory bin under the SmartAuth folder
mkdir bin 
cd bin

#get the dataset from S3 bucket
wget https://s3.ap-south-1.amazonaws.com/smartauth/dataset.zip

# unzip the dataset inside bin folder
unzip dataset.zip

# quit the bin folder and come back to SmartAuth folder.
cd ..

# run the below command to complete the setup for SmartAuth
python smartauth.py -a setup -i 1

# After setup is successful use the below command to register the user. Voice over the text given
# Follow the instructions given interactively

#python smartauth.py -a register -i <<username>>

# to Authenticate the user use the below command to verify the user. Voice over the text given
# Follow the instructions given interactively

#python smarthauth.py -a authenticate -i <<username>>





