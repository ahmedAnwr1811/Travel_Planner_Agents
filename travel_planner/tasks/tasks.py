from crewai import Task
from agents.agents import create_agents

def create_tasks(travel_inputs):
    agents = create_agents()
    travel_advisor, flight_agent, hotel_agent, tour_guide, budget_planner = agents

    # Extract inputs
    destination = travel_inputs["destination"]
    start_date = travel_inputs["travel_dates"]["start"]
    end_date = travel_inputs["travel_dates"]["end"]
    travelers = travel_inputs["travelers"]
    budget = travel_inputs["budget"]

    travel_advice_task = Task(
        description=f"Provide an overview of travel tips for {destination}, including visa requirements, best time to visit, and cultural etiquette for {travelers} travelers planning a trip from {start_date} to {end_date}.",
        expected_output="A concise summary of travel tips, visa information, and cultural guidelines in Markdown format.",
        agent=travel_advisor
    )

    flight_task = Task(
        description=f"Search for round-trip flights to {destination} for {travelers} travelers, departing on {start_date} and returning on {end_date}. Prioritize low-cost options with layovers under 4 hours. Provide flight details including airlines, times, layovers, and prices.",
        expected_output="A list of flight options with airlines, departure/arrival times, layovers, and total prices in Markdown format.",
        agent=flight_agent
    )

    hotel_task = Task(
        description=f"Find budget-friendly hotels or accommodations in {destination} for {travelers} travelers from {start_date} to {end_date}, within a ${budget} total budget. Include hotel names, locations, nightly rates, and amenities.",
        expected_output="A list of 3-5 hotel options with names, locations, nightly rates, and key amenities in Markdown format.",
        agent=hotel_agent
    )

    itinerary_task = Task(
        description=f"Create a detailed daily itinerary for a trip to {destination} from {start_date} to {end_date} for {travelers} travelers. Include major attractions, dining options, and local experiences.",
        expected_output="A day-by-day itinerary with activities, dining recommendations, and estimated costs in Markdown format.",
        agent=tour_guide
    )

    budget_task = Task(
        description=f"Compile a budget breakdown for a trip to {destination} for {travelers} travelers, ensuring the total cost stays within ${budget}. Include flights, accommodations, activities, dining, and transportation costs based on other agents' outputs.",
        expected_output="A detailed budget table with cost estimates for each category and a total cost in Markdown format.",
        agent=budget_planner
    )

    return [travel_advice_task, flight_task, hotel_task, itinerary_task, budget_task]