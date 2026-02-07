from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful Customer Support agent"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

chat_history = []

with open("chat_history.txt") as f:
    for line in f:
        role, content = line.strip().split("|", 1)

        if role == "human":
            chat_history.append(HumanMessage(content=content))
        elif role == "ai":
            chat_history.append(AIMessage(content=content))

print(chat_history)

prompt = chat_template.invoke({
    "chat_history": chat_history,
    "query": "Where is my refund?"
})

print(prompt)
