import sys
from scripts.search_rhino_docs import search

if __name__ == "__main__":
    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else ""
    print(search(query))
