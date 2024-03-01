# import streamlit as st
# import streamlit.components.v1 as components
# st.title('🎈 Data Storyboard')
# components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQuRgMB0NvkKx8b2ZLPgiDUBZyQBFLLHAUJQq40fTFoZD15sMo1Vj9dEBxs3kfIlQYOne-PFGZUiIsU/embed?start=false&loop=false&delayms=3000", height=480)

import streamlit as st
import streamlit.components.v1 as components

st.title('🎈Presentation from Google Slides')

# Get user input for Google Slides link
slide_link = st.text_input('Enter your Google Slides link', 'https://docs.google.com/presentation/d/')

# Check if the input link is valid
if slide_link and slide_link != 'https://docs.google.com/presentation/d/':
    # Extract the presentation ID from the link
    presentation_id = slide_link.split('/')[-2]

    # Construct the iframe URL with the presentation ID
    iframe_url = f'https://docs.google.com/presentation/d/e/{presentation_id}/embed?start=false&loop=false&delayms=3000'

    # Display the Google Slides presentation in an iframe
    components.iframe(iframe_url, height=480)
else:
    st.write('Please enter a valid Google Slides link.')
# Adding the HTML footer
# Profile footer HTML for sidebar
sidebar_footer_html = """
<div style="text-align: left;">
    <p style="font-size: 16px;"><b>Author: 🌟 Rizwan Rizwan 🌟</b></p>
    <a href="https://github.com/Rizwankaka"><img src="https://img.shields.io/badge/GitHub-Profile-blue?style=for-the-badge&logo=github" alt="GitHub"/></a><br>
    <a href="https://www.linkedin.com/in/rizwan-rizwan-1351a650/"><img src="https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn"/></a><br>
    <a href="https://twitter.com/RizwanRizwan_"><img src="https://img.shields.io/badge/Twitter-Profile-blue?style=for-the-badge&logo=twitter" alt="Twitter"/></a><br>
    <a href="https://www.facebook.com/RIZWANNAZEEER"><img src="https://img.shields.io/badge/Facebook-Profile-blue?style=for-the-badge&logo=facebook" alt="Facebook"/></a><br>
    <a href="mailto:riwan.rewala@gmail.com"><img src="https://img.shields.io/badge/Gmail-Contact%20Me-red?style=for-the-badge&logo=gmail" alt="Gmail"/></a>
</div>
"""

# Render profile footer in sidebar at the "bottom"
st.sidebar.markdown(sidebar_footer_html, unsafe_allow_html=True)
# Set a background image
def set_background_image():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.pexels.com/photos/6847584/pexels-photo-6847584.jpeg");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background_image()

# Set a background image for the sidebar
sidebar_background_image = '''
<style>
[data-testid="stSidebar"] {
    background-image: url("https://images.pexels.com/photos/6101958/pexels-photo-6101958.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
    background-size: cover;
}
</style>
'''

st.sidebar.markdown(sidebar_background_image, unsafe_allow_html=True)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Custom CSS to inject into the Streamlit app
footer_css = """
<style>
.footer {
    position: fixed;
    right: 0;
    bottom: 0;
    width: auto;
    background-color: transparent;
    color: black;
    text-align: right;
    padding-right: 10px;
}
</style>
"""

# HTML for the footer - replace your credit information here
footer_html = f"""
<div class="footer">
    <p>Credit: Dr. Aammar Tufail | Phd | Data Scientist | Bioinformatician (<a href="https://www.youtube.com/@Codanics" target="_blank">CODANICS</a>)</p>
</div>
"""

# Combine CSS and HTML for the footer
st.markdown(footer_css, unsafe_allow_html=True)
st.markdown(footer_html, unsafe_allow_html=True)