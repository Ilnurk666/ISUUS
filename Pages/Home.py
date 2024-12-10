import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image

class Home:
    def __init__(self):
        self.lottie = self.load_lottieurl("https://lottie.host/dfd6bdbf-e3e5-4694-bc02-2d1501878b1d/dlNALUv7yv.json")
        self.toni = Image.open("img/gavno.png")

    def load_lottieurl(self, url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()



    def app(self):

        with st.container():
            st.title("Welcome to the Home page")
        with st.container():
            st.write("---")
            lef, righ = st.columns(2)
            with lef:
                st.header("Introduction")
                st.write("This project (streamlit) will analyze any dataset and create a user-friendly table and also "
                         "create graphs with any values from dataset. And contain the content from football team.")
            with righ:
                st_lottie(self.lottie, height=300, key="coding")

        with st.container():
            st.header("Manchester City")
            imageg, teext = st.columns((1, 2))
            with imageg:
                st.image(self.toni)
            with teext:
                st.subheader("Manchester city team")
                st.write(
                    """
                    This video show to us content from Manchester City team
                    """
                )
                st.markdown("[Watch Video...](https://youtu.be/nIZxFNgYWOc?si=YMXqYIUgbUmR0gpc)")