from kivy.lang import Builder
from widgets.Shadows import *
from kivy.uix.behaviors import ButtonBehavior, ToggleButtonBehavior
from kivy.properties import ListProperty
from kivy.uix.label import Label
from kivy.metrics import dp
from functools import partial
from widgets.Dialogs import DialogConfirm
from kivy.core.window import Window
from kivy.uix.modalview import ModalView
import threading
from kivy.core.text import Label as CoreLabel
from kivy.graphics import Color, Ellipse, RoundedRectangle, SmoothLine
import ast

Builder.load_string('''

<Bask_purchase>:
    canvas:
        Color:
            rgba: 1,1,1,1

        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: dp(4), dp(4), dp(4), dp(4)
        
        Color:
            rgba: 0,0,0,.3

        SmoothLine:
            rounded_rectangle: self.x, self.y, self.width, self.height, dp(4)
            
    size_hint_y: None
    elevation: '0'
    height: dp(30)
    padding: dp(8),0,0,0
    
    MDLabel:
        text: '[sup][size=10]Kshs[/size][/sup] %s'%root.price
        halign:'left'
        valign: 'middle'
        markup: True
        color: (0,0,0, .83)

    Widget:
        canvas:
            Color:
                rgba: 0,0,0,.3

            Rectangle:
                size: self.size
                pos: self.pos
                
        size_hint: None, .5
        width: dp(1)
        pos_hint: {'center_y':.5}
        

    Text_Button:
        id: btn_purchase
        text: 'PURCHASE'
        halign: 'center'
        size: dp(120), dp(30)
        color: (45/255, 11/255, 250/255, 1)
        pos_hint: {'center_x':.5, 'center_y':.5}


<Notif_P>:
    canvas:
        Color:
            rgba: 1,1,1, 1

        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: dp(4), dp(4),dp(4),dp(4)
            
    size_hint_y: None
    height: dp(80)
    padding: dp(16),dp(8),dp(16),dp(8)
    spacing: dp(8)
  

##    Icon_label_toggle:
##        text: u'\uF364'
##        font_size: '32sp'
##        halign: 'center'
##        valign: 'middle'
##        color: 0,0,0,1
##        size_hint_x: None
##        width: dp(48)
##        pos_hint:{'center_x':.5}

    BoxLayout:
        orientation: 'vertical'
        
        MDLabel:
            text: '%s has purchased your basket'%root.buyer
            halign: 'left'
            valign: 'top'
            font_style: 'Caption'
        MDLabel:
            text: root.date
            halign: 'left'
            valign: 'middle'
            size_hint_y: None
            height: dp(15)
            font_size: '10sp'
            color: 0,0,0,.63
            pos_hint:{'top':1}

<Pple_W>:
    canvas:
        Color:
            rgba: 1,1,1,1

        Rectangle:
            size: self.size
            pos: self.pos
            
    orientation: 'vertical'
    elevation: '4'
    size_hint_y: None
    spacing: dp(8)
    padding: dp(8), dp(8), dp(8), dp(8)


    BoxLayout:
        size_hint_y: None
        height: dp(64)
        
        BoxLayout:
            size_hint_x:None
            width: dp(80)
            Widget:
                canvas:
                    Color:
                        rgba: 1,1,1,1

                    Ellipse:
                        source: 'pics/user_name.jpg'
                        size: self.size
                        pos: self.pos

                    Color:
                        rgba: 1,1,1,1

                    SmoothLine:
                        ellipse: self.x,self.y, self.width, self.height
                size_hint:None,None
                size: dp(64),dp(64)
                pos_hint: {'center_x':.5, 'center_y':.5}

        BoxLayout:
            orientation: 'vertical'
            MDLabel:
                text: root.username
                font_style: 'Subhead'
                size_hint_y: None
                height: dp(15)
                shorten: True
                shorten_from: 'right'
            MDLabel:
                text: root.email
                size_hint_y: None
                height: dp(15)
                color: 0,0,0,.63
                shorten: True
                shorten_from: 'right'
            BoxLayout:

    ClickableLabel:
        text: 'Show basket list'
        down_color: (45/255, 11/255, 250/255, 1)
        up_color: (45/255, 11/255, 250/255, 1)
        color: (45/255, 11/255, 250/255, 1)
        size_hint_y: None
        halign: 'center'
        height: dp(15)
        on_release: root.show_baskets(self)

    BoxLayout:
        id: box1
        orientation: 'vertical'
        spacing: dp(8)
        size_hint_y: None
        height: dp(0)

        
<Referees>:
    canvas:
        Color:
            rgba: 1,1,1,1

        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: dp(4), dp(4), dp(4), dp(4)
            
    orientation: 'vertical'
    elevation: '4'
    size_hint_y: None
    height: dp(80)
    spacing: dp(8)
    padding: dp(8), dp(8), dp(8), dp(8)
    group: 'a'


    BoxLayout:
        size_hint_y: None
        height: dp(64)
        
        BoxLayout:
            size_hint_x:None
            width: dp(80)
            Widget:
                canvas:
                    Color:
                        rgba: 1,1,1,1

                    Ellipse:
                        source: 'pics/user_name.jpg'
                        size: self.size
                        pos: self.pos

                    Color:
                        rgba: 1,1,1,1

                    SmoothLine:
                        ellipse: self.x,self.y, self.width, self.height
                size_hint:None,None
                size: dp(64),dp(64)
                pos_hint: {'center_x':.5, 'center_y':.5}

        BoxLayout:
            orientation: 'vertical'
            MDLabel:
                text: root.username
                font_style: 'Subhead'
                size_hint_y: None
                height: dp(15)
                shorten: True
                shorten_from: 'right'
            MDLabel:
                text: root.email
                size_hint_y: None
                height: dp(15)
                color: 0,0,0,.63
                shorten: True
                shorten_from: 'right'
            BoxLayout:


<List_BaskW>:
    canvas:
        Color:
            rgba: (1,1,1,1)

        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: dp(4), dp(4), dp(4), dp(4)

    orientation: 'vertical'
    size_hint: .8, None
    height: dp(245)
    pos_hint:{'center_x':.5}
    padding: 0,dp(32),0,0
    opacity: .5
    
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(8)

        MDLabel:
            text: '[sup]KES[/sup] %s'%root.price
            size_hint_y: None
            height: dp(15)
            font_size: '20sp'
            halign: 'center'

        BoxLayout:


        BoxLayout:
            canvas:
                Color:
                    rgba: 0,0,0,1

                Rectangle:
                    size: self.size
                    pos: self.pos
            size_hint: None, None
            size: dp(20), dp(2)
            pos_hint: {'center_x':.5, 'center_y':.5}

        BoxLayout: 
            
        MDLabel:
            text: 'Quantity %s'%root.quantity
            size_hint_y: None
            height: dp(15)
            halign: 'center'
            color: 0,0,0,.63
            
        MDLabel:
            text: "Date bought %s"%root.date_bought
            size_hint_y: None
            height: dp(15)
            halign: 'center'
            color: 0,0,0,.63

        MDLabel:
            text: "Bought from %s"%root.bought_from
            size_hint_y: None
            height: dp(15)
            halign: 'center'
            color: 0,0,0,.63

        MDLabel:
            text: 'Tag %s'%root.tag
            size_hint_y: None
            height: dp(15)
            halign: 'center'
            color: 0,0,0,.63

    FloatLayout:
        size_hint_y: None
        height: dp(64)
        id: box_tings


<CardBaskets>:
    canvas:
        Color:
            rgba: 34/255, 139/255,34/255, 1

        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: dp(4),dp(4),dp(4),dp(4)

        Color:
            rgba: 34/255, 139/255,34/255, 1

        RoundedRectangle:
            size: self.size[0], self.size[1]*1/4
            pos: self.pos[0], self.pos[1]+(self.size[1]*3/4)
            radius: dp(4),dp(4),dp(0),dp(0)

############################
        Color:
            rgba: 0/255,178/255, 238/255,1

        RoundedRectangle:
            size: self.size[0]-dp(8), self.size[1]+dp(8)
            pos: self.pos[0], self.pos[1]-dp(8)
            radius: dp(4),dp(4),dp(4),dp(4)

        Color:
            rgba: 0/255,178/255, 238/255,1

        RoundedRectangle:
            size: self.size[0]-dp(8), self.size[1]*1/4+dp(8)
            pos: self.pos[0], self.pos[1]+(self.size[1]*3/4)
            radius: dp(4),dp(4),dp(0),dp(0)
            
############################
            
        Color:
            rgba: 1,1,1,1

        RoundedRectangle:
            size: self.size[0]-dp(16), self.size[1]*3/4+dp(16)
            pos: self.pos[0], self.pos[1]-dp(16)
            radius: dp(0),dp(4),dp(8),dp(4)
            
    elevation: '1'
    size_hint: None, None
    orientation: 'vertical'
    padding: 0,0,0,dp(8)

    BoxLayout:
        canvas:
            Color:
                rgba: 1,1,1, 1

            RoundedRectangle:
                size:  self.size[0]-dp(16), self.size[1]+dp(16)
                pos:self.pos
                radius: dp(4),dp(4),dp(8),dp(0)
                
        size_hint_y: None
        height: root.height*1/4

        
    FloatLayout:
        size_hint_y: None
        height: dp(1)
        
        BoxLayout:
            canvas:
                Color:
                    rgba: 1,1,1,1

                Ellipse:
                    size: self.size
                    pos:self.pos

                Color:
                    rgba: 0,0,0, .53

                SmoothLine:
                    ellipse: self.x, self.y, self.width, self.height
                    width: 1
                    
            orientation: 'vertical'
            size_hint: None, None
            size: dp(82), dp(82)
            pos_hint:{'center_x':.5}
            y: self.parent.y - self.height/2

            BoxLayout:

            MDLabel:
                text: root.price
                halign:'center'
                font_style: 'Subhead'
                color: 0,0,0,1
                size_hint_y: None
                height: dp(15)
                pos_hint: {'center_y':.5}
                
            MDLabel:
                text: 'Price(Kshs)'
                halign:'center'
                color: 0,0,0,1
                font_size: '10sp'
                size_hint_y: None
                height: dp(15)
                pos_hint: {'center_y':.5}
            BoxLayout:

    BoxLayout:
        spacing: dp(8)
        size_hint_y: None
        height: dp(41)

    
    BoxLayout:
        spacing: dp(8)
        size_hint_y: None
        padding: dp(16),0,0,0
        height: dp(30)
    
        Label:
            text: u'\uF114'
            halign:'left'
            color: 0,0,0, .63
            size_hint: None, None
            size: dp(32), dp(15)
            font_size: '24sp'
            font_name: 'fonts/materialdesignicons-webfont.ttf'
           
        MDLabel:
            text:'Commission %s'%root.commission
            halign:'left'
            font_style: 'Subhead'
            color: 0,0,0, .63
            size_hint_y: None
            height: dp(15)
            
    BoxLayout:
        spacing: dp(8)
        size_hint_y: None
        height: dp(30)
        padding: dp(16),0,0,0
    
        Label:
            text: u'\uF076'
            halign:'left'
            font_name: 'fonts/materialdesignicons-webfont.ttf'
            color: 0,0,0, .63
            size_hint: None, None
            size: dp(32), dp(15)
            font_size: '20sp'

        MDLabel:
            text: "Quantity %s"%root.items
            font_style: 'Subhead'
            halign:'left'
            size_hint_y: None
            height: dp(15)
            color: 0,0,0, .63
            
    BoxLayout:
    

    Contained_button:
        id: btn_purchase
        text: 'PURCHASE'
        halign: 'center'
        size: dp(150), dp(30)
        color: (0,0,0, 1)
        pos_hint: {'center_x': .5, 'center_y':.5}


<Card_how_it_works>:
    elevation: '1'
    canvas:
        Color:
            rgba: 1,1,1, 1

        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: dp(4), dp(4),dp(4),dp(4)
        
    orientation: 'vertical'
    padding: dp(16),0,dp(16), dp(16)
    spacing: dp(8)
    size_hint: None, None
    
    Label:
        text: root.source
        font_name: 'fonts/materialdesignicons-webfont.ttf'
        font_size: '32sp'
        halign: 'center'
        valign: 'center'
        color: 0,0,0,.33
        

    MDLabel:
        text: root.title
        halign: 'center'
        valign: 'center'
        size_hint: 1, None
        height: dp(40)
        font_size: '15sp'
        pos_hint: {'center_y':.5}
        font_style: 'Subhead'
        color: 0,0,0, 1

    MDLabel:
        text: root.details
        halign: 'center'
        valign: 'center'
        size_hint: 1, None
        font_size: '11sp'
        height: dp(100)
        pos_hint: {'center_y':.5}
        font_style: 'Caption'
        color: 0,0,0, 1
    BoxLayout:


<Influential_ppl>:
    canvas:
        Color:
            rgba: 1,1,1,1

        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: dp(4), dp(4), dp(4), dp(4)
    orientation: 'vertical'
    elevation: '6'
    size_hint_y: None
    height: dp(95)
    spacing: dp(8)
    padding: dp(8), dp(8), dp(8), dp(8)


    BoxLayout:
        size_hint_y: None
        height: dp(79)
        spacing: dp(8)
        
        BoxLayout:
            size_hint_x:None
            width: dp(80)
            orientation: 'vertical'
            Widget:
                canvas:
                    Color:
                        rgba: 1,1,1,1

                    Ellipse:
                        source: 'pics/user_name.jpg'
                        size: self.size
                        pos: self.pos

                    Color:
                        rgba: 1,1,1,1

                    SmoothLine:
                        ellipse: self.x,self.y, self.width, self.height
                size_hint:None,None
                size: dp(64),dp(64)
                pos_hint: {'center_x':.5, 'center_y':.5}

            BoxLayout:

        BoxLayout:
            orientation: 'vertical'
            MDLabel:
                text: root.username
                font_style: 'Subhead'
                size_hint_y: None
                height: dp(15)
                shorten: True
                shorten_from: 'right'
                
            MDLabel:
                text: root.email
                size_hint_y: None
                height: dp(15)
                color: 0,0,0,.63
                shorten: True
                shorten_from: 'right'
            MDLabel:
                text: 'Reputation %s'%root.reputation
                size_hint_y: None
                height: dp(15)
                color: 0,0,0,.63

            Label:
                halign: 'left'
                font_name: 'fonts/materialdesignicons-webfont.ttf'
                size: self.texture_size
                text_size: self.width, None
                size_hint_y: None
                height: dp(15)
                text: "%s"%root.stars
                color: 1,1,0,1
            BoxLayout:
            
''')

