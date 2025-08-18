import streamlit as st

from config import config
from ui_components import ui
from video_processor import video_processor
from analysis import analysis_engine

ui.setup_page()
ui.apply_custom_css()

left_col, right_col = st.columns([1, 1])

with left_col:
    st.subheader("Video Upload & Settings")
    
    video_file = ui.create_video_uploader()
    
    if video_file:
        video_path = video_processor.process_uploaded_file(video_file)
        video_processor.display_video_preview(video_path)
        
        st.divider()
        
        st.subheader("Analysis Configuration")
        
        user_query = ui.create_query_input()
        
        include_web_research, search_depth, focus_areas = ui.create_advanced_options()
        
        analyze_button = ui.create_analyze_button()
    else:
        user_query = ""
        include_web_research = True
        search_depth = "Detailed"
        focus_areas = config.default_focus_areas
        analyze_button = False

with right_col:
    st.subheader("Analysis Results")
    
    if video_file and analyze_button:
        if not analysis_engine.validate_query(user_query):
            st.warning("Please enter a query to analyze the video")
        else:
            try:
                with st.spinner("Analyzing video and conducting web research..."):
                    processed_video = video_processor.upload_to_gemini(video_path)
                    
                    analysis_prompt = analysis_engine.generate_analysis_prompt(
                        user_query, include_web_research, search_depth, focus_areas
                    )
                    
                    response = analysis_engine.run_analysis(analysis_prompt, processed_video)

                ui.display_analysis_results(response.content)
                
                st.divider()
                
                if include_web_research:
                    ui.display_web_research_details(response)
                
                ui.create_download_button(user_query, response.content)

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
            finally:
                video_processor.cleanup_temp_file()
    
    elif not video_file:
        ui.show_info_messages()
    else:
        ui.show_waiting_message()