import threading
import teleManager
 
TOKEN = 'my token'
 
tManager = teleManager.teleManager(TOKEN)
tManagerThread = threading.Thread(target=tManager.run)
tManagerThread.start()
