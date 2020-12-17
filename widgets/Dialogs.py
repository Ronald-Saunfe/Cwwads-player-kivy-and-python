from kivy.lang import Builder
from widgets.Shadows import *

Builder.load_string('''

<DialogOk>:
    canvas:
        Color:
            rgba: 1,1,1,1

        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: dp(4),dp(4),dp(4),dp(4)
    elevation: '6'
    orientation: 'vertical'
    padding: dp(8), dp(16), dp(8), dp(16)
    spacing: dp(8)

    MDLabel:
        text: root.title
        valign: 'middle'
        font_style: 'Title'

    MDLabel:
        text: root.desc
        valign: 'middle'

    Text_Button:
        id: btn_ok
        text: 'Ok'
        size: dp(120), dp(30)
        font_style: 'Subhead'
        halign: 'center'
        color: (45/255, 11/255, 250/255, 1)
        pos_hint: {'center_x':.5, 'center_y':.5}
        

<DialogConfirm>:
    canvas:
        Color:
            rgba: 1,1,1,1

        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: dp(4),dp(4),dp(4),dp(4)
    elevation: '6'
    orientation: 'vertical'
    padding: dp(8), dp(16), dp(8), dp(16)
    spacing: dp(8)

    MDLabel:
        text: root.title
        valign: 'middle'
        font_style: 'Title'

    MDLabel:
        text: root.desc
        valign: 'middle'

    BoxLayout:
        size_hint: None,None
        size: dp(168), dp(30)
        spacing: dp(8)
        pos_hint: {'center_y':.5, 'right':1}
        
        Text_Button:
            id: btn_purchase
            text: 'NO'
            size: dp(80), dp(30)
            font_style: 'Subhead'
            halign: 'center'
            color: (45/255, 11/255, 250/255, 1)
            pos_hint: {'center_x':.5, 'center_y':.5}

        Text_Button:
            id: btn_purchase1
            text: 'YES'
            size: dp(80), dp(30)
            font_style: 'Subhead'
            halign: 'center'
            color: (45/255, 11/255, 250/255, 1)
            pos_hint: {'center_x':.5, 'center_y':.5}
            
<Change_Email>:
    canvas:
        Color:
            rgba: 1,1,1,1

        Rectangle:
            size: self.size
            pos: self.pos
            
    orientation: 'vertical'
    padding: dp(16), dp(8), dp(16),dp(8)
    spacing: dp(8)

    MDLabel:
        text: 'Change Email'
        font_name: 'fonts/Montserrat-Medium.ttf'
        size_hint_y: None
        height: dp(30)
        pos_hint:{'center_y':.5}

    NewTextinput:
        id: txt_email
        cursor_color: 45/255, 11/255, 250/255, 1
        hint_text: 'Enter email'
        pos_hint:{'center_y':.5}

    Contained_button:
        id: btn_chng
        text: 'CHANGE'
        size_hint:1,None
        height: dp(30)
        pos_hint:{'center_y':.5}
        
<Change_Usr>:
    canvas:
        Color:
            rgba: 1,1,1,1

        Rectangle:
            size: self.size
            pos: self.pos
            
    orientation: 'vertical'
    padding: dp(16), dp(8), dp(16),dp(8)
    spacing: dp(8)

    MDLabel:
        text: 'Change Username'
        font_name: 'fonts/Montserrat-Medium.ttf'
        size_hint_y: None
        height: dp(30)
        pos_hint:{'center_y':.5}

    NewTextinput:
        id: txt_usr
        cursor_color: 45/255, 11/255, 250/255, 1
        hint_text: 'Enter username'
        pos_hint:{'center_y':.5}

    Contained_button:
        id: btn_change
        text: 'CHANGE'
        size_hint:1,None
        height: dp(30)
        pos_hint:{'center_y':.5}

<Change_Pass>:
    canvas:
        Color:
            rgba: 1,1,1,1

        Rectangle:
            size: self.size
            pos: self.pos
            
    orientation: 'vertical'
    padding: dp(16), dp(8), dp(16),dp(8)
    spacing: dp(8)
    
    MDLabel:
        text: 'Change Password'
        font_name: 'fonts/Montserrat-Medium.ttf'
        size_hint_y: None
        height: dp(30)
        pos_hint:{'center_y':.5}
        
    NewTextinput:
        id: txt_newp
        cursor_color: 45/255, 11/255, 250/255, 1
        hint_text: 'Enter New password'
        password: True

    NewTextinput:
        id: txt_confrmp
        cursor_color: 45/255, 11/255, 250/255, 1
        hint_text: 'Confirm password'
        password: True

    Contained_button:
        id: btn_chng
        text: 'CHANGE'
        size_hint:1,None
        height: dp(30)   

<Recov_Dialog>:
    canvas:
        Color:
            rgba: 1,1,1,1

        Rectangle:
            size: self.size
            pos: self.pos
            
    orientation: 'vertical'
    padding: dp(16), dp(8), dp(16),dp(8)

    FloatLayout:
        size_hint_y: None
        height: dp(15)

        Icon_label_toggle:
            id: lbl_close
            n_text: u'\uF156'
            d_text: u'\uF156'
            size_hint: None, None
            size: dp(32), dp(32)
            color: 0,0,0,.63
            pos_hint:{'center_y':.5}
            x: root.x+root.width-self.width- dp(8)

    ScreenManager:
        id: sm
        Screen:
            name: 'one'

            BoxLayout:
                spacing: dp(8)
                orientation: 'vertical'

                MDLabel:
                    text: 'Reset Password'
                    font_name: 'fonts/Montserrat-Medium.ttf'
                    size_hint_y: None
                    height: dp(30)
                    pos_hint:{'center_y':.5}

                NewTextinput:
                    id: txt_email
                    cursor_color: 45/255, 11/255, 250/255, 1
                    hint_text: 'Enter email address'
                    pos_hint:{'center_y':.5}

                Contained_button:
                    id: btn_email
                    text: 'RESET'
                    size_hint:1,None
                    height: dp(30)
                    pos_hint:{'center_y':.5}
        Screen:
            name: 'two'

            BoxLayout:
                spacing: dp(8)
                orientation: 'vertical'

                MDLabel:
                    text: 'Recovery Key'
                    text_style: 'Subhead'
                    size_hint_y: None
                    height: dp(30)

                NewTextinput:
                    id: txt_recover
                    cursor_color: 45/255, 11/255, 250/255, 1
                    hint_text: 'Enter recovery key'  

                Contained_button:
                    id: btn_recover
                    text: 'RECOVER'
                    size_hint:1,None
                    height: dp(30)
        Screen:
            name: 'passwd'

            BoxLayout:
                spacing: dp(8)
                orientation: 'vertical'

                MDLabel:
                    text: 'Reset password'
                    text_style: 'Subhead'
                    size_hint_y: None
                    height: dp(15)

                NewTextinput:
                    id: txt_newp
                    cursor_color: 45/255, 11/255, 250/255, 1
                    hint_text: 'Enter New password'
                    password: True

                NewTextinput:
                    id: txt_confrmp
                    cursor_color: 45/255, 11/255, 250/255, 1
                    hint_text: 'Confirm password'
                    password: True

                Contained_button:
                    id: btn_cont
                    text: 'CONTINUE'
                    size_hint:1,None
                    height: dp(30)
                    
''')

class Recov_Dialog(Rounded_Shadow1):
    pass

class Change_Email(Rectangle_Shadow1):
    pass

class Change_Usr(Rectangle_Shadow1):
    pass

class Change_Pass(Rectangle_Shadow1):
    pass


class DialogConfirm(Rounded_Shadow1):
    title = StringProperty('')
    desc = StringProperty('')

class DialogOk(Rounded_Shadow1):
    title = StringProperty('')
    desc = StringProperty('')
