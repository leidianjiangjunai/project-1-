from infrastructure.vector_db import VectorStorage

storage = VectorStorage()
storage.add_documents([
    {"content": "苹果公司2023年股价数据", "source": "market_data"},
    {"content": "谷歌2022年财务报表", "source": "sec_filings"}
])