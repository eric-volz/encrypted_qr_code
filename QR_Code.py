from qrcode import QRCode
from qrcode import constants


class QR_Code:

    @staticmethod
    def save_to_qr_code(text: str):
        qr = QRCode(version=1, error_correction=constants.ERROR_CORRECT_H, box_size=20, border=4)
        qr.add_data(text)
        qr.make(fit=True)

        return qr.make_image()
