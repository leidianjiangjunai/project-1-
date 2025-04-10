from sentence_transformers import SentenceTransformer
import faiss

class SemanticCache:
    def __init__(self):
        self.encoder = SentenceTransformer('paraphrase-mpnet-base-v2')
        self.index = faiss.IndexFlatL2(768)
        self.cache = {}
        
    def query_cache(self, query: str, threshold=0.9):
        """基于语义相似度的缓存查询[[96]][[98]][[101]]"""
        vector = self.encoder.encode([query])[0]
        distances, indices = self.index.search(vector.reshape(1,-1), 1)
        
        if distances[0][0] < (1 - threshold):
            matched = self.cache[indices[0][0]]
            return matched["response"]
        return None