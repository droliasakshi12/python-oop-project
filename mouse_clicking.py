import pyautogui

class clicking():
    def __init__(self,time):
        self.time=time
        self.on_click=0
    
    def click(self):
       while self.on_click<self.time:
            self.on_click+=1
            pyautogui.leftClick()
       print("stopped clicking")
    

if __name__=="__main__":
    time=10
    obj=clicking(time)
    obj.click()

    