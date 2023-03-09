import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )
    
    qr.add_data(text)
    qr.make(fit=True)
    image = qr.make_image(fill_color ="black",back_color ="white")
    image.save("qrimg.png")
    

text_input = input("Enter a link/text for your qrcode: ")
    
generate_qrcode(text_input)

print("\n QRcode generate succesfully in your folder")