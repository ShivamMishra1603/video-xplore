from config import config
from agents import agent_manager

class AnalysisEngine:
    
    def __init__(self):
        pass
    
    def generate_analysis_prompt(self, user_query, include_web_research, search_depth, focus_areas):
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
    
    def run_analysis(self, prompt, processed_video):
        return agent_manager.run_analysis(prompt, videos=[processed_video])
    
    def validate_query(self, user_query):
        return bool(user_query and user_query.strip())

analysis_engine = AnalysisEngine()