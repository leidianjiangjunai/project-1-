from pydantic import BaseSettings
from pydantic import Field
import yaml

class Settings(BaseSettings):
    # 模型配置
    LLM_PROVIDER: str = "deepseek"
    LLM_MODEL: str = "deepseek-chat"
    API_KEY: str = Field(..., env="DEEPSEEK_API_KEY")
    
    # 缓存配置
    CACHE_THRESHOLD: float = 0.85
    MAX_CACHE_ITEMS: int = 5000
    
    # 并发控制
    MAX_CONCURRENT: int = 12
    REQUEST_TIMEOUT: int = 8
    
    # 向量数据库
    VECTOR_STORE: str = "faiss"
    EMBEDDING_MODEL: str = "paraphrase-mpnet-base-v2"
    
    class Config:
        env_file = ".env"

class Settings(BaseSettings):
    @validator('VALID_SYMBOLS', pre=True)
    def load_symbols(cls, v):
        with open('config/symbols.yaml') as f:
            return yaml.safe_load(f)['stock_symbols']

config = Settings()