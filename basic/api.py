from flask import Flask, request, render_template, jsonify
from autogen import ConversableAgent, UserProxyAgent
import os
from keyboard import press
import litellm
# set env variables
os.environ["OPENAI_API_KEY"] = "NotRequired"

app = Flask(__name__)


# Set your LiteLLM proxy URL and API key
os.environ["LITELLM_API_BASE"] = "http://172.26.80.1:4000"
os.environ["LITELLM_API_KEY"] = "NotRequired"

# Define the local LLM configuration
local_llm_config = {
    "config_list": [
        {
            "model": "NotRequired",
            "api_key": "NotRequired",
            "base_url": "http://172.26.80.1:4000",
            "price": [0, 0],
        }
    ],
    "cache_seed": None,
}

# Create the ConversableAgent and UserProxyAgent
assistant = ConversableAgent("agent", llm_config=local_llm_config)
user_proxy = UserProxyAgent("user", code_execution_config=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    res = litellm.completion(
            model="ollama/llama2:chat",
            messages=[{ "content": user_message,"role": "user"}],
            max_tokens=10
    )

    # Initiate chat with the assistant
    #res = assistant.initiate_chat(user_proxy, message=user_message)
    #res = assistant.initiate_chat(assistant, message=user_message)
    press('enter')
    print('after chat')
    print( 'res:') 
    print( res) 
    
    print(res.choices[0].message.content)
    print( res.json()) 
    
    return res.json()
    #return jsonify({"response": res})

if __name__ == '__main__':
    #app.run(host='172.26.80.1', port=80)
    app.run(host='0.0.0.0', port=80)
