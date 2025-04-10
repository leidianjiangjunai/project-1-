class ValidationAgent:
    def validate_financial_query(self, symbol: str, year: int):
        """多级金融数据校验"""
        # 宏观校验[[37]]
        if year < 2010 or year > 2025:
            raise ValueError("无效的年份范围")
        
        # 中观校验[[41]]
        if symbol not in VALID_SYMBOLS:
            raise ValueError("无效的股票代码")
        
        # 微观校验[[44]]
        if not FinancialData.exists(symbol, year):
            raise ValueError("数据记录不存在")