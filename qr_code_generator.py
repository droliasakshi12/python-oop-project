import qrcode

class qr():

    def code(self):

        data='https://futurevisioncomputers.com/'

        Qrcode="fvcode.png"

        qrimage=qrcode.make(data)

        qrimage.save(Qrcode)


obj=qr()
obj.code()

