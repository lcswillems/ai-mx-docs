import os
import pickle
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

chain = load_qa_with_sources_chain(OpenAI(temperature=0, max_tokens=-1))

with open("index.pickle", "rb") as f:
  search_index = pickle.load(f)

def query(question):
  selected_docs = search_index.similarity_search(question, k=1)

  response = chain({
    "input_documents": selected_docs,
    "question": f"{question} — Give as much details as possible."
  }, return_only_outputs=True)["output_text"]

  return response

while True:
    question = input("Q: ")
    response = query(question)
    print(f"A: {response}\n")
