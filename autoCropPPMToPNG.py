import os
import sys
from PIL import Image
import threading

cropping_request = False
renaming_request = False


class ProcessingThread(threading.Thread):
    def __init__(
        self,
            fileToProcess: str,
            box: (int, int, int, int),
            prefix: str):
        """  """
        super(ProcessingThread, self).__init__()
        self.fileToProcess = fileToProcess
        self.box = box
        self.prefix = prefix

    def run(self):
        filelastName = self.fileToProcess.split('/', 1)[-1]
        imageFile = Image.open(self.fileToProcess)
        newImage = imageFile

        if self.box is not None:
            newImage = imageFile.crop(self.box)

        # Vertical mirror image
        pixels = newImage.load()
        height = newImage.size[1]
        for y in range(height // 2):
            for x in range(newImage.size[0]):
                temp = pixels[x, y]
                pixels[x, y] = pixels[x, height - 1 - y]
                pixels[x, height - 1 - y] = temp

        outputFileName = sys.argv[2]
        if outputFileName[-1] != '/' and\
           outputFileName[-1] != '\\':
                outputFileName = outputFileName + '/'
        filelastName_noExt = filelastName.split('.', 1)[0]
        if self.prefix is not None:
            outputFileName =\
                outputFileName + self.prefix + filelastName_noExt + ".png"
        else:
            outputFileName = outputFileName + filelastName_noExt + ".png"
        print("Saving " + outputFileName)
        newImage.save(outputFileName)


def processOnImage(filename: str, box: (int, int, int, int), prefix: str):
    """ Process the image filename and save it
    Keyword arguments:
    filename -- string that contains the path of the file
    box -- if not None, crop the original image before mirroring
    prefix -- if not None, prefix the result
    """
    filelastName = filename.split('/', 1)[-1]
    imageFile = Image.open(filename)
    newImage = imageFile

    if box is not None:
        newImage = imageFile.crop(box)

    # Vertical mirror image
    pixels = newImage.load()
    height = newImage.size[1]
    for y in range(height // 2):
        for x in range(newImage.size[0]):
            temp = pixels[x, y]
            pixels[x, y] = pixels[x, height - 1 - y]
            pixels[x, height - 1 - y] = temp

    outputFileName = sys.argv[2]
    if outputFileName[-1] != '/' and\
       outputFileName[-1] != '\\':
            outputFileName = outputFileName + '/'
    filelastName_noExt = filelastName.split('.', 1)[0]
    if prefix is not None:
        outputFileName =\
            outputFileName + sys.argv[3] + filelastName_noExt + ".png"
    else:
        outputFileName = outputFileName + filelastName_noExt + ".png"
    print("Saving " + outputFileName)
    newImage.save(outputFileName)
# End of processOnImage

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(
            "Usage : " + sys.argv[0] +
            " <folderIn> <folderOut> " +
            " [<resultsPrefix> <left> <up> <width> <height>]")
        sys.exit(1)
    else:
        box = None
        prefix = None
        if len(sys.argv) > 3:
            renaming_request = True
            print("png files will be prefixed with " + sys.argv[3])
            prefix = sys.argv[3]
        if len(sys.argv) > 4:
            cropping_request = True
            if len(sys.argv) < 8:
                print(
                    "Cropping request failed," +
                    "treatment wil continue without cropping")
                print(
                    "Usage : " +
                    sys.argv[0] +
                    " <folderIn> <folderOut>" +
                    " [<resultsPrefix> <left> <up> <width> <height>]")
                cropping_request = False
            else:
                print(
                    "Cropping images from coord x: " + sys.argv[4] +
                    " and y: " + sys.argv[5] +
                    " with dimension w: " + sys.argv[6] +
                    " and h: " + sys.argv[7])
                box = (
                    int(sys.argv[4]),
                    int(sys.argv[5]),
                    int(sys.argv[4]) + int(sys.argv[6]),
                    int(sys.argv[5]) + int(sys.argv[7]))

        fileList = []
        filePath = sys.argv[1]
        if filePath[-1] != '/' and\
                filePath[-1] != '\\':
                filePath = filePath + "/"

        for fileName in os.listdir(sys.argv[1]):
            extension = fileName.split('.', 1)[-1]
    #       fileLastName = fileName.split('/', 1)[-1]
            if "png" in extension or\
               "jpg" in extension or\
               "ppm" in extension or\
               "pgm" in extension:
                fileList.append(filePath + fileName)
                processOnImage(fileList[-1], box, prefix)

        try:
            threads = []
            for file in fileList:
                threads.append(ProcessingThread(file, box, prefix))
                threads[-1].start()
                # limiting the concurrent thread number
                if len(threads) == 8:
                    for t in threads:
                        t.join()
                    while len(threads) > 0:
                        threads.pop()
        except KeyboardInterrupt:
            # stop threading
            for t in threads:
                t.join()
            while len(threads) > 0:
                threads.pop()
#        with Pool(8) as p:
#            try:  # Merci stack overflow
#                p.map(processOnImage, fileList)
#            except KeyboardInterrupt:
#                p.terminate()
#                print("Program Cancelled")
#                sys.exit(1)
