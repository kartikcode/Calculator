import kivy 
from kivy.app import App 
kivy.require('1.9.0')
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
Config.set('graphics', 'resizable', 1) 




class CalcGridLayout(GridLayout): 

	def calculate(self, calculation): 
		if calculation: 
			try: 
				self.d_equation.text = str(eval(calculation)) 
			except Exception: 
				self.d_equation.text = "Error"

class CalculatorApp(App): 

	def build(self): 
		return CalcGridLayout() 

myApp = CalculatorApp() 
myApp.run() 

