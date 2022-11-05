import streamlit as st
# from StateManagement.StateManagement import StateManagement


class UploadWidget:
    def __init__(self):
        # State = StateManagement()

        try:
            # upload signal
            uploadedSignals = st.file_uploader(
                "Upload Signal", type=["csv", "wav", "mp3"], key='uploadButton', on_change=self.change_upload_value)

        except Exception as e:
            st.error(e)

    def change_upload_value(self):
        pass