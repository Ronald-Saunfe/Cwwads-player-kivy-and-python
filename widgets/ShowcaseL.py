from kivy.lang import Builder
from kivy.uix.stencilview import StencilView
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, ObjectProperty,\
     NumericProperty, ListProperty
from kivy.metrics import dp
from kivy.animation import Animation


Builder.load_string('''

<ShowcaseL>:


''')


class ShowcaseL(FloatLayout, StencilView):
    box_x = NumericProperty()
    show_box = ObjectProperty()
    show_box_width = NumericProperty()
    init_coord = ListProperty([0,0])
    init_coord_gest = ListProperty([0,0])
    current_index = NumericProperty(0)
    indeeex = NumericProperty(0)
    anim_progress = StringProperty('no')
    paddings = NumericProperty(dp(20))
    no_widgets=StringProperty()
    add_count = NumericProperty(0)
    add_count1 = NumericProperty(0)
    lock = False
    
    def __init__(self, **kwargs):
        super(ShowcaseL, self).__init__(**kwargs)
        self._x = self.x + (self.width*1/8)
        self.on_going_scroll = False
        self.on_going_scroll1 = False
        self.on_going_scroll2 = False
        self.scroll_direction=''
        
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.on_going_scroll == True: #ensure there is no current scroll
                touch.ungrab(self)
                return True
                
            self.init_coord = touch.pos
            self.init_coord_gest = touch.pos
            touch.grab(self)
            
        return super(ShowcaseL, self).on_touch_down(touch)
            

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            self.change_x_gest = touch.pos[0] - self.init_coord_gest[0]
            self.change_x = touch.pos[0] - self.init_coord[0]
            if self.on_going_scroll1 == False and self.on_going_scroll2 == False: #prevent interupting other previous scrolling
                print(self.on_going_scroll1, self.on_going_scroll2)
                if int(abs(self.change_x_gest)) <= int(self.width*1/7):#Be scrollling
                    self.on_going_scroll = True
                    
                    for child in self.children:
                        child.x += self.change_x
                        self.init_coord = touch.pos
                        self.move_gest = self.change_x_gest #check the movement

                    if str(self.change_x_gest)[0] =='-':
                        self.scroll_direction='left'
                    else:
                        self.scroll_direction='right'

                else: #jump to the center
                    #check the direction of the scroll
                    #ensure their is no prevous scrolling going on
                    if self.on_going_scroll2 == False :
                        self.on_going_scroll2 =True
                        if self.scroll_direction =='left': #moving left
                            if self.indeeex+1 < len(self.children):
                                for child in self.children:
                                    ch_x = child.x
                                    ch_x -= (child.width + self.paddings)
                                    
                                    ch_x += abs(self.move_gest)

                                    self.anim = Animation(x = ch_x, t='in_quad', duration=.3, height= self.height*5/8)
                                    self.anim.start(child)
                                    
                                    
                                    self.init_coord = touch.pos
                                    
                                #set the current indeeex
                                self.anim = Animation( t='in_sine', duration=.3, height = self.height*3/4)
                                self.anim.start(self.children[self.indeeex+1])
                                
                                
                                self.anim.bind(on_complete=lambda *largs: setattr(self, 'indeeex', self.indeeex+1))
                                self.anim.bind(on_complete=lambda *args: self.on_going_scroll)
                                self.anim.bind(on_complete=lambda *x: print(self.indeeex+1, 'indeeex'))
                                
                            else:
                                for child in self.children:
                                    anim = Animation( x=child.x + abs(self.move_gest),t='out_expo', duration=.4)
                                    anim.start(child)
                                    
                            
                        elif self.scroll_direction =='right': #moving right
                            if self.indeeex >0:
                                for child in self.children:
                                    ch_x1 = child.x
                                    ch_x1 += ((child.width + self.paddings))

                                    ch_x1 -= abs(self.move_gest)
                                    
                                    self.anim = Animation(x = ch_x1, t='in_quad', duration=.3, height= self.height*5/8)
                                    self.anim.start(child)
                                    
                                    self.init_coord = touch.pos

                                self.anim = Animation( t='in_sine', duration=.3, height = self.height*3/4)
                                self.anim.start(self.children[self.indeeex-1])
                                
                                self.anim.bind(on_complete=lambda *largs: setattr(self, 'indeeex', self.indeeex-1))
                                self.anim.bind(on_complete=lambda *x: print(self.indeeex-1, 'indeeex'))
                               
                            else:
                                for child in self.children:
                                    anim = Animation( x=child.x - abs(self.move_gest),t='out_quad', duration=.3)
                                    anim.start(child)
                                    
                                    
                        self.on_going_scroll2 = False

                    touch.ungrab(self)
                    
                    self.on_going_scroll = False
                    

    def on_touch_up(self, touch):
        if touch.grab_current is not self:
            return True

        if self.on_going_scroll == True:
            #if the gesture was not complete then return the widgets to their normal positions
            #prevent changing variable 
            if int(abs(self.change_x_gest)) <= int(self.width*1/7):
                if self.on_going_scroll1 == False:
                    self.on_going_scroll1 = True
                    if self.scroll_direction =='left':
                        for child in self.children:
                            anim = Animation( x=child.x + abs(self.change_x_gest),t='out_cubic', duration=.1)
                            
                            anim.start(child)
                        self.on_going_scroll =False
                        
                    elif self.scroll_direction =='right':
                        for child in self.children:
                            anim = Animation( x=child.x - abs(self.change_x_gest),t='out_cubic', duration=.1)
                            anim.start(child)
                            
                            
                        self.on_going_scroll =False

                    self.on_going_scroll1 = False

        touch.ungrab(self)
        return super(ShowcaseL, self).on_touch_up(touch)

     
    def add_widget(self, widget, index=0, x=None, canvas=None):
        #set the size of the widget
        widget.width = (self.width*3/4)
        widget.height = (self.height*3/4) if len(self.children)==0 else (self.height*5/8)
        #set the widget position
        if self.add_count >0:
            if len(self.children)==0:
                self._px = self._x
            else:
                self._px = (self.children[len(self.children)-1].x+ self.children[len(self.children)-1].width) + self.paddings
                if x==None:
                    self._px += (self.add_count*widget.width)+(self.add_count*self.paddings)
                else:
                    self._px = self.children[len(self.children)-1].x + self.children[len(self.children)-1].width+ self.paddings

                self.add_count1 +=1
        else:
            self._px = self._x

        widget.x = self._px
        widget.pos_hint ={'center_y':.5}
       
        self.no_widgets = str(len(self.children))
        self.c =0
        
        self.add_count +=1
        index+=len(self.children)
        return super(ShowcaseL, self).add_widget(widget, index, canvas)

    def on_size(self, layout, size):
        if self.on_going_scroll==False:
            _x = layout.x = (layout.x + (layout.width*1/8))
            ind = 0
            #print(self.on_going_scroll, self.indeeex,'size changed triggered')
            self.indeeex = 0
            for child in layout.children:
                #set new size
                child.width = (layout.width*3/4)
                child.height = (layout.height*3/4) if self.current_index==ind else (layout.height*5/8) 
                #set new pos
                child.x =_x
                _x += (child.width + self.paddings)
                ind+=1
