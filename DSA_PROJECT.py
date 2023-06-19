import heapq

class TrieNode:
    def init(self):
        self.children = {}
        self.document_ids = []

class HybridDataStructure:
    def init(self):
        self.root = TrieNode()
        self.documents = {}

    def insert_document(self, document_id, keywords):
        # Insert keywords into Trie
        for keyword in keywords:
            self._insert_keyword(keyword, document_id)

    def _insert_keyword(self, keyword, document_id):
        node = self.root
        for char in keyword:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.document_ids.append(document_id)

    def add_document(self, document_id, document_text):
        self.documents[document_id] = document_text
        keywords = document_text.lower().split()  # Split text into keywords
        self.insert_document(document_id, keywords)

    def search_documents(self, query):
        relevant_documents = self._retrieve_documents(query)
        ranked_documents = self._rank_documents(relevant_documents)
        return self._get_top_documents(ranked_documents)

    def _retrieve_documents(self, query):
        node = self.root
        for char in query:
            if char not in node.children:
                return []  # No matching documents
            node = node.children[char]
        return node.document_ids

    def _rank_documents(self, documents):
        ranked_documents = []
        for document_id in documents:
            relevance_score = self._calculate_relevance_score(document_id)
            ranked_documents.append((relevance_score, document_id))
        return ranked_documents

    def _calculate_relevance_score(self, document_id):
        # Calculate relevance score based on specific criteria
        # Example: Count keyword occurrences in the document
        relevance_score = 0
        # ... calculation logic ...
        return relevance_score

    def _get_top_documents(self, ranked_documents):
        top_documents = []
        seen_documents = set()  # Keep track of seen documents
        for ranked_document in ranked_documents:
            document_id = ranked_document[1]
            if document_id not in seen_documents:
                heapq.heappush(top_documents, ranked_document)
                seen_documents.add(document_id)

        return [document[1] for document in heapq.nlargest(len(top_documents), top_documents)]
        

def get_input_documents():
    documents = {}
    num_documents = int(input("Enter the number of documents: "))
    for i in range(num_documents):
        document_id = i + 1
        document_text = input(f"Enter the text for Document {document_id}: ")
        documents[document_id] = document_text
    return documents


# Create search engine instance
search_engine = HybridDataStructure()

# Get input documents
input_documents = get_input_documents()

# Build search engine index
for document_id, document_text in input_documents.items():
    search_engine.add_document(document_id, document_text)

# Menu-based loop
while True:
    print("\nMenu:")
    print("1. Search")
    print("2. Add Document")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        # Perform search
        search_query = input("Enter the search query: ")
        search_results = search_engine.search_documents(search_query)

        # Display search results
        if len(search_results) > 0:
            print("Search Results:")
            for document_id in search_results:
                print(f"Document ID: {document_id}\n{search_engine.documents[document_id]}\n")
        else:
            print("No matching documents found.")
            
    elif choice == "2":
        # Add document
        document_id = len(search_engine.documents) + 1
        document_text = input("Enter the text for the document: ")
        search_engine.add_document(document_id, document_text)
        print(f"Document {document_id} added successfully.")
    elif choice == "3":
        # Exit the program
        break
    else:
        print("Invalid choice. Please try again.")

print("Exiting the program.")