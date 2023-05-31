import streamlit as st

page_bg_img = """
<style>
[data-testid = "stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1640340434855-6084b1f4901c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8dHJhZGluZ3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60");
background-size: cover;
}
[data-testid = "stSidebar"] {
background-image: url("https://images.unsplash.com/photo-1651347589091-8f9f43a1e42c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=387&q=80");
background-position : center;

}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.sidebar.success("Select a page above.")

st.header (" :mailbox: Get In Touch With Us!")

contact_form = """
<form action="https://formsubmit.co/suhasigadge0907@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder= "Your Name" required>
     <input type="email" name="email" placeholder= "Your Email"  required>
     <textarea name="message" placeholder="Your Message Here"></textarea>
     <button type="submit">Send</button>
</form>

"""

st.markdown(contact_form, unsafe_allow_html = True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")