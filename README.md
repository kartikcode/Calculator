# Calculator
Kivy based code, very efficient one for understanding the Kivy workflow.<br>
I personally find this simple project to be a real must if someone wishes to fully understand the Kivy GUI.<br><br><br>
Of course, run it on your terminal with python3 installed on it.<br>
While installing Kivy, make sure its compatible with python3 or else its gonna make your life tough:)
<br>
# Running it through a virtual environment<br>
There is some sort of a bug in Ubuntu 18.0.4 which causes a lot of trouble.<br>
An easy cure is that you run it in a python3 virtual environment.<br>
Run in the folllowing code on your terminal for doing so:
Install Python 3 virtual environment creator

sudo apt install virtualenv python3-virtualenv

Create a Python virtual environment for python3. You can only install python3 packages inside this Python virtual environment. If you also want to install Python 2.x packages, then you need to make another Python virtual environment.

virtualenv -p python3 env  
source ./env/bin/activate

The new Python virtual environment for python3 will be created in the env directory which is located in the current directory.
```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

