import pathlib
import pickle
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

documents = []

splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=2500, chunk_overlap=100)

docs_path = pathlib.Path("./mx-docs/docs/")
file_paths = list(docs_path.glob("**/*.md")) + list(docs_path.glob("**/*.mdx"))

for file_path in file_paths:
  with open(file_path, "r") as f:
    content = f.read()

  relative_path = file_path.relative_to(docs_path).with_suffix("")
  metadata = {"source": f"https://docs.multiversx.com/{relative_path}"}

  for chunk in splitter.split_text(content):
    documents.append(Document(page_content=chunk, metadata=metadata))

index = FAISS.from_documents(documents, HuggingFaceEmbeddings())

with open("index.pickle", "wb") as f:
    pickle.dump(index, f)
