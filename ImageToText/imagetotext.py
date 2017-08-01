from PIL import Image
import subprocess
def cleanFile(filepath,newfile):
    image=Image.open(filepath)
    image=image.point(lambda x:0 if x<143 else 255)
    image.save(newfile)
    subprocess.call(["tesseract",newfile,"output"])
    outputfile=open("output.txt","r")
    print(outputfile.read())
    outputfile.close()
if __name__=="__main__":
    cleanFile("F:image/1.jpg", "F:image/2.jpg")