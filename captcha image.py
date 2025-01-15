
#import
from captcha.image import ImageCaptcha

#create main function

def create_image() ->None: #function return none
    try:
        try:
            width = int(input("Введите ширину капчи:"))
            height = int(input("Введите высоту капчи:"))
            image =ImageCaptcha(width=width,height=height)

            text =str(input("Введите текст капчи:"))

            #create captcha

            data =image.generate(text)

            #write captcha

            image.write(text,"catcha.png")
        except ValueError:
            print("Вы ввели неконкретные данные")
            return

    except OverflowError:
        print("Вы ввели неконкретные данные")
        return

#launch
if __name__ == "__main__":
    create_image()