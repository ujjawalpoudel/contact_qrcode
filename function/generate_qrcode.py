import vobject
import qrcode

from utils import vcf_generator, qrcode_generator
from current_directory import dir_path


def generate_qrcode_main(personal):
    """

    Args:
        personal (dict): Input parameters

    Returns:
        dict: {
            msg: Appropriate message related to operation
            status: Boolean
            image_path: Path of qr code where it is stored
        }
    """
    response_data = {}
    try:
        status, msg, serialize_data, path = vcf_generator(personal)

        if status:
            status, msg, image_path = qrcode_generator(serialize_data, path)
            response_data["image_path"] = image_path

    except Exception as e:
        msg = str(e)
        status = False
        print("Error: " + msg)

    response_data["msg"] = msg
    response_data["status"] = status
    return response_data
