import tempfile
import time
from pathlib import Path
import streamlit as st
from google.generativeai import upload_file, get_file

class VideoProcessor:
    
    def __init__(self):
        self.temp_video_path = None
    
    def process_uploaded_file(self, video_file):
        if video_file is None:
            return None
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
            temp_file.write(video_file.read())
            self.temp_video_path = temp_file.name
        
        return self.temp_video_path
    
    def upload_to_gemini(self, video_path):
        if not video_path:
            raise ValueError("Video path is required")
        
        processed_video = upload_file(video_path)
        
        while processed_video.state.name == "PROCESSING":
            time.sleep(1)
            processed_video = get_file(processed_video.name)
        
        return processed_video
    
    def cleanup_temp_file(self):
        if self.temp_video_path:
            Path(self.temp_video_path).unlink(missing_ok=True)
            self.temp_video_path = None
    
    def display_video_preview(self, video_path):
        if video_path:
            st.video(video_path, format="video/mp4", start_time=0)

video_processor = VideoProcessor()