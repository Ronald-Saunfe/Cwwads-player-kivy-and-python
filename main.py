import os
import kivy
from kivy.config import Config
Config.set('graphics', 'borderless', '1')
Config.set('graphics', 'resizable', 'False')
#ronald

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, ObjectProperty,\
     NumericProperty, ListProperty, OptionProperty, BooleanProperty
from kivy.uix.behaviors import ButtonBehavior, ToggleButtonBehavior
from kivy.animation import Animation

from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from touchripple import TouchRippleButtonBehavior, TouchRippleBehavior

from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, NoTransition, CardTransition,\
                                        FadeTransition
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse,\
                          Rectangle, RoundedRectangle, SmoothLine, Line

from kivy.graphics.texture import Texture

from kivy.core.text import Label as CoreLabel
from kivy.uix.modalview import ModalView
from kivy.clock import mainthread
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.video import Video
from kivy.uix.stencilview import StencilView
from kivy.uix.scrollview import ScrollView

from functools import partial
import threading
import socket
import re
import pickle
import random
import datetime
import queue
from threading import Thread, Event
from multiprocessing.pool import ThreadPool
import time
import ast
import os
import cv2
import numpy as np
from subprocess import Popen, PIPE
import subprocess
import ffmpeg
from decimal import Decimal

from widgets.BoxLayout_animation import *
from widgets.Buttons import *
from widgets.Cards import *
from widgets.Dialogs import *
from widgets.Labels import *
from widgets.Loading import *
from widgets.ShowcaseL import *
from widgets.TextFields import *
from widgets.PaginationLayout import Paginating_BoxLayout
from HoverBehavior import HoverBehavior
from ctypes import windll, Structure, c_long, byref


Window.size= (800, 600)
class CustomScrollView(ScrollView):
    def __init__(self, **kwargs):
        super(CustomScrollView, self).__init__(**kwargs)

        # get app instance to add function from widget
        app = App.get_running_app()

        # add function to the list
        app.drops.append(self.on_dropfile)

        self.counter =0 

    def on_dropfile(self, widget, filename):
        # a function catching a dropped file
        # if it's dropped in the widget's area
        print(filename)
        if self.collide_point(*Window.mouse_pos):
            # on_dropfile's filename is bytes (py3)
            path = filename.decode('utf-8')
            self.add_video(path)


    def add_video(self, filepath,*args):
        #check extension of the file
        if filepath.endswith(".wmv"):
            file = filepath[:filepath.rfind('/')]
            vid = Video_Widget(source = filepath,\
                               name = file,\
                               duration = '-')

            #read a frame for the video
            vidcap = cv2.VideoCapture(filepath)
            amount_of_frames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
            if int(amount_of_frames)!=0:
                frame_number = random.randrange(int(amount_of_frames)-1)
            else:
                frame_number = (amount_of_frames)
            vidcap.set(1, frame_number)
            
            res, frame = vidcap.read()
            
            success,image = vidcap.read()
            while success:
              cv2.imwrite("mime\\frame%s.jpg"%self.counter, image)     # save frame as JPEG file      
              success,image = vidcap.read()
              break

            vid.mime = "mime\\frame%s.jpg"%self.counter

            vid.bind(on_press=partial(self.parent.show_video, "mime\\frame%s.jpg"%self.counter,\
                                      filepath, file, vid))

            self.parent.ids.grid.add_widget(vid)

            self.counter +=1
               
    
class Toolbar_up(BoxLayout):
    title = StringProperty()

class Toolbar_down(BoxLayout):
    duration = StringProperty()

class BaseVideo(HoverBehavior, FloatLayout):
    pass

class CvideoPlayer(BaseVideo, Video, StencilView):
    elevation = StringProperty('6')
    title = StringProperty('')

    def __init__(self, fps=0, **kwargs):
        super(CvideoPlayer, self).__init__(**kwargs)

    def on_enter(self):
        anim = Animation(y=self.y+self.height-self.ids.toolb_up.height,t='out_cubic',\
                         duration=.3)
        anim.start(self.ids.toolb_up)

        anim = Animation(y=self.y,t='out_cubic',duration=.3)
        anim.start(self.ids.toolb_down)
        
    def on_leave(self):
        anim = Animation(y=self.y+self.height,t='in_cubic',duration=.3)
        anim.start(self.ids.toolb_up)

        anim = Animation(y=self.y-self.height,t='in_cubic',duration=.3)
        anim.start(self.ids.toolb_down)

        
class CustomDropdown(DropDown):
    pass

