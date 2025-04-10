from langchain_openai import ChatOpenAI
from pydantic import BaseModel

class LLMAdapterConfig(BaseModel):
    provider: str = "deepseek"
    model_name: str = "deepseek-chat"
    api_key: str
    temperature: float = 0.1
    max_tokens: int = 2048
    api_base: str = "https://api.deepseek.com/v1"

class LLMAdapter:
    def __init__(self, config: LLMAdapterConfig):
        if config.provider not in self.provider_mapping:
            raise ValueError(f"不支持的提供商: {config.provider}")
        try:
            self.llm = self.provider_mapping[config.provider](config)
        except Exception as e:
            raise ConnectionError(f"模型初始化失败: {str(e)}")

    def _init_deepseek(self, config):
        return ChatOpenAI(
            model=config.model_name,
            openai_api_base=config.api_base,
            openai_api_key=config.api_key,
            temperature=config.temperature,
            max_tokens=config.max_tokens
        )

    def _init_openai(self, config):
        return ChatOpenAI(
            model_name=config.model_name,
            openai_api_key=config.api_key,
            temperature=config.temperature
        )