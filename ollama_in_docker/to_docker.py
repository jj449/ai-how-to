from flask import Flask, request, render_template, jsonify
import os
import litellm
import requests
import openai 
# set env variables
os.environ["OPENAI_API_KEY"] = "NotRequired"

app = Flask(__name__)

LITELLM_PROXY_URL = "http://172.26.80.1:4001"; 

client = openai.OpenAI(api_key="anything",base_url=LITELLM_PROXY_URL)

# Set your LiteLLM proxy URL and API key
os.environ["LITELLM_API_BASE"] = "http://127.0.0.1:4001"
os.environ["LITELLM_API_KEY"] = "NotRequired"

# Define the local LLM configuration
local_llm_config = {
    "config_list": [
        {
            "model": "NotRequired",
            "api_key": "NotRequired",
            "base_url": "http://0.0.0.0:4001",
            "price": [0, 0],
        }
    ],
    "cache_seed": None,
}




@app.route('/')
def index():
    return render_template('index_2.html')

@app.route('/chat2', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')

    res = client.chat.completions.create(model="ollama/llama2", messages = [
    {
        "role": "user",
        "content": user_message
    }
])

    #if res.status_code != 200:
    #   return jsonify({'error': 'Failed to get response from litellm proxy'}), 500

    # Initiate chat with the assistant
    #res = assistant.initiate_chat(user_proxy, message=user_message)
    #res = assistant.initiate_chat(assistant, message=user_message)

    print( res) 
    
    print(res.choices[0].message.content)

    return res.json()

if __name__ == '__main__':
    #app.run(host='172.26.80.1', port=80)
    app.run(host='0.0.0.0', port=65401)
