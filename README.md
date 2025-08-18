# VideoXplore

**AI-Powered Video Analysis & Research Platform**

VideoXplore is a modular Streamlit application that combines advanced video analysis with intelligent web research to provide comprehensive insights from video content. Built with Google's Gemini AI and enhanced with real-time web search capabilities.

![Output](public/images/Output.png)

## Demo


![Travel Video Demo](public/videos/TravelVideo.gif)


## Features

- **Video Analysis**: Upload and analyze videos using Google Gemini's multimodal AI
- **Smart Web Research**: Supplement video insights with current web information via DuckDuckGo
- **Configurable Analysis**: Customizable search depth and focus areas
- **Modern UI**: Clean, responsive interface built with Streamlit
- **Modular Architecture**: Well-structured, maintainable codebase
- **Customizable Prompts**: Configure AI prompts via environment variables
- **Export Results**: Download analysis reports as text files


## Quick Start

### Prerequisites

- Python 3.8+
- Google API key with Gemini access
- Phidata API key
- Internet connection for web research

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd VideoXplore
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Copy the example file
   cp env_example.txt .env
   
   # Edit .env and add your Google API key
   GOOGLE_API_KEY=your_google_api_key_here
   PHI_API_KEY=your_phi_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501`

## Usage

### Video Analysis

1. **Upload a video** - Supports MP4, MOV, AVI, and MKV formats
2. **Enter your query** - Describe what insights you want from the video
3. **Configure options** (optional) - Set search depth and focus areas
4. **Analyze** - Click the "Analyze Video" button

### Advanced Features

#### Web Research Integration
- **Toggle web research** on/off
- **Choose search depth**: Basic, Detailed, or Comprehensive
- **Focus areas**: Latest trends, Expert opinions, Statistics, Case studies, Technical details

#### Analysis Results
- **Video Analysis**: Direct insights from video content
- **Web Research Findings**: Current information with clickable source links
- **Export capability**: Download reports as text files


## Configuration

### Environment Variables

Create a `.env` file with the following variables:

```bash
GOOGLE_API_KEY=your_google_api_key_here
PHI_API_KEY=your_phi_api_key_here

VIDEO_ONLY_PROMPT_TEMPLATE="Your custom video analysis prompt..."
WEB_RESEARCH_PROMPT_TEMPLATE="Your custom web research prompt..."
WEB_RESEARCH_INSTRUCTION_TEMPLATE="Your custom research instruction..."
```

### Prompt Customization

VideoXplore supports fully customizable AI prompts through environment variables. This allows you to:

- **Modify analysis style** - Change tone, detail level, or format
- **Adjust output structure** - Customize how results are presented
- **Add domain expertise** - Include specialized knowledge or terminology
- **A/B test prompts** - Experiment with different approaches

See `env_example.txt` for complete prompt templates.

## Development

### Project Structure

- **`app.py`** - Main application entry point and UI layout
- **`config.py`** - Configuration management and API setup
- **`agents.py`** - AI agent initialization with caching
- **`video_processor.py`** - Video file handling and Gemini integration
- **`ui_components.py`** - Reusable UI components and styling
- **`analysis.py`** - Analysis logic and prompt generation

### Key Design Principles

- **Modular Architecture** - Each module has a single responsibility
- **Environment-driven Configuration** - All settings via environment variables
- **Caching** - Streamlit caching for performance optimization
- **Error Handling** - Graceful error handling with user feedback
- **Clean Code** - Minimal, readable code without unnecessary comments



## Dependencies

- **streamlit** - Web application framework
- **phidata** - AI agent framework with tool integration
- **google-generativeai** - Google Gemini API client
- **duckduckgo-search** - Web search functionality
- **python-dotenv** - Environment variable management


## Troubleshooting

### Common Issues

**"Google API key not found"**
- Ensure your `.env` file contains `GOOGLE_API_KEY=your_key_here`
- Verify the API key has Gemini access enabled

**"Prompt templates must be set in .env file"**
- Copy prompt templates from `env_example.txt` to your `.env` file
- Ensure all three prompt templates are defined

**Video processing errors**
- Check video file format (MP4, MOV, AVI, MKV supported)
- Ensure stable internet connection for Gemini API
- Verify video file size is within API limits

**Module import errors**
- Run `pip install -r requirements.txt`
- Ensure you're using Python 3.8+


