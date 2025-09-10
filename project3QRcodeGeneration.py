# import the library  
import qrcode

# from PIL import Imagedata to b eencoded
data="https://youtu.be/EZkrUx9OSC0?si=tG-ZegGWt8g43icz"
# create qrcode object with setting
qr= qrcode.QRCode(
    version=1,    #size=1
    error_correction=qrcode.constants.ERROR_CORRECT_H,  #higher correction code means qrcode can be scan if their is any error
    box_size=10,  #how many pixel each square will have
    border=4,   #thickness of white border around QR
)
qr.add_data(data)  #add the URL in QRcode object
qr.make(fit=True)   #ensure the qrcode size fits automatically
img=qr.make_image(fill_color="black",back_color="white")#generates qrocde as an image
img.save("qrcode.png")  #save teh qrcode in the folder
img.show()  #show the qrcode img in folder