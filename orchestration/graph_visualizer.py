# orchestration/graph_visualizer.py
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


import pydot
from orchestration.langgraph_flow import build_holiday_planner_flow

def generate_flow_diagram():
    graph = build_holiday_planner_flow()
    
    # Use pydot instead of pygraphviz
    dot_graph = pydot.Dot(graph_type='digraph', rankdir='LR', bgcolor="white")

    # Add nodes and edges
    for node_name in graph.nodes:
        dot_graph.add_node(pydot.Node(node_name, shape="box", style="rounded,filled", fillcolor="#a6cee3"))

    for edge in graph.edges:
        src, dest = edge
        dot_graph.add_edge(pydot.Edge(src, dest, color="#1f78b4"))

    dot_graph.write_png("data/graph_flow.png")
    print("✅ Flow diagram saved as data/graph_flow.png")

if __name__ == "__main__":
    generate_flow_diagram()
