# 🌍 Travel Planner Agents

An AI-powered travel planning system built with CrewAI that uses multiple specialized agents to create comprehensive travel itineraries. The system collects user preferences and coordinates between different AI agents to provide personalized travel recommendations, flight options, accommodations, and detailed itineraries.

## ✨ Features

- **Multi-Agent Coordination**: Five specialized AI agents working together
- **Dynamic Input Collection**: Interactive prompts for destination, dates, budget, and travelers
- **Comprehensive Planning**: Covers flights, hotels, activities, and budget management
- **Intelligent Search**: Uses SerperDev for real-time web search capabilities
- **Markdown Output**: Generates well-formatted travel plans saved as Markdown files

## 🤖 AI Agents

The system employs five specialized agents, each with unique expertise:

### 1. Travel Advisor 🗺️
- **Role**: Provides personalized travel recommendations
- **Expertise**: Global cultures, local customs, off-the-beaten-path destinations
- **Output**: Visa requirements, cultural etiquette, travel tips

### 2. Flight Specialist ✈️
- **Role**: Finds optimal flight options
- **Expertise**: Airline systems, fare structures, route optimization
- **Output**: Round-trip flights with prices, layovers, and airlines

### 3. Hotel Specialist 🏨
- **Role**: Identifies suitable accommodations
- **Expertise**: Hospitality industry, property evaluation, value assessment
- **Output**: Budget-friendly hotels with amenities and locations

### 4. Tour Guide 📍
- **Role**: Creates detailed daily itineraries
- **Expertise**: Local attractions, cultural experiences, activity planning
- **Output**: Day-by-day schedules with attractions and dining

### 5. Budget Planner 💰
- **Role**: Ensures financial feasibility
- **Expertise**: Travel economics, cost optimization, budget allocation
- **Output**: Detailed budget breakdown with cost estimates

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key
- SerperDev API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Travel_Planner_Agents
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   SERPER_API_KEY=your_serper_api_key_here
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

## 📋 Required Dependencies

Create a `requirements.txt` file with the following packages:

```txt
crewai
langchain-openai
crewai-tools
python-dotenv
```

## 🎯 Usage

1. **Start the application**
   ```bash
   python main.py
   ```

2. **Follow the interactive prompts**:
   - Enter your destination (e.g., "Paris, France")
   - Specify travel dates (YYYY-MM-DD format)
   - Number of travelers
   - Total budget in USD

3. **Wait for processing**
   - The agents will work sequentially to gather information
   - Progress will be displayed in the terminal

4. **Review your travel plan**
   - Results are displayed in the terminal
   - A detailed plan is saved as `travel_plan.md`

## 📁 Project Structure

```
Travel_Planner_Agents/
├── main.py                 # Entry point and user interaction
├── travel_planner.py       # Alternative entry point
├── travel_plan.md          # Generated travel plan output
├── .env                    # Environment variables (create this)
├── requirements.txt        # Python dependencies (create this)
├── agents/
│   ├── __init__.py
│   └── agents.py          # AI agent definitions and creation
├── config/
│   ├── __init__.py
│   └── settings.py        # Configuration and API setup
└── tasks/
    ├── __init__.py
    └── tasks.py           # Task definitions for each agent
```

## ⚙️ Configuration

### API Keys Setup

The application requires two API keys:

1. **OpenAI API Key**
   - Sign up at [OpenAI](https://platform.openai.com)
   - Generate an API key from your dashboard
   - Uses GPT-4o-mini model for cost efficiency

2. **SerperDev API Key**
   - Sign up at [SerperDev](https://serper.dev)
   - Get your API key for web search capabilities

### Model Configuration

The system uses GPT-4o-mini with the following settings:
- Temperature: 0.7 (balanced creativity)
- Max tokens: 4096 (comprehensive responses)

## 🔧 Customization

### Adding New Agents

1. Define new agent in `agents/agents.py`:
   ```python
   new_agent = Agent(
       role="Your Role",
       goal="Your Goal",
       backstory="Your Backstory",
       verbose=True,
       llm=llm,
       tools=[search_tool]
   )
   ```

2. Add corresponding task in `tasks/tasks.py`
3. Update the crew initialization in `main.py`

### Modifying Agent Behavior

Edit the `backstory` and `goal` parameters in `agents/agents.py` to change how agents approach their tasks.

## 📝 Output Format

The system generates travel plans in Markdown format including:

- **Travel Tips**: Visa requirements, cultural guidelines
- **Flight Options**: Airlines, schedules, prices, layovers
- **Accommodations**: Hotels with rates and amenities
- **Daily Itinerary**: Activities, dining, local experiences
- **Budget Breakdown**: Detailed cost analysis by category

## 🐛 Troubleshooting

### Common Issues

1. **Missing API Keys**
   ```
   ValueError: OPENAI_API_KEY not set in .env file
   ```
   **Solution**: Ensure your `.env` file contains valid API keys

2. **Import Errors**
   ```
   ModuleNotFoundError: No module named 'crewai'
   ```
   **Solution**: Install dependencies with `pip install -r requirements.txt`

3. **Date Format Errors**
   ```
   Invalid date format. Use YYYY-MM-DD.
   ```
   **Solution**: Enter dates in the correct format (e.g., 2025-07-15)

---

*Built with ❤️ using CrewAI and OpenAI*
