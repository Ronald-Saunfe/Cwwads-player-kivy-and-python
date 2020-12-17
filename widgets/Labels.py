from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import OptionProperty

Builder.load_string('''

<MDLabel>:
    font_name: 'fonts/Montserrat-Bold.ttf' if self.font_style == 'Title' else 'fonts/Montserrat-Medium.ttf' if self.font_style == 'Subhead' else 'fonts/Montserrat-Regular.ttf' 
    markup: True
    mipmap: True
    size: self.texture_size
    text_size: root.width, None
    color: 0,0,0,1

''')


class MDLabel(Label):
    font_style = OptionProperty(
        'Caption', options=['Caption', 'Subhead', 'Title'])
    def __init__(self, **kwargs):
        super(MDLabel, self).__init__(**kwargs)
