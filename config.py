import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class Config:
    
    def __init__(self):
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self._configure_apis()
        self._load_prompt_templates()
    
    def _configure_apis(self):
        if self.google_api_key:
            genai.configure(api_key=self.google_api_key)
        else:
            st.error("Google API key not found")
            st.stop()
    
    @property
    def page_config(self):
        return {
            "page_title": "VideoXplore",
            "page_icon": "🎥",
            "layout": "wide"
        }
    
    @property
    def supported_video_formats(self):
        return ["mp4", "mov", "avi", "mkv"]
    
    @property
    def search_depth_options(self):
        return {
            "Basic": "1-2 relevant searches",
            "Detailed": "3-5 comprehensive searches", 
            "Comprehensive": "5-8 thorough searches covering multiple angles"
        }
    
    @property
    def focus_areas_options(self):
        return [
            "Latest trends", 
            "Expert opinions", 
            "Statistics", 
            "Case studies", 
            "Technical details"
        ]
    
    @property
    def default_focus_areas(self):
        return ["Latest trends", "Expert opinions"]
    
    def _load_prompt_templates(self):
        self.video_only_prompt = os.getenv("VIDEO_ONLY_PROMPT_TEMPLATE")
        self.web_research_prompt = os.getenv("WEB_RESEARCH_PROMPT_TEMPLATE") 
        self.web_research_instruction = os.getenv("WEB_RESEARCH_INSTRUCTION_TEMPLATE")
        
        if not all([self.video_only_prompt, self.web_research_prompt, self.web_research_instruction]):
            raise ValueError("Prompt templates must be set in .env file. See env_example.txt for format.")

config = Config()