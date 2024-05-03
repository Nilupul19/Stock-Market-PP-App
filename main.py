import streamlit as st
from streamlit_option_menu import option_menu
import Panel,MainDashboard




class MultiApp:

	def __init__(self):
		self.apps = []

	def add_app(self,title,function):
	   self.apps.append({
         "title": title,
         "function": function
	   	})
def run():

        with st.sidebar:
	        app = option_menu(
             menu_title='Side Bar',
             options=['Panel','MainDashboard'],
             icons=['house-fill','trophy-fill'],
             menu_icon='abacus',
             default_index=1,
                              )
        
        if app == 'Panel':    	  		
		       Panel.app()
        if app == 'Signout':
                     Signout.app()
	                	            
run()         