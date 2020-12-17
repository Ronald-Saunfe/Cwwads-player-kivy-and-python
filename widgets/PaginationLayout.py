from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import DictProperty
from kivy.properties import ObjectProperty, ListProperty, OptionProperty,\
     NumericProperty, StringProperty
from kivy.metrics import dp
import ast
from widgets.Loading import *
from kivy.core.window import Window

Builder.load_string('''

<Paginating_BoxLayout>:
    on_scroll_y: root.scrolled_y()
    BoxLayout:
        id: box
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        padding:  dp(16), dp(16), dp(16), dp(16)
        
        


''')

class Paginating_BoxLayout(ScrollView):
    func = ObjectProperty()
    widget = ObjectProperty()
    widget_property = DictProperty()
    no_of_rec = NumericProperty()
    pointer = NumericProperty(0)
    email = StringProperty()
    request = {}
    types = ''
    
    def __init__(self, **kwargs):
        super(Paginating_BoxLayout, self).__init__(**kwargs)
        self.data = []
        self.page = 0
        
    def load_data(self):
        self.crr_load = Loading_widget_progress(size=(dp(48), dp(48)),\
                                pos_hint={'center_x':.5, 'center_y':.5})
        self.ids.box.add_widget(self.crr_load)

        if self.types=='someone_bask':
            request = {'type':'load_people_baskets_init',\
                                      'start': self.pointer,\
                                      'end': int(Window.height/dp(80)),\
                                      'action': 'next',\
                                        'email': self.email}
        else:
            request = self.request
            
        reslt = self.func(request)
        
        self.no_of_rec = reslt['no_emails']

        self.ids.box.remove_widget(self.crr_load)
        delattr(self, 'crr_load')
        return reslt

    def init_widgets(self):
        res = self.load_data()['results']
       
        for rec in res:
            wid = self.widget()
            #set widget properties
            for prop in self.widget_property.keys():
                statement = "%s.%s = str(%s)"%('wid', prop, self.widget_property[prop] )
                exec("%s"%statement)

            self.pointer +=1
            
            

            self.ids.box.add_widget(wid)
        self.page+=1
            
        
    def scrolled_y(self):
        #check if the scroll has reached the last widget
        if self.scroll_y <=0:
            #check if all emails are shown
            
            if self.pointer < (self.no_of_rec-1):
                #check if there is a curent request in progress
                if hasattr(self, 'crr_load')==False:
                    res = self.load_data()

                    #remove the second last set of widgets
                    if (self.page+1)>2:
                        c=0
                        for child in self.ids.box.walk():
                            if isinstance(child, self.widget):
                                if c <= int(Window.height/dp(80)):
                                    self.ids.box.remove_widget(child)
                                    c+=1
                            
                        self.page = 0

                    #add new widgets
                    for rec in res['results']:
                        wid = self.widget()
                        #set widget properties
                        for prop in self.widget_property.keys():
                            statement = "%s.%s = str(%s)"%('wid', prop, self.widget_property[prop] )
                            exec("%s"%statement)

                        self.pointer +=1
                        

                        self.ids.box.add_widget(wid)
                    print(self.pointer, 'pointer')

                    self.page +=1
                    
                    #change the view
                    top = (self.ids.box.top - self.y) / self.ids.box.height
                    y = top + self.height
                    self.scroll_y = y / self.ids.box.height
                    
                    self.no_of_rec = res['no_emails']

                    
        
