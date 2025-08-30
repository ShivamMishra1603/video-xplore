import streamlit as st
import time
from config import config

class UIComponents:
    
    @staticmethod
    def apply_custom_css():
        st.markdown(
            """
            <style>
            .stTextArea textarea {
                height: 100px;
            }
            .step-header {
                color: #1f77b4;
                font-weight: bold;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    
    @staticmethod
    def setup_page():
        st.set_page_config(**config.page_config)
        st.title("VideoXplore")
        st.subheader("AI-Powered Video Analysis & Research")
    
    @staticmethod
    def create_api_key_inputs():
        st.markdown("Enter your Google AI Studio API key to get started. [Get API Key](https://aistudio.google.com/app/apikey)")
        
        google_api_key = st.text_input(
            "Google AI Studio API Key",
            type="password",
            placeholder="Enter your Google AI Studio API key",
            help="Required for video analysis. Get it from Google AI Studio"
        )
        
        return google_api_key
    
    @staticmethod
    def create_video_uploader():
        st.markdown("### 📹 Video Upload")
        return st.file_uploader(
            label="Upload a video file",
            type=config.supported_video_formats,
            help="Upload a video file to analyze"
        )
    
    @staticmethod
    def create_query_input():
        return st.text_area(
            "What insights are you seeking from this video?",
            placeholder="e.g., Summarize the main points, What are the key takeaways?, Analyze the speaker's arguments...",
            help="Be specific about what you want to learn from the video",
            height=100
        )
    
    @staticmethod
    def create_advanced_options():
        with st.expander("Advanced Search Options", expanded=False):
            include_web_research = st.checkbox(
                "Include web research", 
                value=True, 
                help="Supplement video analysis with web search"
            )
            
            search_depth = st.selectbox(
                "Search depth", 
                ["Basic", "Detailed", "Comprehensive"], 
                index=1
            )
            
            focus_areas = st.multiselect(
                "Focus research on:",
                config.focus_areas_options,
                default=config.default_focus_areas
            )
        
        return include_web_research, search_depth, focus_areas
    
    @staticmethod
    def create_analyze_button():
        return st.button(
            "Analyze Video", 
            key="analyze_video_button", 
            use_container_width=True
        )
    
    @staticmethod
    def display_analysis_results(response_content):
        st.markdown(response_content)
    
    @staticmethod
    def create_download_button(user_query, response_content):
        analysis_text = f"""# Video Analysis Report
Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}

## User Query
{user_query}

## Analysis Results
{response_content}
"""
        st.download_button(
            label="Download Analysis Report",
            data=analysis_text,
            file_name=f"video_analysis_{int(time.time())}.txt",
            mime="text/plain",
            use_container_width=True
        )
    
    @staticmethod
    def display_web_research_details(response):
        if hasattr(response, 'tool_calls') and response.tool_calls:
            with st.expander("Web Research Details", expanded=False):
                st.write("**Search queries performed:**")
                for i, tool_call in enumerate(response.tool_calls, 1):
                    if 'duckduckgo' in str(tool_call).lower():
                        st.write(f"{i}. {tool_call}")
    
    @staticmethod
    def show_info_messages():
        st.info("Upload a video file to start analysis")
    
    @staticmethod
    def show_waiting_message():
        st.info("Enter your query and click 'Analyze Video' to see results here")

ui = UIComponents()