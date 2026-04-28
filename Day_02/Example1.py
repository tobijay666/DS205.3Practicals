class BaseTool:
    def execute(self, task: str) -> str:
        raise NotImplementedError("Tools must implement execute()")

# CalculatorTool: Inherited from BaseTool
class CalculatorTool(BaseTool):
    def execute(self, task: str) -> str:
        return f"Calculating: {task}"

# The Agent: Composition & Dependency Injection
class Agent:
    def __init__(self, tool: BaseTool):
        self._tool = tool # Dependency Injected

    def run(self, task: str):
        # Polymorphism: Agent doesn't care HOW the tool works
        return self._tool.execute(task)
    
