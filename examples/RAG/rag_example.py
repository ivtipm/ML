"""
requirements.txt
# langchain==1.1.0
# langchain-core==1.1.0
# langchain-community==0.4.1
# faiss-cpu==1.13.0
# sentence-transformers==5.1.2
# langchain-ollama==1.0.0
# langchain-huggingface==1.1.0
"""

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains import RetrievalQA
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_ollama import ChatOllama
from langchain_classic.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate


# --- 1.
documents = [
    "Retrieval-Augmented Generation (RAG) is a technique that improves LLM responses by injecting relevant external knowledge at query time.",
    "A RAG pipeline typically includes three components: document indexing, retrieval, and a generation model.",
    "Vector databases such as FAISS, Chroma, or Qdrant store text embeddings and enable efficient similarity search.",
    "Sentence embeddings represent text as numerical vectors and allow semantic comparison between documents.",
    "LangChain provides a modular framework for building RAG systems with custom retrievers, prompts, and LLMs."
]
# todo: загрузить реальные документы


# --- 2. Векторизация и индексация данных ---


# Инициализируем модель для создания эмбеддингов
embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Создаем векторную базу данных FAISS прямо из списка документов и эмбеддингов
# FAISS будет использоваться для быстрого поиска наиболее релевантных документов.
vector_store = FAISS.from_texts(documents, embeddings_model)


# Создаем объект "ретривера" (retriever), который умеет искать в этой базе
retriever = vector_store.as_retriever()


# --- 3. Настройка Генеративной Модели (LLM) ---
# ollama должен быть запущен и доступен
llm = ChatOllama(base_url="http://localhost:11434", model="smollm2:135m")



# --- 4. Определение Промпта и Цепочки RAG ---
# --- системный промпт (system message) + шаблон для запроса ---
system_text = (
    "You are an AI assistant that must answer strictly based on the provided context. "
    "If the context does not contain sufficient information, say you don't know. "
    "Keep your responses concise, factual, and helpful."
)

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_text),
    HumanMessagePromptTemplate.from_template(
        "Context:\n{context}\n\n"
        "Question: {question}\n\n"
        "Answer:"
    ),
])

# объект для QA
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",         # поместить в контекст все релевантные документы; см. также map_reduce, refine, map_rerank
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={
        "prompt": prompt,
        "document_variable_name": "context",
    },
)
# --- пример запроса ---
query = "What is the purpose of a RAG system?"
result = qa.invoke({"query": query})

print("Ответ LLM:\n", result["result"])
print("\nИспользованные документы (фрагменты):")
for i, doc in enumerate(result.get("source_documents", []), 1):
    print(f"\n[{i}] {doc.page_content}")