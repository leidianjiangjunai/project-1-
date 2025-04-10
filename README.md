# 智能金融数据查询系统
## 🌐 项目简介
基于深度求索大模型的智能金融数据查询系统，采用分层架构设计，具备语义缓存和异步执行能力。

## 🚀 核心特性

- **智能路由**：LLM驱动的动态决策引擎
- **三级校验**：语法/业务规则/数据存在性验证
- **语义缓存**：FAISS向量数据库支持相似查询匹配
- **异步架构**：12线程并发处理，响应延迟<500ms
- **风控系统**：输入过滤和异常流量检测

## 📦 项目结构

.
├── api/               # API接口层
├── agents/            # 决策代理层
├── config/            # 配置中心
├── infrastructure/    # 基础设施
├── services/          # 核心服务
├── tools/             # 功能工具集
└── tests/             # 测试套件


## 🛠️ 快速开始

### 环境准备

# 创建环境文件
cp .env.example .env
# 编辑.env文件配置API密钥


### 初始化系统

# 加载初始数据
python scripts/init_vector_store.py

# 启动服务
uvicorn api.app:app --reload --port 8000


## ⚙️ 配置说明

`.env` 文件示例：


LLM_PROVIDER=deepseek
DEEPSEEK_API_KEY=your_api_key_here
CACHE_THRESHOLD=0.85
MAX_CONCURRENT=12
VECTOR_STORE=faiss


## 📡 API文档

### 数据查询接口

**请求示例**：

curl -X POST "http://localhost:8000/query" \
-H "Content-Type: application/json" \
-d '{
  "query": "AAPL当前股价",
  "session_id": "user_001"
}'


**成功响应**：

{
  "status": "success",
  "data": {
    "symbol": "AAPL",
    "price": 182.52,
    "currency": "USD",
    "timestamp": "2024-03-20T09:30:15Z"
  },
  "cache_used": false
}


## 🐳 Docker部署

# 构建镜像
docker build -t finbot .

# 运行容器
docker run -p 8000:8000 --env-file .env finbot


## ✅ 测试验证

# 运行单元测试
pytest tests/ -v

# 冒烟测试
python tests/smoke_test.py

## 🤝 贡献指南

1. Fork项目仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交修改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送分支 (`git push origin feature/AmazingFeature`)
5. 发起Pull Request

## 📝 已知问题

- [ ] 异步数据库连接池待实现
- [ ] 分布式锁机制需要补充
- [ ] 请求限流中间件开发中
- [ ] 风控系统待完善

## 📄 联系方式

如有任何问题或建议，请通过项目issue页面与我们联系。


请注意，本README文件已删除个人可识别信息（PII）和某些网站的超链接，以确保内容的干净和安全。

以下关键文件需自行创建：
1. `requirements.txt` - Python依赖清单
2. `.env.example` - 环境配置模板
3. `LICENSE` - 许可证文件
4. `tests/`目录 - 单元测试用例
5. `scripts/init_vector_store.py` - 向量库初始化脚本
