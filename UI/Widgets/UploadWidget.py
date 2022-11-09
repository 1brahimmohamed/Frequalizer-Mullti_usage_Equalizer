import streamlit as st
from state_management.state_management import state_management

class UploadWidget:
    def __init__(self):
        State = state_management()

        try:
            # upload signal
            uploadedSignals = st.file_uploader(
                "Upload Signal", type=["wav"], key='uploadButton', on_change=self.change_upload_value)

            if (uploadedSignals is not None):
                State.save_file(uploadedSignals)

        except Exception as e:
            st.error("Error Occur while uploading the file")

    def change_upload_value(self):
        pass