import pyqrcode
import os
import time

# global variables

global qr_code_type
global qr_code_scale_value

os.system('color 2')

print('#####################################################\n'
      '# QR Code Creater                                 #\n'
      '# version: (beta) v0.2                              #\n'
      '# release date: 30.03.2020                          #\n'
      '# @author: yusuf                                    #\n'
      '# docs: https://yusufbilgin.de/pyprojects/qrcreater #\n'
      '#####################################################')
print(' ')

while(True):

    print("1) SVG\n2) EPS\n3) PNG")

    user_input_is_int = False

    while (not user_input_is_int):
        try:
            qr_code_type = int(input("Select a image format: "))
            user_input_is_int = True
        except:
            print("Enter a number between 1 - 3 !!!")

    user_input_is_int = False

    user_input = input("Enter your data which do you want to save: ")
    qr_code_file_name = input("Enter file name: ")

    while (not user_input_is_int):
        try:
            qr_code_scale_value = int(input("Enter QR Code image scale\n"
                                            " Enter a number between 1 - 10:"))
            user_input_is_int = True
        except:
            print("Enter a number between 1 - 10!!!")



    qr_code = pyqrcode.create(user_input)


    # create svg file

    if qr_code_type == 1:
        print("In what color should the qr code be created? \n"
              "1) Black\n"
              "2) Blue\n"
              "3) Red\n"
              "4) Yellow\n"
              "5) Brown\n"
              "6) Pink\n"
              "7) Purple\n"
              "8) Green ")
        user_selected_color = input("Enter the name or the number of the color: ")
        print("Background color is set by default to white!")
        if (user_selected_color == "1" or "Black" or "black") == True:
            color = "#000"
        elif (user_selected_color == "2" or "Blue" or "blue") == True:
            color = "#00f"
        elif (user_selected_color == "3" or "Red" or "red") == True:
            color = "#f00"
        elif (user_selected_color == "4" or "Yellow" or "yellow") == True:
            color = "#ff0"
        elif (user_selected_color == "5" or "Brown" or "brown") == True:
            color = "#630"
        elif (user_selected_color == "6" or "Pink" or "pink") == True:
            color = "#f3c"
        elif (user_selected_color == "7" or "Purple" or "purple") == True:
            color = "#660066"
        elif (user_selected_color == "8" or "Green" or "green") == True:
            color = "#009900"

        print("QR code created ...")
        time.sleep(2)
        print("...")
        time.sleep(1)
        print("..")
        qr_code.svg(qr_code_file_name+".svg", scale=qr_code_scale_value, module_color=color)
        time.sleep(1)
        print(".......")
        time.sleep(1)
        print("QR Code ready!\n"
              "..\n"
              "QR Code Successfully Generated!")

        print("Generate Date: " + time.ctime())


    # create eps file

    elif qr_code_type == 2:
        print("QR code created ...")
        time.sleep(2)
        print("...")
        time.sleep(1)
        print("..")
        qr_code.eps(qr_code_file_name+".eps", scale=qr_code_scale_value)
        time.sleep(1)
        print(".......")
        time.sleep(1)
        print("QR Code ready\n"
              "..\n"
              "QR Code Successfully Generated!")

        print(" Generate Date: " + time.ctime())


    # create png file

    elif qr_code_type == 3:
        print("In what color should the QR code be created? \n"
              "1) Black\n"
              "2) Blue\n"
              "3) Red\n"
              "4) Yellow\n"
              "5) Brown\n"
              "6) Pink\n"
              "7) Purple\n"
              "8) Green")
        user_selected_color = input("Enter the name or the number of the color: ")
        print("Background color is set by default to white!")
        if (user_selected_color == "1" or "Black" or "black") == True:
            a, b, c = 0, 0, 0
        elif (user_selected_color == "2" or "Blue" or "blue") == True:
            a, b, c = 0, 0, 255
        elif (user_selected_color == "3" or "Red" or "red") == True:
            a, b, c = 255, 0, 0
        elif (user_selected_color == "4" or "Yellow" or "yellow") == True:
            a, b, c = 255, 255, 0
        elif (user_selected_color == "5" or "Brown" or "brown") == True:
            a, b, c = 102, 51, 0
        elif (user_selected_color == "6" or "Pink" or "pink") == True:
            a, b, c = 255, 51, 204
        elif (user_selected_color == "7" or "Purple" or "purple") == True:
            a, b, c = 102, 0, 102
        elif (user_selected_color == "8" or "Green" or "green") == True:
            a, b, c = 0, 153, 0

        print("QR code created ...")
        time.sleep(2)
        print("...")
        time.sleep(1)
        print("..")
        qr_code.png(qr_code_file_name+".png", scale=qr_code_scale_value, module_color=(a, b, c, 255), background=(255, 255, 255, 255))
        time.sleep(1)
        print(".......")
        time.sleep(1)
        print("QR Code ready!\n"
              "..\n"
              "QR Code Successfully Generated!")

        print("Generate Date: " + time.ctime())

    print('  ')
    print("1) Exit\n"
          "2) Generate again QR Code")
    global h
    h = True
    while h:
        try:
            global do_you_want_close
            do_you_want_close = int(input("..:"))
            if (do_you_want_close == 1 or 2) == True:
                h = False
            elif do_you_want_close == 2:
                h = False
        except:
            print("Enter for exit 1, for continue 2 !!!")

    if do_you_want_close == 1:
        break

