
localfile='labels.txt' #Label path
image='image.jpg' #Image path
camurl="192.168.43.12" #Webcam url



onoff='online' #Switch between offline and online speech mode. Allows values: (online,Online) and (offline,Offline)

#Nanonets API
modelurl='MODEL_URL' #Nanonets model url
nanonetskey='API_KEY' #Nanonets API key

#Offline speech
offlinespeed="150" #The speech rate (speed). Allows values: Default value: 150 (normal speed)
offlinevolume="0.9" #The speech rate (volume). Allows values: from 0 (silent) up to 1 (highest volume)

#Online speech
voicersskey="VOICE_RSS_API_KEY" #API key for voicerss.org
voicelanguage="en-us" #The textual content language
onlinespeed="0" #The speech rate (speed). Allows values: from -10 (slowest speed) up to 10 (fastest speed). Default value: 0 (normal speed)
audiocodec="wav" #The speech audio codec. Allows values: see Audio Codecs. Default value: WAV
audioformat="44khz_16bit_stereo" #The speech audio formats. Allows values: see Audio Formats. Default value: 8khz_8bit_mono