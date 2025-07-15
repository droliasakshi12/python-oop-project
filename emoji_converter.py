import demoji


class converter():
    def __init__(self):
        demoji.download_codes()
    
    def convert(self):
        text="😀😂😁😃🎅👍✌"
        return demoji.findall(text)

if __name__=="__main__":
    obj=converter()
    d=obj.convert()
    print(d)
