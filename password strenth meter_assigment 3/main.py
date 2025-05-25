import streamlit as st
import re

st.set_page_config(page_title="Passworrd Strength Meter", page_icon="🔒")
st.title("🔒Passworrd Strength Meter")
st.markdown("""
## Welcome to the password strength builder
 use this tool & secure your app with **Stronge Password Generator**
            """)
password  = st.text_input("Enter Your Password",type="password")
feedback =[]
score = 0
if password:
    if len(password)>= 8:
     score += 1
else:feedback.append("password should cuntain both upper and lower case characters.")
if re.search(r'\d',password):
    score += 1
else :feedback.append("password should cuntain one digit.")

if re.search(r'[!@#$%^&*)_+-=}{;:?/>.<,|\\]',password):
  score+= 1

else:
    feedback.append("password should cuntain one special character.")
if score==4:
    feedback.append ("your password is strong")

if score==3:
    feedback.append ("your password is normal strenth.if you think batter do more stronge")
else: 
 feedback.append ("your password is weak strenth.do more stronge")

if feedback.append:st.markdown("##improvement suggestion")
for tip in feedback:
   st.write(tip)
#else:st.info("enter your password") 
