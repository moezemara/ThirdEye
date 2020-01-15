# ThirdEye
Smart glasses that use a webcam and internet connection to bring assistance to people with a visual impairment. In this case, however, what you're connected to is a trained assistant who provides spoken feedback about what you are looking at. Useful for help with identifying objects, reading documents, menus or medication.


# Features
  * Object Detection (Nanonets API)
  * OCR for text reading (Tesseract)
  * Distances detection (x2 UltraSonics)
  * Text to speech 
    * Online (Voicerss)
    * Offline (Pyttsx3)
 
# Materials
  * RaspberryPi
  * x2 Ultrasonics
  * Speaker (Headphones - Earphones or Bluetooth devices)

# Installations

### **Software part**

Clone this repository to your Raspberrypi

```
git clone https://github.com/moezemara/ThirdEye
```

Head to the cloned directory and install the requirements

```
pip3 install -r requirements.txt
```

Now we need to install some essintial softwares

```
sudo apt-get install espeak
```

```
sudo apt-get install tesseract-ocr
```

```
sudo apt-get install libtesseract-dev
```

Now you will need to train your own object model ```https://nanonets.com/```

After finishing model training grap your api key and url and put them in ```config.py```

To access online voice service you need to create account on ```http://www.voicerss.org/``` allowing only 350 free daily request, grap your voicerss key place it into ```config.py```

### **Hardware Part**

Download webcam application from playstore 

```
https://play.google.com/store/apps/details?id=com.pas.webcam
```
Connect your phone to raspberrypi's same network

Open the app, start server and grap the camera ip

Place that ip into your ```config.py```

Connect your Ultrasonics triggers to GPIOs 12,18 and ECHO's to 16,22

**NOTE: GPIOs on board not BCM you can use ```https://pinout.xyz/``` as reference**

# Configurations

You can always switch bettween online and offline speech mode using ```onoff```  **Online's sound is better but its too slow and limited**

* **Allowed online speech langauges**

| Language code | Language name           |
|---------------|-------------------------|
| ca-es         | Catalan                 |
| zh-cn         | Chinese (China)         |
| zh-hk         | Chinese (Hong Kong)     |
| zh-tw         | Chinese (Taiwan)        |
| da-dk         | Danish                  |
| nl-nl         | Dutch                   |
| en-au         | English (Australia)     |
| en-ca         | English (Canada)        |
| en-gb         | English (Great Britain) |
| en-in         | English (India)         |
| en-us         | English (United States) |
| fi-fi         | Finnish                 |
| fr-ca         | French (Canada)         |
| fr-fr         | French (France)         |
| de-de         | German                  |
| it-it         | Italian                 |
| ja-jp         | Japanese                |
| ko-kr         | Korean                  |
| nb-no         | Norwegian               |
| pl-pl         | Polish                  |
| pt-br         | Portuguese (Brazil)     |
| pt-pt         | Portuguese (Portugal)   |
| ru-ru         | Russian                 |
| es-mx         | Spanish (Mexico)        |
| es-es         | Spanish (Spain)         |
| sv-se         | Swedish (Sweden)        |

* **Allowed audio codecs**

| Audio codec |
|-------------|
| MP3         |
| WAV         |
| AAC         |
| OGG         |
| CAF         |

* **Allowed audio formats**

