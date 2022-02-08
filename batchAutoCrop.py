import os,sys
from PIL import Image

if len(sys.argv) < 8:
	print ("Usage : " + sys.argv[0] + " <folderIn> <left> <up> <right> <bottom> <folderOut> <resultsPrefix>")
	sys.exit(1)
else:
	for fileName in os.listdir(sys.argv[1]):
		extension = fileName.split('.',1)[-1]
		fileLastName = fileName.split('/',1)[-1]
		if "png" in extension or "jpg" in extension or "ppm" in extension or "pgm" in extension:
			print ("cropping " + sys.argv[1]+"/"+fileName)
			imageFile = Image.open(sys.argv[1]+"/"+fileName)
			box = (int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
			croppedImage = imageFile.crop(box)
			outputFileName = sys.argv[6]
			if outputFileName[-1] != '/' and  outputFileName[-1] != '\\':
				outputFileName = outputFileName + '/'
			outputFileName = outputFileName + sys.argv[7] + fileLastName
			croppedImage.save(outputFileName)