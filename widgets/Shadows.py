from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty

Builder.load_string('''
<Rounded_Shadow_t1>:
    canvas.before:
        Color:
            rgba: 0, 191/255,1,1
            
        BorderImage:
            source:
                'pics/invisible.png' if root.elevation=='0' else\
                'assets/1dpr.png' if root.elevation =='1' else \
                'assets/4dpr.png' if root.elevation =='4' else\
                'assets/6dpr.png' if root.elevation =='6' else \
                'assets/8dpr.png' if root.elevation =='8' else ''
            pos:
                self.x if root.elevation=='0' else\
                (self.x - dp(2.5)) if root.elevation=='1' else \
                (self.x - dp(8)) if root.elevation =='4' else \
                (self.x - dp(14)) if root.elevation =='6' else(self.x - dp(16)),\
                self.y if root.elevation=='0' else\
                (self.y - dp(6)) if root.elevation =='6' else \
                (self.y - dp(5.5)) if root.elevation =='8' else (self.y - dp(5))
                
            size:
                self.width  if root.elevation=='0' else \
                (self.width + dp(5)) if root.elevation=='1' else \
                (self.width + dp(16)) if root.elevation=='4' else \
                (self.width + dp(28)) if root.elevation =='6' else (self.width + dp(32)), \
                self.height  if root.elevation=='0' else \
                self.height - dp(10) if root.elevation=='4' else \
                (self.height - dp(10)) if root.elevation =='6' else (self.height + dp(6.5) )


<Rounded_Shadow_t>:
    canvas.before:
        BorderImage:
            source:
                'pics/invisible.png' if root.elevation=='0' else\
                'assets/1dpr.png' if root.elevation =='1' else \
                'assets/4dpr.png' if root.elevation =='4' else\
                'assets/6dpr.png' if root.elevation =='6' else \
                'assets/8dpr.png' if root.elevation =='8' else ''
            pos:
                self.x if root.elevation=='0' else\
                (self.x - dp(2.5)) if root.elevation=='1' else \
                (self.x - dp(8)) if root.elevation =='4' else \
                (self.x - dp(14)) if root.elevation =='6' else(self.x - dp(16)),\
                self.y if root.elevation=='0' else\
                (self.y - dp(5.5)) if root.elevation =='6' else \
                (self.y - dp(5.5)) if root.elevation =='8' else (self.y - dp(5))
                
            size:
                self.width  if root.elevation=='0' else \
                (self.width + dp(5)) if root.elevation=='1' else \
                (self.width + dp(16)) if root.elevation=='4' else \
                (self.width + dp(28)) if root.elevation =='6' else (self.width + dp(32)), \
                self.height  if root.elevation=='0' else \
                self.height - dp(10) if root.elevation=='4' else \
                (self.height + dp(8)) if root.elevation =='6' else (self.height + dp(6.5) )


<Rounded_Shadow1>:
    canvas.before:
        BorderImage:
            source:
                'pics/invisible.png' if root.elevation=='0' else\
                'assets/1dpr.png' if root.elevation =='1' else \
                'assets/4dpr.png' if root.elevation =='4' else\
                'assets/6dpr.png' if root.elevation =='6' else \
                'assets/8dpr.png' if root.elevation =='8' else ''
            pos:
                self.x if root.elevation=='0' else\
                (self.x - dp(2.5)) if root.elevation=='1' else \
                (self.x - dp(8)) if root.elevation =='4' else \
                (self.x - dp(14)) if root.elevation =='6' else(self.x - dp(16)),\
                self.y if root.elevation=='0' else\
                (self.y - dp(5.5)) if root.elevation =='6' else \
                (self.y - dp(5.5)) if root.elevation =='8' else (self.y - dp(5))
                
            size:
                self.width  if root.elevation=='0' else \
                (self.width + dp(5)) if root.elevation=='1' else \
                (self.width + dp(16)) if root.elevation=='4' else \
                (self.width + dp(28)) if root.elevation =='6' else (self.width + dp(32)), \
                self.height  if root.elevation=='0' else \
                (self.height + dp(8)) if root.elevation =='6' else (self.height + dp(6.5) )

    
<Rectangle_Shadow1>:
    canvas.before:
        BorderImage:
            source:
                'pics/invisible.png' if root.elevation=='0' else\
                'assets/1dp.png' if root.elevation =='1' else \
                'assets/4dp.png' if root.elevation =='4' else\
                'assets/6dpr.png' if root.elevation =='6' else \
                'assets/8dpr.png' if root.elevation =='8' else ''
            pos:
                self.x if root.elevation=='0' else\
                (self.x - dp(2.5)) if root.elevation=='1' else\
                (self.x - dp(8)) if root.elevation =='4' else (self.x - dp(14))  ,\
                self.y if root.elevation=='0' else\
                (self.y - dp(5.5)) if root.elevation =='6' else\
                (self.y - dp(5.5)) if root.elevation =='8' else (self.y - dp(5))
            size:
                self.width  if root.elevation=='0' else \
                (self.width + dp(5)) if root.elevation=='1' else\
                (self.width + dp(16)) if root.elevation=='4' else (self.width + dp(28)),\
                self.height  if root.elevation=='0' else \
                (self.height + dp(8)) if root.elevation =='6' else (self.height + dp(6.5))
        

''')


class Rectangle_Shadow1(BoxLayout):
    elevation = StringProperty('1')

class Rounded_Shadow_t(BoxLayout):
    elevation = StringProperty('1')

class Rounded_Shadow_t1(BoxLayout):
    elevation = StringProperty('1')
    
class Rounded_Shadow1(BoxLayout):
    elevation = StringProperty('1')
