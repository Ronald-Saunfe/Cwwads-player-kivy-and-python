from touchripple import TouchRippleButtonBehavior, TouchRippleBehavior
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior, ToggleButtonBehavior
from kivy.properties import StringProperty, ObjectProperty,\
     NumericProperty, ListProperty, OptionProperty
from kivy.uix.image import Image
from ripplebehavior import CircularRippleBehavior
from kivy.uix.floatlayout import FloatLayout
from widgets.Labels import MDLabel
from widgets.Shadows import *
from kivy.animation import Animation
from kivy.core.text import Label as CoreLabel
from kivy.graphics import Color, Ellipse, RoundedRectangle
from kivy.metrics import dp

Builder.load_string('''
<ClickableLabel>:
    font_size: '12sp'
    
<Label_ripple>:
    font_name: 'fonts/Montserrat-SemiBold.ttf' 
    font_size: '11sp' 
    valign: 'center'
    size_hint: None, None
    color: 0,0,0,.83
    text_size: self.size

<Text_Button>:
    font_name: 'fonts/Montserrat-Bold.ttf' if self.font_style == 'Title' else 'fonts/Montserrat-Medium.ttf' if self.font_style == 'Subhead' else 'fonts/Montserrat-Regular.ttf' 
    font_size: '12sp' if root.font_style == 'Caption' else '14sp'
    halign: root.haligns
    valign: 'center'
    size_hint: None, None
    color: 0,0,0,1
    text_size: self.size 

<Image_clickable>:
    mipmap: True
    allow_stretch: True
    keep_data: False
    size_hint: None, None

<Toggle_Text_Button>:
    canvas.before:
        Color:
            group: 'a'
            rgba: 1,1,1,0

        Rectangle:
            size: self.size
            pos: self.pos

<Icon_label_toggle>:
    font_name: 'fonts/materialdesignicons-webfont.ttf'
    text: u'{0}'.format(root.n_text)

<Badge_icon_toggle>:
    canvas.after:
        Color:
            rgba: 250/255, 240/255, 11/255,1
            

<NPIButton1>:
    canvas:
        Color:
            rgba: .93, .93, .93, 1

        Ellipse:
            group: 'a'
            size: self.size
            pos: self.pos

        Color:
            rgba: 0, 0,0,.3

        SmoothLine:
            group: 'a'
            ellipse: self.x,self.y,self.width, self.height

    size_hint: None, None
    size: dp(8), dp(8)

<CircleBtn>:
    canvas:
        Color:
            group: 'a'
            rgba: 0,0,0, .3

        Ellipse:
            size: self.size
            pos: self.pos

        SmoothLine:
            ellipse: self.x, self.y, self.width, self.height
            
    size_hint: None, None
    size: dp(6), dp(6)

<Contained_button1>:
    lbl: lbl
    elevation: '0' if  root.state=='enabled' else '0'
    canvas.before:
        Color:
            rgba: root.bg_color if root.state=='enabled' else (0,0,0,.2)

        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: dp(0),dp(0),dp(4),dp(4)
 
                
    size_hint: None, None
    color: 0,0,0,1

    padding: dp(16), 0, dp(16), 0
   
    MDLabel:
        canvas:
        id: lbl
        text: str(root.text).upper()
        font_name: 'fonts/materialdesignicons-webfont.ttf'
        halign: 'center'
        valign: 'center'
        font_size: '20sp'
        text_size: self.size
        size_hint: 1,1
        color: root.fg_color

<Contained_button>:
    lbl: lbl
    elevation: '1'
    canvas.before:
        Color:
            rgba: root.bg_color if root.state=='enabled' else (0,0,0,.2)

        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: dp(4),dp(4),dp(4),dp(4)
 
                
    size_hint: None, None
    color: 0,0,0,1

    padding: dp(16), 0, dp(16), 0
   
    MDLabel:
        canvas:
        id: lbl
        text: str(root.text).upper()
        halign: 'center'
        valign: 'center'
        font_size: '12sp'
        size_hint: 1,1
        color: root.fg_color

<Separator>:
    canvas:
        Color:
            rgba: root.color
        
        Rectangle:
            size: self.size
            pos: self.pos
    size_hint: None, None
        
''')

