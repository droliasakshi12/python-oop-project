<h1>PYTHON OBJECT ORIENTED PROGRAMMING🐍</h1>
<h2>Overview💡</h2>
<b><li>This includes the project related to the concept of oop in python.</li></b>
<br>
<h1>🛒Requirement</h1>
<b>Python version</b>
<br>
-Python(3.11.5)<br>
<br>
<b>IDE/Code Editor</b>
<br>
-VS Code
</br>
<br>
<h1>🖥️Tech Stack</h1>
<b>- PYTHON</b>
<br>
<h1>📑About the project</h1>
<li>The concept of  <b>object oriented programming (OOP)</b> leads to the ease of programming and in python we can use the different functions in different files by importing them.</li>
<li>The repository includes <b>5 different projects</b> based on the same concept:</li><br>
<p>
  <b>-Desktop Notification : </b> Displays the time in notification.<br>
  <b>-Emoji converter: </b> Convert the emoji into text.<br>
  <b>-Mouse clicking : </b> Clicking the mouse various times.<br> 
  <b>-qr Code Generator :</b> Generating the qr code with the link.<br>
  <b>-qr Code Decoder</b> Getting the name and link from the qr.<br>
</p>
<br>
<h1>🛠️ Prerequisites</h1>
<p><h4>To run this project, you’ll need:</h4></p>
<li>Python Package installed on your system<br></li>
<b><li>plyer package</li></b>
<b><li>Streamlit</li></b>
<b><li>demoji</li></b>
<b><li>payautogui</li></b>
<b><li>qrcode</li></b>
<b><li>cv2</li></b>
<br>
Install by running:<br>
<pre><code>pip install plyer</code></pre>
<pre><code> pip install streamlit </code></pre>
<pre><code> pip install demoji </code></pre>
<pre><code> pip install pyautogui</code></pre>
<pre><code>pip install qrcode[pil]</code></pre>
<pre><code>pip install opencv-python</code></pre>
<br>
<h1>💻Desktop Notification</h1>
<p>
  -This is a project for the notification that reflects on the desktop on a particular time.<br>
  -We have imported libraries like <b>- getpass - datatime -plyer</b><br>
  -With the use of getpass library we are getting the user name.<br>
  -Using datatime to get the present data and time when the notification is displayed.<br> 
  -Using plyer package to get the notification.<br>
</p>
<br>

<h2>👩‍💻Code - Desktop Notification App</h2>
<br>
<pre><code>
import getpass
import datetime
import streamlit as st
from plyer import notification

class n():

  def notify(self):
  
      username = getpass.getuser()
      current_time=datetime.datetime.now().strftime("%y-%m-%d,%H:%M:%S")
      
      notification.notify(
        title=f"HEY {username}",
        message=f"Have a good day ,the time is {current_time}",
        app_name='Desktop Notifier',
        timeout=20
             )          
obj=n()
obj.notify()
</code></pre>
<br>
<h1>😊Emoji Converter</h1>
<p>
  😎-This program helps to convert the emoji into the text name of that particular emoji.<br>
  😎-Using the demoji module to perform the program.
</p>
<br>
<h2>👩‍💻Code - Emoji Converter</h2>
<br>

<pre><<code>
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
</code></pre>


<br>
<h1>🖱️Mouse Clicking</h1>
<p>
  -In mouse clicking program we just have to hover the mouse and it will be automatically clicked the number of times it is mentioned.<br>
  -hover the cursor on the icon we need to open and it will start the app.
</p><br>

<h2>👩‍💻Code - Mouse Clicking</h2>
<pre><code>
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
</code></pre>

<br>
<h1>🔗qr Code Generator</h1>
<p>
  -This project is to generate the qr code.<br>
  -We have to insert the link for the website or any other platforms for which the qr code is to be generated.
</p>
<br>
<h2>👩‍💻Code - qr Code Generator</h2>
<pre><code>
  import qrcode

class qr():

    def code(self):
    
        data='https://futurevisioncomputers.com/'
        Qrcode="fvcode.png"
        qrimage=qrcode.make(data)
        qrimage.save(Qrcode)
        
obj=qr()
obj.code()
</code></pre>
<br>
<h1>🔗qr code decoder</h1>
<p>
  -This helps in decoding the qe code.
  -In this project the qr code is given it helps to get the link for the qrcode.
</p>
<h2>👩‍💻Code - qr Code Decoder</h2>
<pre><code>
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
</code></pre>
<br>
<b><p>⭐ If you found this repository useful, consider giving it a star!</p>
  <p>Happy Coding 🐍✨</p></b>
<br>
👤 Github  : [@droliasakshi12](https://github.com/droliasakshi12)<br>
📩 Email   : sakshidrolia12@gmail.com <br>
🔗 Linkdin : https://www.linkedin.com/in/sakshi-drolia12<br>
</br>
<h4>Credits</h4>
<b></b>Future Vision Computer Institute</b><br>
🌐 Website : https://futurevisioncomputers.com/
<br>
<b><h5>Author</h5></b>
<h6><b>Sakshi Drolia</b></h6>
