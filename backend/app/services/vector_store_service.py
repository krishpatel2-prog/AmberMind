import chromadb



class VectorStoreService:

    def __init__(self):

        #store everything on disk , not ram
        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )
        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

    def add_chunks(self, chunks, embeddings):

        for index, (chunk,embedding) in enumerate(zip(chunks, embeddings)):
            self.collection.add(
                documents=[
                    chunk["content"]
                ],

                embeddings =[
                  embedding.tolist()
                ],

                metadatas=[
                    {
                        "page": chunk["page"],
                        "source": chunk["source"],
                        "chunk_id": index

                    }
                ],

                ids=[
                    f"{chunk['source']}_{index}"
                ]
            )

    def  retrieve(self,query_embedding, top_k = 5): # top_k = 3:- Give me the top 3 most relevant chunks

        results = self.collection.query(
            query_embeddings = [
                query_embedding.tolist()
            ],
            n_results= top_k
        )
        return results