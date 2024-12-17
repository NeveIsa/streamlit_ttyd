import streamlit as st
from streamlit_ttyd import terminal
import time 

st.text("Terminal showing processes running on your system using the top command")

# start the ttyd server and display the terminal on streamlit
ttydprocess, port = terminal(cmd="top")

# info on ttyd port
st.text(f"ttyd server is running on port : {port}")

# kill the ttyd server after a minute
time.sleep(60)
ttydprocess.kill()
