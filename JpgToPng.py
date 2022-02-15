from PIL import Image
import glob
import os

JPG_list=glob.glob("./clock/Jpg_Image/*.jpg")

print(".jpgから.pngに変換開始")
for JpgName in JPG_list:
    imagefile=Image.open(JpgName)
    PngName=JpgName.replace("Jpg_Image","Png_Image")
    PngName=PngName.replace(".jpg",".png")
    imagefile.save(PngName)
    os.remove(JpgName)
    print(JpgName+"   >>>   "+PngName)
print("変換完了")