# install pillow 
# import pillow 
# open up the image we want to resize usinmg python 
# print the current size of that image
# specify the size we wanna change it to 
# save the new resized image 

from PIL import Image 
def resize_image(size1, size2):
    image = Image.open('Tulips.jpg')

    print(f"Current Size of the Image is: {image.size}")

    resized_image = image.resize((size1, size2))

    resized_image.save('Tulips' + str(size1) + '.jpeg') 

size1 = int(input("Enter the length: "))
size2 = int(input("Enter the width: "))
resize_image(size1, size2)
