import streamlit as st 
st.write("Hello, you've signed in!")
st.write("Now, you can play the game using the following command in the command line")
st.write("<executable> -u <username> -p <password>")

if st.button("Close Window"):
    close_script = """
    <script>
        window.close();
    </script>
    """
    st.markdown(close_script, unsafe_allow_html=True)