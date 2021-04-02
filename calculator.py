from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
''
Window.size = (500,700)

class Mylayout(Widget):
    def clearInput(self):
        self.ids.input_field.text="0"
    def buttonClicked(self,n):
        if self.ids.input_field.text == "0":
            self.ids.input_field.text = n
        else:
            self.ids.input_field.text = self.ids.input_field.text + n

    def calculate(self):
        self.ids.input_field.text = str(eval(self.ids.input_field.text))
    def oppositesign(self):
        self.ids.input_field.text = str(-eval(self.ids.input_field.text))
    def clearonedigit(self):
        prev = self.ids.input_field.text
        self.ids.input_field.text = prev[0:len(prev)-1 ]
        if len(prev) == 1:
            self.ids.input_field.text = "0"

''
class CalculatorApp(App):

    def build(self):
       return Mylayout()   


if __name__=="__main__":
    CalculatorApp().run()
