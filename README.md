<h1>✏️PYTHON OBJECT ORIENTED PROGRAMMING</h1>
<li>This includes the project related to the concept of oop in python.</li>
<br>
<h2>📑About the project</h2>
<li>The concept of oop leads to the ease of programming and in python we can use the different functions in different files by importing them.</li>
<li>The repository includes <b>5 different projects</b> based on the same concept:</li><br>
<p>
  <b>-Desktop Notification : </b> Displays the time in notification.<br>
  <b>-Emoji converter: </b> Convert the emoji into text.<br>
  <b>-Mouse clicking : </b> Clicking the mouse various times.<br> 
  <b>-qr Code Generator :</b> Generating the qr code with the link.<br>
  <b>-qr Code Decoder</b> Getting the name and link from the qr.<br>
</p>
<br>
<h2>🛠️ Prerequisites</h2>
<p><h4>To run this project, you’ll need:</h4></p>
<li>Python installed on your system<br></li>
<b><li>plyer package</li></b>
<br>
Install by running:<br>
<pre><code>pip install plyer</code></pre>
<b><li>Streamlit</li></b>
<pre><code> pip install streamlit </code></pre>

<h2>👩‍💻Code - Desktop Notification App</h2>

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



