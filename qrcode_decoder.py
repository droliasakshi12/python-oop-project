import cv2

class decode():
    def qrdecode(self):

        file="fvcode.png"

        image=cv2.imread(file)

        detector=cv2.QRCodeDetector()

        data,vertices_array,binary_qrcode=detector.detectAndDecode(image)

        if vertices_array is not None:
            print("QR code:")
            print(data)

        else:
            print("there is some error")

obj=decode()
obj.qrdecode()