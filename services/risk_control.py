from typing import Dict, Any
from pydantic import ValidationError
from config.validations import FinancialQuerySchema  # 确保校验模型存在

class RiskControl:
    def validate_input(self, data: Dict[str, Any]) -> bool:
        """三级输入验证流程"""
        try:
            # 第一阶段：结构校验
            validated = FinancialQuerySchema(**data)
            
            # 第二阶段：业务规则校验
            if not self._validate_year_range(validated.year):
                raise ValueError("无效年份范围")
                
            # 第三阶段：存在性校验
            if not self._check_symbol_exists(validated.symbol):
                raise ValueError("证券代码不存在")
                
            return True
            
        except ValidationError as e:
            self._log_validation_error(e)
            return False
        except ValueError as e:
            self._log_business_error(e)
            return False

    def _validate_year_range(self, year: int) -> bool:
        """年份有效性验证"""
        return 2010 <= year <= 2025

    def _check_symbol_exists(self, symbol: str) -> bool:
        """证券代码存在性验证"""
        valid_symbols = ["AAPL", "GOOG", "MSFT"]  # 应该从配置或数据库获取
        return symbol.upper() in valid_symbols

    def _log_validation_error(self, error: ValidationError):
        """结构化日志记录"""
        error_details = {
            "type": "validation_error",
            "errors": error.errors()
        }
        # 实际项目中应该使用logging模块
        print(f"Validation Failed: {error_details}")

    def _log_business_error(self, error: ValueError):
        """业务错误日志"""
        print(f"Business Rule Violation: {str(error)}")