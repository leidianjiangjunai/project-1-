# 1. 创建config/validations.py
from pydantic import BaseModel, validator

class FinancialQuerySchema(BaseModel):
    symbol: str
    year: int

    @validator('symbol')
    def validate_symbol(cls, v):
        if len(v) not in (3,4) or not v.isalpha():
            raise ValueError("股票代码格式错误")
        return v.upper()

    @validator('year')
    def validate_year(cls, v):
        if not 2010 <= v <= 2025:  # 修复年份上限
            raise ValueError("年份超出有效范围")
        return v

    