import tempfile
import time
from pathlib import Path
import streamlit as st
from google.generativeai import upload_file, get_file
from logger import log_info, log_error, log_debug, log_warning

class VideoProcessor:
    
    def __init__(self):
        self.temp_video_path = None
    
    def process_uploaded_file(self, video_file):
        if video_file is None:
            log_debug("No video file provided")
            return None
        
        try:
            log_info(f"Processing video file: {video_file.name}")
            
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
                temp_file.write(video_file.read())
                self.temp_video_path = temp_file.name
            
            log_info("Video file processed successfully")
            return self.temp_video_path
            
        except Exception as e:
            log_error("Failed to process video file", e)
            raise
    
    def upload_to_gemini(self, video_path):
        if not video_path:
            log_error("Video path is required for Gemini upload")
            raise ValueError("Video path is required")
        
        try:
            log_info("Starting video upload to Gemini")
            start_time = time.time()
            
            processed_video = upload_file(video_path)
            log_debug("Video uploaded to Gemini, waiting for processing")
            
            while processed_video.state.name == "PROCESSING":
                time.sleep(1)
                processed_video = get_file(processed_video.name)
            
            duration = time.time() - start_time
            log_info(f"Video processing completed in {duration:.2f}s")
            
            return processed_video
            
        except Exception as e:
            log_error("Failed to upload video to Gemini", e)
            raise
    
    def cleanup_temp_file(self):
        if self.temp_video_path:
            try:
                Path(self.temp_video_path).unlink(missing_ok=True)
                log_debug("Temporary video file cleaned up")
                self.temp_video_path = None
            except Exception as e:
                log_warning("Failed to cleanup temporary file")
    
    def display_video_preview(self, video_path):
        if video_path:
            st.video(video_path, format="video/mp4", start_time=0)

video_processor = VideoProcessor()