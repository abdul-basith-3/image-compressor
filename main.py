from PIL import Image
import os
def compressor(file):
    filepath = os.path.join(os.getcwd(),file)
    picure = Image.open(filepath)
    picure.save("compressed_"+file,"JPEG",optimize=True,quality=10)
def main():
    cwd = os.getcwd()
    format = ('.jpeg','.jpg')
    for file in os.listdir(cwd):
        if os.path.splitext(file)[1].lower() in format:
            print("success")
            compressor(file)
if __name__ == "__main__":
    main()