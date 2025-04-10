import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List, Dict

class VectorStorage:
    """智能向量数据库抽象层"""
    def __init__(self, model_name='paraphrase-mpnet-base-v2'):
        self.encoder = SentenceTransformer(model_name)
        self.index = faiss.IndexFlatL2(768)  # 根据嵌入维度调整
        self.metadata_store = {}
        
    def add_documents(self, documents: List[Dict]):
        """文档向量化存储"""
        texts = [doc["content"] for doc in documents]
        embeddings = self.encoder.encode(texts, normalize_embeddings=True)
        
        # 构建索引
        self.index.add(np.array(embeddings).astype('float32'))
        
        # 存储元数据
        for idx, doc in enumerate(documents):
            self.metadata_store[idx] = {
                "content": doc["content"],
                "source": doc.get("source", "unknown")
            }

    def semantic_search(self, query: str, threshold=0.85) -> List[Dict]:
        """基于语义相似度的缓存查询"""
        query_embedding = self.encoder.encode([query], normalize_embeddings=True)
        distances, indices = self.index.search(query_embedding.astype('float32'), 1)
        
        if distances[0][0] < (1 - threshold):
            matched = self.metadata_store[indices[0][0]]
            return matched
        return None