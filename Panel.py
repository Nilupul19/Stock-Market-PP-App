import streamlit as st
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
import MainDashboard




if not firebase_admin._apps:
  cred = credentials.Certificate('stock-market-pp-app-44c07bf74076.json')
  firebase_admin.initialize_app(cred)



def app():
   
   	
   if 'username' not in st.session_state:
     st.session_state.username = ''
   
   if 'email' not in st.session_state:
     st.session_state.email = ''

   


   def check_login():

      try:
          user = auth.get_user_by_email(email)
          #print(user.uid)
          st.success('User Login Successfully')
          st.balloons()


          st.session_state.username = user.uid
          st.session_state.email = user.email

          st.session_state.signedout = True
          st.session_state.maindashboard = True
         

      except:
          st.warning('Login failed!')

   def register_user():
        
       user = auth.create_user(email = email, password = password, uid = username)
       st.success('User Registered Successfully!')
       st.markdown('Please Login using your email and password')
       st.balloons()
       


   if 'signedout' not in st.session_state:
      st.session_state.signedout = False

   if 'maindashboard' not in st.session_state:
      st.session_state.maindashboard = False

   if st.session_state.maindashboard:
        MainDashboard.app()   
   
   if not st.session_state['signedout']:
     st.title('Welcome To :blue[Login/Signup Page]')
     choice = st.selectbox('Login/Signup', ['Login','Signup'])
   
   
     if choice == 'Login':
                   
                   email = st.text_input('email')
                   password = st.text_input('password', type='password')
                   
                   st.button('Login', on_click=check_login)
                  

     elif choice == 'Signup':

                   email = st.text_input('email')
                   password = st.text_input('password', type='password')
                   username = st.text_input('username')
      	
                   st.button('Register', on_click=register_user)

                   

