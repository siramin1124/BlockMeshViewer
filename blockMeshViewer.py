
# kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.graphics import Line
#from kivy3 import Renderer, Scene

#import platform
#print(platform.python_version())


class blockMeshViewer(App):
    title = "First Simple Code"

    def build(self):
        widget = Widget()

        with widget.canvas:
            Color(1, 1, 0, .5)
            Line(points=[100, 50, 350, 250, 350, 50], width=10, close='True')

        return widget

    def on_touch_move(self, touch):
        print(touch.profile)


blockMeshViewer().run()
