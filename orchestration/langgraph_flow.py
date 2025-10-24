# orchestration/langgraph_flow.py
import logging, os, sys

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# --- Minimal Graph + Node simulation for visualizer ---
class Node:
    def __init__(self, fn):
        self.fn = fn


class Graph:
    def __init__(self, name=""):
        self.name = name
        self.nodes = {}
        self.edges = []

    def add_node(self, name, node):
        self.nodes[name] = node

    def connect(self, src, dest):
        self.edges.append((src, dest))

    def get_node(self, name):
        return self.nodes[name]


# --- Import Agents and Tools ---
from agents.user_input_agent import UserInputAgent
from agents.destination_agent import DestinationAgent
from agents.weather_agent import WeatherAgent
from agents.itinerary_agent import ItineraryAgent
from agents.budget_agent import BudgetAgent
from agents.result_agent import ResultAggregator
from tools.mcp_client import MCPClient
from tools.metrics_tool import MetricsTracker


logging.basicConfig(filename="logs/agent_logs.txt", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


def build_holiday_planner_flow():
    graph = Graph(name="HolidayPlannerFlow")

    # Add nodes
    graph.add_node("user_input", Node(UserInputAgent()))
    graph.add_node("destination_agent", Node(DestinationAgent()))
    graph.add_node("weather_agent", Node(WeatherAgent()))
    graph.add_node("itinerary_agent", Node(ItineraryAgent()))
    graph.add_node("budget_agent", Node(BudgetAgent()))
    graph.add_node("result_aggregator", Node(ResultAggregator()))

    # Define connections
    graph.connect("user_input", "destination_agent")
    graph.connect("destination_agent", "weather_agent")
    graph.connect("weather_agent", "itinerary_agent")
    graph.connect("itinerary_agent", "budget_agent")
    graph.connect("budget_agent", "result_aggregator")

    return graph


def run_holiday_planner_flow(user_data: dict):
    metrics = MetricsTracker()
    mcp = MCPClient()
    try:
        logging.info("Starting HolidayPlanner flow")
        graph = build_holiday_planner_flow()
        state = {"user_input": user_data}
        metrics.log_event("start_workflow", {"input": user_data})

        # Sequential execution
        for step in [
            "user_input",
            "destination_agent",
            "weather_agent",
            "itinerary_agent",
            "budget_agent",
            "result_aggregator",
        ]:
            node = graph.get_node(step).fn
            state = node.run(state)
            metrics.log_event(f"{step}_complete")

        metrics.log_event("workflow_complete", {"status": "success"})
        logging.info("HolidayPlanner flow completed successfully")
        return state

    except Exception as e:
        logging.error(f"Flow error: {e}")
        metrics.log_event("workflow_failed", {"error": str(e)})
        return {"error": str(e)}