class List_BaskW(Rounded_Shadow1):
    price = StringProperty('')
    quantity = StringProperty('')
    bought_from = StringProperty('')
    date_bought = StringProperty('')
    tag = StringProperty('')
    
class Referees(ToggleButtonBehavior, Rectangle_Shadow1):
    username = StringProperty()
    email = StringProperty()

    def on_state(self, inst, value):
        if value=='down':
            self.elevation = '0'
            self.badge_label = CoreLabel()
            self.badge_label.text = u'\uF12C'
            # the label is usually not drawn until needed, so force it to draw.
            self.badge_label.refresh()
            self.badget_texture = self.badge_label.texture

            #set the bg of the tint
            bg_tint_color = (Color( 28/255, 134/255,238/255, .63))
            bg_tint = RoundedRectangle(size=self.size, pos=self.pos,\
                                       radius=(dp(4),dp(4),dp(4),dp(4)))

            outline_roundrec = SmoothLine(rounded_rectangle=(self.x, self.y,self.width,self.height, dp(4)),\
                                    width =dp(2))

            #set the bg of the circle
##            ellipse_bg_color = (Color(46/255, 139/255, 87/255, 1))
##            ellipse_bg = Ellipse(size=(dp(64), dp(64)),\
##                                 pos = (self.x+self.width/2-dp(32), self.y+self.height/2-dp(32)))
##
##            #set the text
##            ellipse_txt_color = Color(1,1,1,1)
##            ellipse_txt = Ellipse(texture=self.badget_texture,\
##                                  size=(dp(16), dp(16)), \
##                                  pos=(ellipse_bg.pos[0] + dp(8), ellipse_bg.pos[1] + dp(8)))

            #add to the canvas
            self.canvas.after.add(bg_tint_color)
            self.canvas.after.add(outline_roundrec)

