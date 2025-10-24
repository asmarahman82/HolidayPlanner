# agents/budget_agent.py
import logging

class BudgetAgent:
    def run(self, data: dict):
        logging.info("BudgetAgent: estimating budget")
        # Very simple estimate: base daily cost + food/activities
        base_daily = 100
        duration = int(data.get("duration", 1))
        estimate = base_daily * duration
        # if user budget < estimate, flag it
        flagged = data.get("budget", 0) < estimate
        data["budget_estimate"] = {"estimate": estimate, "flagged": flagged}
        logging.info(f"BudgetAgent: estimate={estimate}, flagged={flagged}")
        return data
