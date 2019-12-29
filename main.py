import kivy
from kivy.app import App
from kivy.boxlayout import Boxlayout
from kivy.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.config import Config

Config.set('graphics','resizable',1)
kivy.require('1.9.0')

class CalcLayot(GridLayout):
  def calculate(self,calculation):
    if calculation:
      try:
        self.d_equation.text=str(eval(calculation))
      except Error:
        self.d_equation.text="ERROR"
  


class CalculatorApp(self):
  def build(self):
    return CalcLayout()

if __name__="__main":
  CalculatorApp().run()
