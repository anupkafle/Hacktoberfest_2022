import img2pdf
import os
os.chdir(input("Enter The Path to The Folder Containing Images]: "))
list1 = os.listdir('.')
print(list1)
imagesList = [x for x in list1 if x.endswith(".png") or x.endswith(".jpg") or x.endswith(".jpeg")]

print(imagesList)
pdf = img2pdf.convert(imagesList)
os.chdir(input("Enter the path of the directory where you want to save the pdf: "))
with open('img1.pdf','wb') as fp:
    fp.write(pdf)

print("total no of pages is: ", len(imagesList))
