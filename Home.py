import streamlit as st
import pandas as pd


from streamlit_option_menu import option_menu



# 2. horizontal menu
selected2 = option_menu(None, ["Home", "Installation"], 
    icons=None,
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={"nav-link-selected": {"background-color": " #0047AB"}})


if selected2 == "Home": 


    st.title("Welcome to PIP Manager")

    st.write(
    """
PIP Manager is designed to make Python Package handling easier by just a click of a button!!

    """
        )


    col1, col2 = st.columns(2)

    with col1:
        f = st.expander(label="Available Features")
        
        f.write(
"""
- Installing packages
- Upgrading packages (Installing if they are not already)
- Uninstalling packages
- Upgrading pip
- Test Importing. (If the module is not on your machine it will auto download.)
- Dark mode | can be enabled in the 'settings' tab (Defaulted)
- Built-In Console | This console is a live feed of the CMD but simplified for easier reading
- 'settings' tab | This has two current settings and they are saved in a json file for saved configurations
- Threading (Developed by Cole Bohanon) | This prevents the freezing of the app and allows for a live feed to the CMD
- Package List Tab (Displays all packages and colorizes the outdated ones in red, right click on the package to get a menue of "Upgrade or Uninstall" Be sure to select the Package before you do this.)
- Auto-Py-to-EXE function in the settings tab.

"""
        )
        sg = st.expander(label="Saftey/Guidelines")
        sg.write(
            """
- We do not recommend installing any packages you are not familiar with.
- We do not recommend installing packages that may require log in information, unless its trusted by the Python Community
- We are not resopnsible for faulty or virus enbeded packages that are installed through this Software.

            """
        )

    with col2:
        s = st.expander(label="Requirements")
        #st.header("Requirements")

        s.write(
"""
This app does require some third party packages. But don't worry the app will detect if you have them or not and it will ask you if you want to install them in a CMD. From here you can also start in CLI mode instead of installing the packages. NOTE: features are limited in CLI Mode. Here are the required packages:
"""

        )

        s.code("ttkthemes")
        s.code("win32gui & win32con")




if selected2 == "Installation":
    st.title("Installation")


    col1, col2 = st.columns(2)


    with col1:
        st.header("Zip File Download")
        st.button(label="Download", key="https://github.com/blaze005/PIP-Manager-App/archive/refs/tags/3.1.zip")


