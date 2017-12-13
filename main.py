# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 17:42:49 2017

@author: Trevor
"""

import kivy
kivy.require('1.0.9')
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty
from kivy.app import App

Builder.load_string('''
<HelloWorldScreen>:
    cols: 1
    Label:
        text: 'Welcome to the Hello World'
    Button:
        text: 'Click me! %d % root.counter
        on_release: root.my_callback()
''')
    
class HelloWorldScreen(GridLayout):
    counter = NumericProperty(0)
    def my_callback(self):
        print('The button has been pushed')
        self.counter += 1
        
class HelloWorldApp(App):
    def build(self):
        return HelloWorldScreen()
    
if __name__ == '__main__':
    HelloWorldApp().run()