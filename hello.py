import streamlit as st 
import webbrowser
import streamlit.components as components

st.write("Hello, you've signed in!")
st.write("Now, you can play the game using the following command in the command line")
st.write("<executable> -u <username> -p <password>")

def close_window():
    # JavaScript to close the window
    js = """
        <script>
            window.parent.window.close();
            // Fallback for browsers that block window.close()
            window.parent.location.href = "about:blank";
        </script>
        """
    components.html(js, height=0)

# Create a button that triggers the close function
if st.button("Close Application"):
    close_window()