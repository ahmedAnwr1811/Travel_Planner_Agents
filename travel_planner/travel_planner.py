from crewai import Agent
from config.settings import llm, search_tool

def create_agents():
    travel_advisor = Agent(
        role="Travel Advisor",
        goal="Provide personalized travel recommendations for a memorable trip.",
        backstory="An experienced travel consultant with deep knowledge of global destinations, cultures, and logistics.",
        verbose=True,
        llm=llm,
        tools=[search_tool]
    )

    flight_agent = Agent(
        role="Flight Specialist",
        goal="Find the best round-trip flight options, prioritizing low-cost options with short layovers.",
        backstory="A seasoned expert in navigating flight booking systems and finding cost-effective travel solutions.",
        verbose=True,
        llm=llm,
        tools=[search_tool]
    )

    hotel_agent = Agent(
        role="Hotel Specialist",
        goal="Identify comfortable and budget-friendly accommodations.",
        backstory="A hospitality expert with extensive knowledge of hotels and lodging options worldwide.",
        verbose=True,
        llm=llm,
        tools=[search_tool]
    )

    tour_guide = Agent(
        role="Tour Guide",
        goal="Plan a detailed daily itinerary with must-see attractions and local experiences.",
        backstory="A local expert with a passion for sharing the history, culture, and hidden gems of destinations.",
        verbose=True,
        llm=llm,
        tools=[search_tool]
    )

    budget_planner = Agent(
        role="Budget Planner",
        goal="Ensure the trip stays within the specified budget, allocating funds for flights, accommodations, and activities.",
        backstory="A financial expert skilled in budget optimization for travel planning.",
        verbose=True,
        llm=llm
    )

    return [travel_advisor, flight_agent, hotel_agent, tour_guide, budget_planner]