from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from noti import Ournoti,Loginnoti
from kivy.uix.widget import Widget
from kivy.core.window import Window

Builder.load_file('calculator.kv')
Builder.load_file('loginsystem.kv')
Builder.load_file('noti.kv')
Builder.load_file('history.kv')

class HistoryScreen(Screen):
   

    def __init__(self, **kwargs):
        super(HistoryScreen, self).__init__(**kwargs)
        self.myinformation = [ {'text': x, "font_size":"20sp"} for x in open("write.txt","r").readlines()]
        self.ids.recycle_view_id.data = self.myinformation
        self.ids.recycle_view_id.refresh_from_data()
        
        
class RegistrationScreen(Screen):
    def registerUser(self):
        uname = self.ids.username.text
        passwd = self.ids.password.text
        confirm_pass = self.ids.confirm_pass.text
     
        if uname != "" and passwd != "" and passwd == confirm_pass:
               
            f = open("all,acc&pass.txt","a")
            f.write( uname + "#" + passwd + "\n")
            f.close()
            p = Ournoti()
            p.open()
    def goToLoginScreen(self):
        self.manager.current = "login"

class LoginScreen(Screen):
    def checklogin(self):
        input_user = self.ids.username.text
        input_pass = self.ids.password.text
        
        checker = False

        f = open("all,acc&pass.txt","r")   
        for user in f:
            p = user.split("#")

            uname = p[0]
            passwd = p[1][0:len(p[1])-1]
            
            if uname == input_user and passwd == input_pass:
                checker = True
                self.manager.current= 'Calculator'
        
        
        if checker == False:
            pop = LoginPopup()
            pop.open()

    def goToRegisterPage(self):
        self.manager.current ='register' 

class Calculator(Screen):
    
    def clearInput(self):            
        self.ids.input_field.text="0"
    def buttonClicked(self,n):
        if self.ids.input_field.text == "0":
            self.ids.input_field.text = n
        else:
            self.ids.input_field.text = self.ids.input_field.text + n
    def HistoryClicked(self):
        self.manager.current ='HistoryScreen'            
    def calculate(self):
        e = open("write.txt","a")
        e.write(self.ids.input_field.text+'='+str(eval(self.ids.input_field.text) )+'\n')
        self.ids.input_field.text = str(eval(self.ids.input_field.text))
    def oppositesign(self):
        self.ids.input_field.text = str(-eval(self.ids.input_field.text))
    def clearonedigit(self):
        prev = self.ids.input_field.text
        self.ids.input_field.text = prev[0:len(prev)-1 ]
        if len(prev) == 1:
            self.ids.input_field.text = "0"

SB = ScreenManager()
SB.add_widget(RegistrationScreen(name='register'))
SB.add_widget(LoginScreen(name ='login'))
SB.add_widget(Calculator(name ='Calculator'))
SB.add_widget(HistoryScreen(name ='HistoryScreen'))


class Myapp(App):
    def build(self):
        return SB

if __name__=='__main__':
    Myapp().run()