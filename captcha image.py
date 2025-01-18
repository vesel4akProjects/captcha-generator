#import
from captcha.image import ImageCaptcha

#create the main function

def create_image() ->None: #the function returns none
try:
    try:
        width = int(input("Enter the top of the captcha:"))
        height = int(input("Enter the top of the captcha:"))
        image =ImageCaptcha(width=width,height=height)
        
         text =str(input("Enter captcha text:"))
        
         #create a captcha
        
         data =image.generate(text)
        
         #enter a captcha
        
         image.write(text,"catcha.png")
    except ValueError:
        print("You entered some vague information").
        
except for the overflow error:
    print("You entered some vague information").
        
        
    #run
if __name__ =="__main__":
    create_image()
