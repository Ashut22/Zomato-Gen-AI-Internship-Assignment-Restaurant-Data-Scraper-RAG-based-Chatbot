import gradio as gr
from chatbot import load_vector_store, setup_llm, create_retrieval_chain

# Load the components
vector_store = load_vector_store()
llm = setup_llm()
chain = create_retrieval_chain(vector_store, llm)

# Define the chatbot response function
def chatbot_response(message, history):
    response = chain({"question": message})["answer"]
    return response

# Create ChatInterface
iface = gr.ChatInterface(
    fn=chatbot_response,
    title="Restaurant Chatbot",
    description="Ask questions about restaurants, such as 'Which restaurant has the best vegetarian options?' or 'Does ABC restaurant have gluten-free appetizers?'"
)

# Launch the app
iface.launch()