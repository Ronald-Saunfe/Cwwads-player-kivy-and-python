from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation


class BoxLayout_animation(BoxLayout):
    def add_widget(self, widget, index=0, canvas=None):
        
        anim= Animation(opacity=1, duration = 0.5, t='out_cubic')
        anim.start(widget)
   
        return super(BoxLayout_animation, self).add_widget(widget, index, canvas)
