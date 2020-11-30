
""" Python code to convert pdf | ppt | pptx to image and attach metadata"""

# import module 
from pdf2image import convert_from_path 
from PIL.PngImagePlugin import PngImageFile, PngInfo
import os
from comtypes import client
import uuid
import json 
import shutil
import os
import argparse

path = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))

# Input
# pdf=1
# ppt=0
# png=0

# Create output directory
if not os.path.exists('Output'):os.makedirs('Output')
    
# Create dump directory
if not os.path.exists('Dump'):os.makedirs('Dump')

# Assigning the path
inputPath_pdf=path.replace("\\","/")+r"/Input/"
outputpath_pdf=path.replace("\\","/")+r"/Output/"
dump_pdf=path.replace("\\","/")+r"/Dump/"

# inputPath_ppt=path+r"\Input/"
# outputpath_ppt=path+r"\Output/"
# dump_ppt=path+r"\Dump/"

files_pdf=[f for f in os.listdir(inputPath_pdf) if f.endswith('.' + 'pdf')]

files_image=[f for f in os.listdir(inputPath_pdf) if f.endswith('.' + 'png')]

# files_ppt=[f for f in os.listdir(inputPath_ppt) if f.endswith(('.ppt','.pptx'))]

def metadataAttacher(imagename,Exif):
    " Python function to attach the metadata in image "
    targetImage = PngImageFile(imagename)
    metadata = PngInfo()
    metadata.add_text("Title", Exif.get("Title"))  
    metadata.add_text("filename", Exif.get("filename"))
    metadata.add_text("primary_key", Exif.get("primary_key"))
    metadata.add_text("pdf_url", Exif.get("pdf_url"))
    metadata.add_text("website_url", Exif.get("website_url"))
    metadata.add_text("data_source", Exif.get("data_source"))
    metadata.add_text("date_modified", str(Exif.get("date_modified")))
    metadata.add_text("Application_Type", str(Exif.get("Application_Type")))
    targetImage.save(imagename, pnginfo=metadata)  
    print("Success") 

def main(pdf,png):
    """ PDF/PPT to image converter """
    
    pdf=pdf
    png=png

    if pdf==1:
        """ pdf to png conversion """
        for file in files_pdf:
            images = convert_from_path(inputPath_pdf+file,poppler_path = path+r'/poppler/bin') 
            for i,img in enumerate(images): 
                img.save(outputpath_pdf+os.path.splitext(os.path.basename(file))[0]+f'__{i}.png', 'PNG')
                metadataAttacher(outputpath_pdf+os.path.splitext(os.path.basename(file))[0]+f'__{i}.png',json.load(open(inputPath_pdf+os.path.splitext(os.path.basename(file))[0]+".json")))  
            shutil.move(inputPath_pdf+file,dump_pdf+file)
            shutil.move(inputPath_pdf+os.path.splitext(os.path.basename(file))[0]+".json",dump_pdf+os.path.splitext(os.path.basename(file))[0]+".json")
    
    if png==1:
        """ pdf to png conversion """
        for file in files_image:  
            metadataAttacher(inputPath_pdf+os.path.splitext(os.path.basename(file))[0]+f'.png',json.load(open(inputPath_pdf+os.path.splitext(os.path.basename(file))[0]+".json")))  
            shutil.copy(inputPath_pdf+file,outputpath_pdf+file)
            shutil.move(inputPath_pdf+file,dump_pdf+file)
            shutil.move(inputPath_pdf+os.path.splitext(os.path.basename(file))[0]+".json",dump_pdf+os.path.splitext(os.path.basename(file))[0]+".json")
    
    # if ppt==1:
    #     """ ppt to png conversion """
    #     for file in files_ppt:   
    #         powerpoint = client.CreateObject('Powerpoint.Application')
    #         powerpoint.Presentations.Open(inputPath_ppt + file)
    #         powerpoint.ActivePresentation.Export(outputpath_ppt+file, 'PNG')
    #         powerpoint.ActivePresentation.Close()
    #         powerpoint.Quit()

        # shutil.move(config.path+"./DataIn/"+file,config.path+"./DataOut/"+file)
    # 
    # print(str(uuid.uuid4()))

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('-d',"--pdf",type=int,help='to convert pdf to image and attach metadata on generated images',default=1)
    parser.add_argument('-i',"--png",type=int,help='to attach meta data on png images',default=0)
    args=parser.parse_args()
    main(pdf=args.pdf,png=args.png)
