import os
from os import listdir
from PIL import Image
count=0
for filename in os.listdir('/Users/ajinkyabobade/Downloads/2/'):
    if filename.upper().endswith('.JPG'):
     try:
         img = Image.open('/Users/ajinkyabobade/Downloads/2/' + filename)
         img.verify()
     except(IOError,SyntaxError)as e:
         print('Bad file  :  '+filename)
         count=count+1
         print(count)

#file_count=len(filename)
#print(file_count)