class LabelMenu(ToggleButtonBehavior,Label):

    def on_state(self, inst, value):
        if value =='down':
            self.color =(0,245/255,1,1)
        else:
            self.color = (1,1,1,1)
            

class Video_Widget(ButtonBehavior, BoxLayout):
    mime = StringProperty()
    source = StringProperty()
    name = StringProperty('')
    duration = StringProperty('')


class SearchText(BoxLayout):
    pass


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]



def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}


class CustomBoxLayout(BoxLayout):

    def on_touch_down(self, touch):
        pos = queryMousePosition()
        self.current_pos = pos
        
        return super(CustomBoxLayout,self).on_touch_down(touch)

    def on_touch_move(self, touch):
        pos = queryMousePosition()
        change_pos_x = pos['x'] - self.current_pos['x']
        change_pos_y = pos['y'] - self.current_pos['y']
        
        Window.top += change_pos_y
        Window.left += change_pos_x

        self.current_pos = pos
        
        return super(CustomBoxLayout,self).on_touch_move(touch)
    

class Pipvideo(VideoPlayer):
    bg_img = StringProperty()
    source = StringProperty()

class ButtonBack(BoxLayout):
    title = StringProperty()

class Body(FloatLayout, StencilView):
    bg_path = StringProperty('frame.jpg')
    
    def __init__(self, **kwargs):
        super(Body, self).__init__(**kwargs)

        self.ids.player.options =  {'allow_stretch': False}
        self.ids.player.ids.toolb_up.ids.close.bind(on_release=self.unShowPlayer)

        self.ids.player.y = self.y -dp(1)
        self.ids.player.size =dp(1), dp(1)

    def unShowPlayer(self, *args):
        anim = Animation(x=0,\
                         y=0,\
                         width=Window.width/2,\
                         height = Window.height-dp(60),\
                         duration = .3,\
                         t='in_circ')
        anim.start(self.ids.player)

        anim2 = Animation(x=Window.width/2,\
                          y=0,\
                          width = Window.width,\
                          height = Window.height-dp(60),\
                          duration = .3,\
                          t='in_circ')

        anim2.start(self.ids.csrllv)
        self.ids.grid.cols =int((Window.width/2)/dp(250))
    
    def show_menu(self):
        self.dropdown = CustomDropdown()
        self.dropdown.dismiss_on_select=True
        self.dropdown.size_hint_x=None
        self.dropdown.width =dp(100)

        self.dropdown.add_widget(Button(size_hint_y=None, height=dp(30),
                                        text='Switch off'))

        self.dropdown.open(self.ids.lbl_menu)
        

    def show_video(self, bg_img, source, title, vid,*args):
        self.export_to_png('bg_img.png')
        img = cv2.imread('bg_img.png')  
  
        # make sure that you have saved it in the same folder 
        # You can change the kernel size as you want
        blurImg = cv2.blur(img,(30,30))
        cv2.imwrite('bg_img.png',blurImg)

        #set position on start anim
        #self.ids.player.pos = vid.pos
        #self.ids.player.size = vid.size

        #display animation
        anim = Animation(x = dp(16),\
                         y = Window.height*1/8,\
                         size = ( Window.width-dp(32), Window.height*(3/4)),\
                         duration = .3,\
                         t='out_circ')
        anim.start(self.ids.player)
        
        anim.bind(on_complete = lambda *x: setattr(self.ids.player, 'source', source) )
        anim.bind(on_complete = lambda *x: setattr(self.ids.player, 'state', 'play') )
        anim.bind(on_complete = lambda *x: setattr(self.ids.player, 'title', title) )
    
        anim2 = Animation(x=0,\
                          y=0,\
                          width = Window.width,\
                          height = Window.height-dp(60),\
                          duration = .3,\
                          t='in_circ')
        anim.bind(on_complete = lambda *x: anim2.start(self.ids.csrllv))
        self.ids.grid.cols =int(Window.width/dp(250))
        
class MainApp(App):
    
    def build(self):
        # set an empty list that will be later populated
        # with functions from widgets themselves
        self.drops = []

         # bind handling function to 'on_dropfile'
        Window.bind(on_dropfile=self.handledrops)
        
        self.body= Body()
        return self.body

    def handledrops(self, *args):
        # this will execute each function from list with arguments from
        # Window.on_dropfile
        #
        # make sure `Window.on_dropfile` works on your system first,
        # otherwise the example won't work at all
        for func in self.drops:
            func(*args)
    
if __name__=='__main__':
    MainApp().run()
    
    