##            self.canvas.after.add(ellipse_bg_color)
##            self.canvas.after.add(ellipse_bg)
##
##            self.canvas.after.add(ellipse_txt_color)
##            self.canvas.after.add(ellipse_txt)
        elif value == 'normal':
            self.canvas.after.clear()
            self.elevation = '4'


class Pple_W(Rectangle_Shadow1):
    username = StringProperty()
    acc_no = StringProperty()
    email = StringProperty()
    baskets = StringProperty()
    referees = StringProperty()

    def __init__(self, **kwargs):
        super(Pple_W, self).__init__(**kwargs)

    def show_baskets(self, instance):
        self.basketss = ast.literal_eval(self.baskets)
        if instance.text=='Show basket list':
            instance.text = 'Hide basket list'
            if len(self.basketss) ==0:
                self.empt_lbl = Label(text='The person has no basket',\
                                        height=dp(30), color=(0,0,0,.4),\
                                        halign = 'center', size_hint_y=None)
                self.add_widget(self.empt_lbl)
                self.height += dp(38)
            else:
                for bask in self.basketss:
                    wid = Bask_purchase(price = str(bask[0]),\
                                        acc_no = str(bask[1]))
                    
                    wid.ids.btn_purchase.bind(on_release=partial(self.puchase_smn_basket,wid))
                    self.ids.box1.add_widget(wid)
                    
                    self.ids.box1.height+=dp(38)
                    self.height+=dp(38)
                    
        elif instance.text=='Hide basket list':
            instance.text = 'Show basket list'
            if len(self.basketss) ==0:
                self.remove_widget(self.empt_lbl)
                self.height -= dp(38)
            else:
                self.ids.box1.clear_widgets()
                self.height = dp(111)
                self.ids.box1.height = dp(0)
                

    def puchase_smn_basket(self, inst, *args):
        dialog_c = DialogConfirm(title='Confirm',\
                        desc='Are you sure you want to purchase basket price %s from %s'%(inst.price, self.username),\
                                size=(Window.size[0]-dp(16)  if int(Window.size[0]) < 304 else dp(304), dp(150)) )
        self.modal_bask_buy = ModalView(size_hint = (None, None),\
                                    background_color=(0,0,0,.5),\
                                    size=(Window.size[0]-dp(16)  if int(Window.size[0]) < 304 else dp(304), dp(150)),auto_dismiss = True,\
                                    background='pics/invisible.png')
        self.modal_bask_buy.add_widget(dialog_c)
        self.modal_bask_buy.open()
        dialog_c.ids.btn_purchase1.bind(on_release = partial(self.puchase_smn_basket1, inst) )
        dialog_c.ids.btn_purchase.bind(on_release = lambda *x: self.modal_bask_buy.dismiss())

    def puchase_smn_basket1(self, inst, *args):
        self.modal_bask_buy.dismiss()
        th = threading.Thread(target=self.puchase_smn_basket_th, args=(inst,))
        th.start()

    def puchase_smn_basket_th(self, inst, *args):
        email_buyer = self.parent.parent.parent.parent\
                      .parent.parent.parent.parent.parent.email

        res = self.parent.parent.parent.parent\
            .parent.parent.parent.parent.parent.request({'type':'puchase_smn_basket1',\
                                    'email_buyer': email_buyer,\
                                    'email_seller': self.email,\
                                     'acc_no': inst.acc_no,\
                                     'price': inst.price,\
                                     'seller_username': self.username,\
                                     'referee': self.referees})
        
        

        if res['results']=='bask_finished':
            self.parent.parent.parent.parent\
                      .parent.parent.parent.parent.parent.showDialogOk('Information', 'Sorry %s has sold all of his baskets'%self.username)
        elif res['results'] =='success':
            self.parent.parent.parent.parent\
                      .parent.parent.parent.parent.parent.showDialogOk('Information', 'You have successfully bought basket price %s'%inst.price)
            
        self.parent.parent.parent.parent\
                      .parent.parent.parent.parent.parent.Load_myBaskets()



class Notif_P(Rounded_Shadow1):
    buyer = StringProperty()
    price = StringProperty()
    date = StringProperty()


class Influential_ppl(Rounded_Shadow_t1):
    username = StringProperty()
    email = StringProperty()
    reputation = StringProperty()
    stars = StringProperty()


class CardBaskets(Rounded_Shadow1):
    price = StringProperty('')
    commission = StringProperty('')
    items = StringProperty('')

class Card_how_it_works(Rounded_Shadow1):
    title = StringProperty('')
    details = StringProperty('')
    color=ListProperty()
    source = StringProperty('')

class Bask_purchase(Rounded_Shadow1):
    price = StringProperty()
    acc_no = StringProperty()