class ClickableLabel(ButtonBehavior, MDLabel):
    down_color = ListProperty()
    up_color = ListProperty()
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.color = self.down_color
        return super(ClickableLabel, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        self.color = self.up_color
        if self.collide_point(*touch.pos):
            return super(ClickableLabel, self).on_touch_up(touch)
        return False

    
class Label_ripple(TouchRippleBehavior, Label):
    font_style = OptionProperty(
        'Caption', options=['Caption', 'Subhead', 'Title'])

class Text_Button(TouchRippleButtonBehavior, Label):
    state = OptionProperty( 'enabled', options=['enabled','disabled'] )
    haligns = StringProperty('right')
    font_style = OptionProperty(
        'Caption', options=['Caption', 'Subhead', 'Title'])
    upper = StringProperty('False')
    ripple_colors = ListProperty((.85,.85,.85,.1))
    ripple_to_alpha = NumericProperty(.3)

    def __init__(self, **kwargs):
        super(Text_Button, self).__init__(**kwargs)
        self.bind(text=self.capitalize)
        self.ripple_color = self.ripple_colors
        self.ripple_fade_to_alpha = self.ripple_to_alpha
        self.ripple_duration_in = .3
        self.ripple_duration_out = .1
        self.font_size= '13sp'
        

    def capitalize(self, *args):
        if self.upper=='True':
            self.text = self.text.upper()

        if self.state == 'disabled':
            self.opacity = .6
        elif self.state == 'enabled':
            self.opacity = 1

class Image_clickable(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(Image_clickable, self).__init__(**kwargs)

class Base_Icon(CircularRippleBehavior,Label):
    pass

class Toggle_Text_Button(ToggleButtonBehavior, Label_ripple):
    down_color = ListProperty((45/255, 11/255, 250/255, .83))
    up_color = ListProperty((0,0,0,.63))
    def __init__(self, **kwargs):
        super(Toggle_Text_Button, self).__init__(**kwargs)
        
    def on_state(self, widget, value):
        if value=='down':
            anim = Animation(rgba =(.95, .95, .95,1), duration=.2, t='out_cubic')
            anim.start(self.canvas.before.get_group('a')[0])
            self.color = self.down_color
        else:
            anim = Animation(rgba =(1,1,1,0), duration=.2, t='in_cubic')
            anim.start(self.canvas.before.get_group('a')[0])
            self.color = self.up_color


class Icon_label_toggle(ToggleButtonBehavior, Base_Icon):
    d_text = StringProperty()
    n_text = StringProperty()
    
    def on_state(self, widget, value):
        if value =='down':
            self.text =  self.d_text
        else:
            self.text =  self.n_text

            
class Badge_icon_toggle(Icon_label_toggle):
    texts = StringProperty(0)

    def put_badge(self):      
        self.badge_label = CoreLabel()
        if int(self.texts) > 99:
            self.texts = '99+'
            
        self.badge_label.text = str(self.texts)
        # the label is usually not drawn until needed, so force it to draw.
        self.badge_label.refresh()
        self.badget_texture = self.badge_label.texture


        self.roun_rec = RoundedRectangle(size = (self.badget_texture.size[0]+dp(16),\
                                                 self.badget_texture.size[1]),\
                                         pos = (self.x+(self.width*1/2),\
                                                self.y+(self.height*1/2)),\
                                         radius=(dp(8),dp(8),dp(8),dp(8)))
        
        self.text_graphics = RoundedRectangle(size =(self.roun_rec.size[0]-dp(8),\
                                                 self.roun_rec.size[1]),\
                                        pos = self.roun_rec.pos,\
                                        texture = self.badget_texture,\
                                              radius=(dp(1),dp(1),dp(1),dp(1)))

        self.canvas.after.add(Color(rgba=(11/255,135/255,250/255,1)))
        self.canvas.after.add(self.roun_rec)
        self.canvas.after.add(Color(rgba=(1,1,1,1)))
        self.canvas.after.add(self.text_graphics)

        self.bind(pos = self.pos_change)

    def pos_change(self, *args):
        self.update_graphics()

    def update_graphics(self):
        self.roun_rec.size = (self.badget_texture.size[0]+dp(8),\
                                                 self.badget_texture.size[1])
        self.roun_rec.pos = (self.x+(self.width*1/2),\
                                                self.y+(self.height*1/2))
        self.text_graphics.size = (self.roun_rec.size[0]-dp(8),\
                                   self.roun_rec.size[1])
        
        self.text_graphics.pos = (self.roun_rec.pos[0]+dp(4),\
                                  self.roun_rec.pos[1])
        
    def update_badge(self):
        self.canvas.after.clear()
        self.put_badge()
        self.update_graphics()

class NPIButton1(ToggleButtonBehavior, FloatLayout):
    indexs = NumericProperty(0)
    bg_color = ListProperty([250/255, 240/255, 11/255,1])
        
    def pos_correct(self,*args):
        self.new_rec.pos = self.pos
        
    def on_state(self, widget, state):
        if state == 'down':
            Clock.schedule_once(self.put_now,1)
        else:
            try:
                self.canvas.remove(self.color_top)
                self.canvas.remove(self.new_rec)
            except:
                pass

    def put_now(self, *args):
        self.color_top = Color(rgba=self.bg_color)
     
        self.new_rec = Ellipse(size = self.size, pos = self.pos)
        self.bind(pos=self.pos_correct)
        
        self.canvas.add(self.color_top)
        self.canvas.add(self.new_rec)

class CircleBtn(ToggleButtonBehavior,FloatLayout):
    def on_state(self, inst, value):
        if value=='down':
            anim = Animation(rgba=(1,1,1,1), duration=.3)
            anim.start(self.canvas.get_group('a')[0])
        else:
            anim = Animation(rgba=(0,0,0,.3), duration=.3)
            anim.start(self.canvas.get_group('a')[0])
          
class Contained_button(TouchRippleBehavior, Rounded_Shadow1):
    state = OptionProperty( 'enabled', options=['enabled','disabled'] )
    bg_color = ListProperty([.1,.3,.8,1])
    fg_color = ListProperty([1,1,1,1])
    lbl = ObjectProperty()
    text = StringProperty()
    ripple_colors = ListProperty((1,1,1,.8))
    ripple_to_alpha = NumericProperty(.3)

    def __init__(self, **kwargs):
        self.register_event_type('on_press')
        self.register_event_type('on_release')
      
        super(Contained_button, self).__init__(**kwargs)
        self.elevation = '1'
        self.ripple_color = self.ripple_colors
        self.ripple_fade_to_alpha = self.ripple_to_alpha
        self.ripple_duration_in = .3
        self.ripple_duration_out = .5
        self.prev_bg_color = self.bg_color
      
    def on_touch_down(self, touch):
        if not self.collide_point(touch.x, touch.y):
            return False
       
        if self.state == 'enabled':
            touch.grab(self)
            self.elevation = '4'
            self.ripple_show(touch)
            self.dispatch('on_press')

        return True
            
     
    def on_touch_up(self, touch):
        #prevent from other button being triggered
        if touch.grab_current is not self:
            return False
        touch.ungrab(self)
        self.elevation = '1'
        #Clock.schedule_once(self.elev_down, 0.8)
        self.ripple_fade()
        if self.collide_point(touch.x, touch.y):
            if self.state == 'enabled':
                self.dispatch('on_release')

        return True
                
    def elev_down(self, *args):
        self.elevation = '0'
        
    def on_press(self):
        pass

    def on_release(self):
        pass


class Separator(BoxLayout):
    color = ListProperty([0,0,0,.3])

class Contained_button1(TouchRippleButtonBehavior, Rectangle_Shadow1):
    state = OptionProperty( 'enabled', options=['enabled','disabled'] )
    bg_color = ListProperty([.1,.3,.8,1])
    fg_color = ListProperty([1,1,1,1])
    lbl = ObjectProperty()
    text = StringProperty()
    ripple_colors = ListProperty((1,1,1,.8))
    ripple_to_alpha = NumericProperty(.3)    

    def __init__(self, **kwargs):
        self.register_event_type('on_press')
        self.register_event_type('on_release')
      
        super(Contained_button1, self).__init__(**kwargs)
        self.elevation = '0'
        self.ripple_color = self.ripple_colors
        self.ripple_fade_to_alpha = self.ripple_to_alpha
        self.ripple_duration_in = .3
        self.ripple_duration_out = .5
        self.prev_bg_color = self.bg_color
      
    def on_touch_down(self, touch):
        if not self.collide_point(touch.x, touch.y):
            return False
       
        if self.state == 'enabled':
            touch.grab(self)
            self.elevation = '4'
            self.ripple_show(touch)
            self.dispatch('on_press')

        return True
            
     
    def on_touch_up(self, touch):
        #prevent from other button being triggered
        if touch.grab_current is not self:
            return False
        touch.ungrab(self)
        self.elevation = '0'
        #Clock.schedule_once(self.elev_down, 0.8)
        self.ripple_fade()
        if self.collide_point(touch.x, touch.y):
            if self.state == 'enabled':
                self.dispatch('on_release')

        return True
                
    def elev_down(self, *args):
        self.elevation = '0'
        
    def on_press(self):
        pass

    def on_release(self):
        pass
    
