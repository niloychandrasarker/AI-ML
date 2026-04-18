import streamlit as st
import PIL as Image
from api_calling import Issue, code_solution_genarator

st.title("AI Code Debugger App")
st.markdown(
    """`    This app uses the Gemini API to debug code snippets. Simply input your code and let the AI identify and fix any issues!`
    """ )
st.divider()

#Sidebar
with st.sidebar:
    st.header("Controls")
    #image uploader
    images = st.file_uploader(
        "upload your error code snippet screenshot",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
    )

    pil_images = []
    for image in images:
        pil_image = Image.open(image)
        pil_images.append(pil_image)

    if images:
        if len(images) > 5:
           st.error("Please upload a maximum of 5 images.")
        else:
            st.subheader("Uploaded Error Code Snippets")
            col = st.columns(len(images))
            for i, image in enumerate(images):
                with col[i]:
                    st.image(image)
    
    #Dificulty level
    selected_optiopn = st.selectbox(
        "select you want to get",
        ("Hints","solution with code"),
        index=None,
    )



    pressed = st.button("Generate Solution",type="primary")

if pressed:
    if not images:  
        st.error("Please upload at least one image of your error code snippet.")
    if not selected_optiopn:
        st.error("Please select an option for the solution.")

    if images and selected_optiopn:
        #notes
        with st.container(border=True): 
            st.subheader("Solution")
            with st.spinner("Generating solution..."):
                hints = Issue(pil_images)
                st.write(hints)

        with st.container(border=True): 
            st.subheader("Code Solution")
            with st.spinner("Generating code solution..."):
                code_solution = code_solution_genarator(pil_images, selected_optiopn)
                st.markdown(code_solution)