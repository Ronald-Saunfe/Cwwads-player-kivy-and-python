from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty,ListProperty, BooleanProperty
from kivy.animation import Animation


Builder.load_string('''

<NewTextinput>:
    canvas.after:
        Color:
            rgba: 0,0,0,.5
            group: 'a'

        SmoothLine:
            group: 'a'
            width: dp(1)
            points: self.x, self.y, self.x+self.width, self.y

        Color:
            rgba: root.color_highlt 
            group: 'b'

        SmoothLine:
            group: 'b'
            width: dp(2)
            points: self.x+self.width/2, self.y, self.x+self.width/2, self.y

    size_hint_y:None
    height: dp(48)
    padding: dp(8), (self.height/3.6), dp(8),0
    foreground_color: 0,0,0,1
    font_name: 'fonts/Montserrat-Regular.ttf'
    hint_text_color: 0,0,0,.63
    background_color: 1,1,1,0
    background_normal: ''
    background_active: ''
    multiline: False

''')

class NewTextinput(TextInput):
    validate_type = StringProperty('')
    color_highlt = ListProperty((45/255, 11/255, 250/255, 1))
    
    def insert_text(self, substring, from_undo=False):
        if self.validate_type == 'numbers':
            pat = re.compile('[^0-9]')
            if '.' in self.text:
                s = re.sub(pat, '', substring)
            else:
                s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
            return super(NewTextinput, self).insert_text(s, from_undo=from_undo)

        elif self.validate_type == 'alpha':
            pat = re.compile('[^A-Za-z0-9 ]')
            if '.' in self.text:
                s = re.sub(pat, '', substring)
            else:
                s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
            return super(NewTextinput, self).insert_text(s, from_undo=from_undo)

        else:
            return super(NewTextinput, self).insert_text(substring, from_undo=from_undo)


    def on_focus(self,instance, value):
        line = self.canvas.after.get_group('b')[1]
        if value:
            anim1 = Animation(points=[self.x, self.y, self.x+self.width, self.y],\
                              duration=.3, t= 'out_cubic')
            anim1.start(line)
        else:
            anim1 = Animation(points=[self.x+self.width/2, self.y, self.x+self.width/2, self.y]\
                    , duration=.3, t= 'in_cubic')
            anim1.start(line)

    def err(self,blean=True):
        if blean==True:
            self.color_highlt = (1,0,0,1)
        else:
            self.color_highlt = (45/255, 11/255, 250/255, 1)


            
class Textfield(TextInput):
    error = BooleanProperty(False)
    helper_text_on_ = StringProperty('')
    lin_color = ListProperty((45/255, 11/255, 250/255, 1))
    
    def insert_text(self, substring, from_undo=False):
        if self.validate_type == 'numbers':
            pat = re.compile('[^0-9]')
            if '.' in self.text:
                s = re.sub(pat, '', substring)
            else:
                s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
            return super(Textfield, self).insert_text(s, from_undo=from_undo)

        elif self.validate_type == 'alpha':
            pat = re.compile('[^A-Za-z0-9 ]')
            if '.' in self.text:
                s = re.sub(pat, '', substring)
            else:
                s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
            return super(Textfield, self).insert_text(s, from_undo=from_undo)

        else:
            return super(Textfield, self).insert_text(substring, from_undo=from_undo)

    def on_focus(self, instance, value):
        color = self.canvas.after.get_group('b')[0]
        line = self.canvas.after.get_group('b')[1]
        if value:
            if self.error==False:
                lin_color = self.lin_color
            else:
                lin_color =(250/255, 11/255, 40/255,1)
                
            anim = Animation(rgba=lin_color, duration=.1, t= 'out_cubic')
            anim.start(color)

            if (self.helper_text_on_)=='':
                anim1 = Animation(points=[self.x, self.y, self.x+self.width, self.y],\
                              duration=.4, t= 'out_cubic')
                anim1.start(line)
            else:
                self.bind(pos=partial(self.o_pos, line))
            
        else:
            anim = Animation(rgba=(0,0,0,0), duration=0, t= 'in_cubic')
            anim.start(color)
            if len(self.helper_text_on_)==0:
                anim1 = Animation(points=[self.x+self.width/2, self.y, self.x+self.width/2, self.y]\
                    , duration=.4, t= 'in_cubic')
                anim1.start(line)
            else:
                self.bind(pos=partial(self.o_pos1, line))

    def o_pos1(self, line,*args):
        anim1 = Animation(points=[self.x+self.width/2, self.y, self.x+self.width/2, self.y]\
                    , duration=.4, t= 'in_cubic')
        anim1.start(line)
                
    def o_pos(self, line,*args):
        anim1 = Animation(points=[self.x, self.y, self.x+self.width, self.y],\
                              duration=.1, t= 'out_cubic')
        anim1.start(line)
