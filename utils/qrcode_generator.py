import qrcode


def qrcode_generator(data, path):
    """
    Returns image path of qr code after generation.
    Args:
        data (str): string format of VCF object
        path (str): path where image is going to be stored

    Returns:
        boolean: True/False
        str: message related to success or failure
        str: project_directory/image.png
    """
    try:
        # Creating an instance of qrcode
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")

        qrcode_path = path + ".png"
        img.save(qrcode_path)
        status = True
        msg = "QR code generate successfully."
        image_path = qrcode_path
    except Exception as err:
        print("Error saving QR Code", err)
        status = False
        msg = "Error generating QR Code " + err
        image_path = None
    return status, msg, image_path
