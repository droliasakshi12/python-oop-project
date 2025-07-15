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

