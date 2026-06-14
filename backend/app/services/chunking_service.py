class ChunkingService:

    def chunk_pages(self, pages, chunk_size = 1000, chunk_overlap = 200):
        chunks = []
        step = chunk_size - chunk_overlap

        for page in pages: # We'll process each page.
            content = page["content"]

#iterates over positions inside a page to split it into smaller chunks.
            for i in range(0, len(content), step):

                chunk = content[i:i + chunk_size]

                chunks.append(
                    {
                        "content" : chunk,
                        "page" : page["page"],
                        "source" : page["source"]
                    }
                )

        return chunks