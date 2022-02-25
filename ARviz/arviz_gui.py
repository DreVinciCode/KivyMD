#!/usr/bin/python3

import rospy
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton



class KivyMD_GUI(MDApp):
	
	def __init_(self, **kwargs):
		super().__init__(**kwargs)
		
		self.screen=Builder.load_file('/home/dre/catkin_ws/src/SENSAR_ROS/turtlebot/KivyMD/ARViz/ros_gui.kv')


	def build(self):
		self.screen = Screen()
		self.screen.add_widget(
            MDRectangleFlatButton(
                text="Worked!",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
		return self.screen

if __name__ == "__main__":
	rospy.init_node('kivymd_gui', anonymous=True)

	KivyMD_GUI().run()