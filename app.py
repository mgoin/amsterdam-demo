import gradio as gr
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load the data (please update the path to where you have saved the data)
with open('amsterdam_data.txt', 'r', encoding='utf-8') as file:
    amsterdam_data = file.read()

# Break the data into paragraphs
paragraphs = amsterdam_data.split('\n')
paragraphs = [para for para in paragraphs if len(para) > 50]  # Filtering out very short paragraphs

# Convert the paragraphs into a vector space using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(paragraphs)

# Function to find the most relevant paragraph to a given question
def find_relevant_paragraph(question):
    query_vector = vectorizer.transform([question])
    cosine_matrix = cosine_similarity(query_vector, X)
    best_match = np.argmax(cosine_matrix)
    return paragraphs[best_match]

# Function to be used with Gradio
def amsterdam_facts(question):
    answer = find_relevant_paragraph(question)
    return answer

# Create a Gradio interface
iface = gr.Interface(
    fn=amsterdam_facts, 
    inputs="text", 
    outputs="text",
    examples=[
        ["What is the population of Amsterdam?"],
        ["Can you tell me about the history of Amsterdam?"],
        ["What are the famous landmarks in Amsterdam?"],
        ["Can you tell me about the economy of Amsterdam?"]
    ]
)

# Launch the Gradio interface
iface.launch()

