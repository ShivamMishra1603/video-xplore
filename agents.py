import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from logger import log_info, log_error, log_debug

class AgentManager:
    
    def __init__(self):
        self._multimodal_agent = None
    
    def get_multimodal_agent_with_keys(self, google_api_key, phi_api_key=None):
        """Create agent with user-provided API keys"""
        log_info("Initializing multimodal agent with user keys")
        
        # Create tools list
        tools = []
        if phi_api_key:
            # Use phi_api_key if provided
            tools.append(DuckDuckGo())
        else:
            # Use DuckDuckGo without phi key (free tier)
            tools.append(DuckDuckGo())
        
        agent = Agent(
            name="Video AI Summarizer",
            model=Gemini(model_name="gemini-2.0-flash", api_key=google_api_key),
            tools=tools,
            markdown=True,
            show_tool_calls=True
        )
        log_info("Multimodal agent initialized successfully with user keys")
        return agent
    
    # @st.cache_resource
    # def get_multimodal_agent(_self):
    #     if _self._multimodal_agent is None:
    #         log_info("Initializing multimodal agent")
    #         _self._multimodal_agent = Agent(
    #             name="Video AI Summarizer",
    #             model=Gemini(model_name="gemini-2.0-flash"),
    #             tools=[DuckDuckGo()],
    #             markdown=True,
    #             show_tool_calls=True
    #         )
    #         log_info("Multimodal agent initialized successfully")
    #     return _self._multimodal_agent
    
    def run_analysis_with_keys(self, prompt, google_api_key, phi_api_key=None, videos=None):
        try:
            agent = self.get_multimodal_agent_with_keys(google_api_key, phi_api_key)
            log_debug("Running analysis with agent using user keys")
            return agent.run(prompt, videos=videos)
        except Exception as e:
            log_error("Agent analysis failed", e)
            raise
    
    # def run_analysis(self, prompt, videos=None):
    #     try:
    #         agent = self.get_multimodal_agent()
    #         log_debug("Running analysis with agent")
    #         return agent.run(prompt, videos=videos)
    #     except Exception as e:
    #         log_error("Agent analysis failed", e)
    #         raise

agent_manager = AgentManager()