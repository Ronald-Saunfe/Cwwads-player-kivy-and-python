from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.animation import Animation
from kivy.clock import Clock
import random

Builder.load_string('''

<Loading_widget>:
    size_hint: None, None
    orientation: 'vertical'
    spacing: dp(8)
    
    Loading_widget_progress:
        size: dp(64), dp(64)
        pos_hint: {'center_x':.5,'center_y':.5}
        
    MDLabel:
        text: root.text
        halign: 'center'
        color: root.color

<Loading_widget_progress>:
    canvas:
        Color:
            rgba: 1,1,1,1

        SmoothLine:
            width: 1
            ellipse: self.x + self.width/4, self.y + self.height/4, self.width/2, self.height/2
                        
        Color:
            rgba: root.anim_color

        SmoothLine:
            group: 'a'
            width: 2
            ellipse: self.x + self.width/4, self.y + self.height/4, self.width/2, self.height/2, root.angle_start,root.angle_end
    size_hint: None,None

''')

class Loading_widget_progress(FloatLayout):
    angle_start = NumericProperty(30)
    angle_end = NumericProperty(35)
    anim_color = ListProperty([0,.2,.4,1])
    
    
    def __init__(self, **kwargs):
        super(Loading_widget_progress, self).__init__(**kwargs)
        Clock.schedule_once(self.animate_circle,1)

    def animate_circle(self, *args):
        load_c = self.canvas.get_group('a')[0]
        anim = Animation(angle_end = 395, duration = 1.4, t = 'in_sine')\
               & Animation(angle_start = 390, duration = 1.4, t = 'out_sine')\
               & Animation(anim_color = [random.randint(0.0, 1.0),random.randint(0.0, 1.0),random.randint(0.0, 1.0),1])
        anim.bind(on_complete = self.start_anim)
        anim.start(self)
    
    def start_anim(self, *args):
        self.angle_start = 30
        self.angle_end = 35
        Clock.schedule_once(self.animate_circle,0)


class Loading_widget(BoxLayout):
    text = StringProperty('')
    color = ListProperty((0,0,0,.8))
