from concurrent.futures import ThreadPoolExecutor

class AsyncExecutor:
    def __init__(self):
        self.pool = ThreadPoolExecutor(max_workers=12)

    async def execute_tool(self, tool_name: str, params: dict):
        """异步执行工具调用"""
        return await asyncio.get_event_loop().run_in_executor(
            self.pool, 
            lambda: TOOLS[tool_name].run(params)
        )