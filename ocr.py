try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import urllib
import requests
import config

def run():
	url = "http://"+config.camurl+":8080/shot.jpg"
	urllib.request.urlretrieve(url, config.image)

	output_file=open(config.localfile,'w')

	def ocr_core(filename):
	    text = pytesseract.image_to_string(Image.open(filename))
	    return text


	text = ocr_core(config.image)
	print(text)
	output_file.writelines(text)
	output_file.close()