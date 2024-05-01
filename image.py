from openai import OpenAI
import json

# Initialize the API with your API key
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

history = [
    {"role": "system",
     "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
    {"role": "user",
     "content": "Hello, introduce yourself to someone opening this program for the first time. Be concise.return json"},
]
# Generate a completion using the model
completion = client.chat.completions.create(
    model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",  # Replace with your engine
    messages=history,
    stream=True
)

# Convert the completion to a Python dictionary


# Serialize the dictionary into JSON format
# completion_json = json.dumps(completion)

# Print or return the JSON-formatted completion
print(completion)
