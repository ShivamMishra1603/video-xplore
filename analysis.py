import time
from config import config
from agents import agent_manager
from logger import log_info, log_error, log_debug, log_warning

class AnalysisEngine:
    
    def __init__(self):
        pass
    
    def generate_analysis_prompt(self, user_query, include_web_research, search_depth, focus_areas):
        log_debug("Generating analysis prompt")
        
        if not include_web_research:
            return self._generate_video_only_prompt(user_query)
        
        return self._generate_web_research_prompt(user_query, search_depth, focus_areas)
    
    def _generate_video_only_prompt(self, user_query):
        return config.video_only_prompt.format(user_query=user_query)
    
    def _generate_web_research_prompt(self, user_query, search_depth, focus_areas):
        focus_text = ", ".join(focus_areas) if focus_areas else "general information"
        search_intensity = config.search_depth_options[search_depth]
        
        web_research_instruction = config.web_research_instruction.format(
            search_intensity=search_intensity,
            focus_text=focus_text
        )
        
        return config.web_research_prompt.format(
            user_query=user_query,
            web_research_instruction=web_research_instruction
        )
    
    def run_analysis_with_keys(self, prompt, processed_video, google_api_key, phi_api_key=None):
        try:
            log_info("Starting analysis with agent using user keys")
            start_time = time.time()
            
            response = agent_manager.run_analysis_with_keys(
                prompt, 
                google_api_key, 
                phi_api_key, 
                videos=[processed_video]
            )
            
            duration = time.time() - start_time
            log_info(f"Analysis completed successfully in {duration:.2f}s")
            
            return response
            
        except Exception as e:
            log_error("Analysis failed", e)
            raise
    
    # def run_analysis(self, prompt, processed_video):
    #     try:
    #         log_info("Starting analysis with agent")
    #         start_time = time.time()
    #         
    #         response = agent_manager.run_analysis(prompt, videos=[processed_video])
    #         
    #         duration = time.time() - start_time
    #         log_info(f"Analysis completed successfully in {duration:.2f}s")
    #         
    #         return response
    #         
    #     except Exception as e:
    #         log_error("Analysis failed", e)
    #         raise
    
    def validate_query(self, user_query):
        is_valid = bool(user_query and user_query.strip())
        if not is_valid:
            log_warning("Invalid query provided")
        return is_valid

analysis_engine = AnalysisEngine()