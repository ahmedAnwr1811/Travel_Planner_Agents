from crewai import Crew, Process
from config.settings import llm
from agents.agents import create_agents
from tasks.tasks import create_tasks
from datetime import datetime

def get_user_inputs():
    """Collect travel inputs dynamically from the user."""
    print("=== Travel Planner ===")
    
    # Destination
    destination = input("Enter your destination (e.g., Paris, France): ").strip()
    
    # Travel dates
    while True:
        start_date = input("Enter start date (YYYY-MM-DD): ").strip()
        end_date = input("Enter end date (YYYY-MM-DD): ").strip()
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
            if end > start:
                break
            else:
                print("End date must be after start date. Try again.")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

    # Number of travelers
    while True:
        try:
            travelers = int(input("Enter number of travelers: ").strip())
            if travelers > 0:
                break
            else:
                print("Number of travelers must be positive.")
        except ValueError:
            print("Please enter a valid number.")

    # Budget
    while True:
        try:
            budget = float(input("Enter total budget (in USD): ").strip())
            if budget > 0:
                break
            else:
                print("Budget must be positive.")
        except ValueError:
            print("Please enter a valid number.")

    return {
        "destination": destination,
        "travel_dates": {
            "start": start_date,
            "end": end_date
        },
        "travelers": travelers,
        "budget": budget
    }

def main():
    # Get dynamic user inputs
    travel_inputs = get_user_inputs()

    # Initialize crew
    travel_crew = Crew(
        agents=create_agents(),
        tasks=create_tasks(travel_inputs),  # Pass travel_inputs to tasks
        process=Process.sequential,
        verbose=True,
        memory=True,
        manager_llm=llm
    )

    # Execute crew
    result = travel_crew.kickoff(inputs=travel_inputs)

    # Output results
    print("\n=== Travel Plan ===")
    print(result)
    with open("travel_plan.md", "w", encoding="utf-8") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()