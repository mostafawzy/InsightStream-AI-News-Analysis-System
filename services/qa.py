from langchain_groq import ChatGroq
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_community.vectorstores import FAISS

def answer_question(question, embeddings, index_path):
    vectorstore = FAISS.load_local(
        index_path,
        embeddings,
        allow_dangerous_deserialization=True
    )

    llm = ChatGroq(
        temperature=0,
        model_name="llama-3.3-70b-versatile"
    )

    chain = RetrievalQAWithSourcesChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever()
    )

    return chain.invoke({"question": question})
