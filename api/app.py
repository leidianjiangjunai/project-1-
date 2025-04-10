from fastapi import FastAPI
from agents.supervisor import SupervisorAgent
from services.async_engine import AsyncEngine

app = FastAPI()
supervisor = SupervisorAgent()
engine = AsyncEngine()

@app.post("/query")
async def handle_query(query: str):
    # 分层处理流程
    plan = supervisor.plan_execution(query)
    
    # 多阶段校验
    validation_results = await engine.execute_validation(plan)
    
    # 缓存检查
    if cached := cache.query_cache(query):
        return cached
    
    # 异步执行查询
    results = await engine.batch_execute([
        partial(get_stock_price, symbol),
        partial(get_financial_data, symbol, year)
    ])
    
    # 结果校验和格式处理
    return format_response(results)