| Audio format code  | Audio format description |
|--------------------|--------------------------|
| 8khz_8bit_mono     | 8 kHz, 8 Bit, Mono       |
| 8khz_8bit_stereo   | 8 kHz, 8 Bit, Stereo     |
| 8khz_16bit_mono    | 8 kHz, 16 Bit, Mono      |
| 8khz_16bit_stereo  | 8 kHz, 16 Bit, Stereo    |
| 11khz_8bit_mono    | 11 kHz, 8 Bit, Mono      |
| 11khz_8bit_stereo  | 11 kHz, 8 Bit, Stereo    |
| 11khz_16bit_mono   | 11 kHz, 16 Bit, Mono     |
| 11khz_16bit_stereo | 11 kHz, 16 Bit, Stereo   |
| 12khz_8bit_mono    | 12 kHz, 8 Bit, Mono      |
| 12khz_8bit_stereo  | 12 kHz, 8 Bit, Stereo    |
| 12khz_16bit_mono   | 12 kHz, 16 Bit, Mono     |
| 12khz_16bit_stereo | 12 kHz, 16 Bit, Stereo   |
| 16khz_8bit_mono    | 16 kHz, 8 Bit, Mono      |
| 16khz_8bit_stereo  | 16 kHz, 8 Bit, Stereo    |
| 16khz_16bit_mono   | 16 kHz, 16 Bit, Mono     |
| 16khz_16bit_stereo | 16 kHz, 16 Bit, Stereo   |
| 22khz_8bit_mono    | 22 kHz, 8 Bit, Mono      |
| 22khz_8bit_stereo  | 22 kHz, 8 Bit, Stereo    |
| 22khz_16bit_mono   | 22 kHz, 16 Bit, Mono     |
| 22khz_16bit_stereo | 22 kHz, 16 Bit, Stereo   |
| 24khz_8bit_mono    | 24 kHz, 8 Bit, Mono      |
| 24khz_8bit_stereo  | 24 kHz, 8 Bit, Stereo    |
| 24khz_16bit_mono   | 24 kHz, 16 Bit, Mono     |
| 24khz_16bit_stereo | 24 kHz, 16 Bit, Stereo   |
| 32khz_8bit_mono    | 32 kHz, 8 Bit, Mono      |
| 32khz_8bit_stereo  | 32 kHz, 8 Bit, Stereo    |
| 32khz_16bit_mono   | 32 kHz, 16 Bit, Mono     |
| 32khz_16bit_stereo | 32 kHz, 16 Bit, Stereo   |
| 44khz_8bit_mono    | 44 kHz, 8 Bit, Mono      |
| 44khz_8bit_stereo  | 44 kHz, 8 Bit, Stereo    |
| 44khz_16bit_mono   | 44 kHz, 16 Bit, Mono     |
| 44khz_16bit_stereo | 44 kHz, 16 Bit, Stereo   |
| 48khz_8bit_mono    | 48 kHz, 8 Bit, Mono      |
| 48khz_8bit_stereo  | 48 kHz, 8 Bit, Stereo    |
| 48khz_16bit_mono   | 48 kHz, 16 Bit, Mono     |
| 48khz_16bit_stereo | 48 kHz, 16 Bit, Stereo   |
| alaw_8khz_mono     | ALaw, 8 kHz, Mono        |
| alaw_8khz_stereo   | ALaw, 8 kHz, Stereo      |
| alaw_11khz_mono    | ALaw, 11 kHz, Mono       |
| alaw_11khz_stereo  | ALaw, 11 kHz, Stereo     |
| alaw_22khz_mono    | ALaw, 22 kHz, Mono       |
| alaw_22khz_stereo  | ALaw, 22 kHz, Stereo     |
| alaw_44khz_mono    | ALaw, 44 kHz, Mono       |
| alaw_44khz_stereo  | ALaw, 44 kHz, Stereo     |
| ulaw_8khz_mono     | uLaw, 8 kHz, Mono        |
| ulaw_8khz_stereo   | uLaw, 8 kHz, Stereo      |
| ulaw_11khz_mono    | uLaw, 11 kHz, Mono       |
| ulaw_11khz_stereo  | uLaw, 11 kHz, Stereo     |
| ulaw_22khz_mono    | uLaw, 22 kHz, Mono       |
| ulaw_22khz_stereo  | uLaw, 22 kHz, Stereo     |
| ulaw_44khz_mono    | uLaw, 44 kHz, Mono       |
| ulaw_44khz_stereo  | uLaw, 44 kHz, Stereo     |

# Errors you may face

if you are connecting raspberrypi through ssh you might face some sort of displaying error

```
export DISPLAY=:0.0
```

Its very recommended that you run this project from virtual enviroment to avoid any packages errors

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
