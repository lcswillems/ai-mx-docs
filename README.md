# Question-Answer Bot for MultiversX docs

A QA bot for MultiversX docs, made in 50 lines of code, using LangChain, FAISS, SBERT and GPT-3.

> Q: How to create an ESDT token?
>
> A: To create an ESDT token, you need to open the MultiversX web wallet, go to the ISSUE section, click on Tokens, enter the required details, review and sign the transaction, and wait for it to be processed. You can find the token identifier on the Explorer page of the issue transaction or from the Web Wallet. To transfer a token, open the MultiversX web wallet, navigate to the Tokens tab, click on Send for the token you want to transfer, introduce the recipient and the amount you want to send, and press Send.

Test the bot using [the Jupyter Notebook](./notebook.ipynb), or with the scripts 👇

## 1. Installation

(Optional) To not mess up your computer, create a virtual env:

```
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```
python install -r requirements.txt
```

Create an OpenAI API token: [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)

Set `OPENAI_API_KEY` in the `.env` file.

## 2. Creating the index

Next, we need to create the index (takes ~3 mins on my computer):

```
python ingest.py
```

## 3. Asking questions to the bot

Now, we can ask questions to the bot:

```
python query.py
```
