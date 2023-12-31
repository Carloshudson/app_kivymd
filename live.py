from kivymd.tools.hotreload.app import MDApp
from kivy.factory import Factory
import os

class LiveApp(MDApp):
    DEBUG = True
    
    FOREGROUND_LOCK = False
    
    KV_FILES = [
    	os.path.join(os.getcwd(), 'main.kv')
    	]
    	
    AUTORELOADER_PATHS = [
    		(".", {"recursive": True})
    		]
    	
    CLASSES = {
    		"Contatos": "main",
    	}
    	
    IDLE_DETECTION = False
    	
    IDLE_TIMEOUT = 60
    	
    RAISE_ERRROR = False
    	
    def build_app(self):
        return Factory.Contatos()
    	    
if __name__ == '__main__':
    LiveApp().run()
