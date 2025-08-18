import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo

class AgentManager:
    
    def __init__(self):
        self._multimodal_agent = None
    
    @st.cache_resource
    def get_multimodal_agent(_self):
        if _self._multimodal_agent is None:
            _self._multimodal_agent = Agent(
                name="Video AI Summarizer",
                model=Gemini(model_name="gemini-2.0-flash"),
                tools=[DuckDuckGo()],
                markdown=True,
                show_tool_calls=True
            )
        return _self._multimodal_agent
    
    def run_analysis(self, prompt, videos=None):
        agent = self.get_multimodal_agent()
        return agent.run(prompt, videos=videos)

agent_manager = AgentManager()