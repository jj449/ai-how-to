這裡紀錄一些如何建構&使用 AI model 的過程 ，供自己參考，including  environment constructing , necessary system config (linux/windows/WSL/conda...)  & python coding ...and so on 
### **- 就是 AI model to service How To -**

(由於硬體環境限制 (a crappy old pc with i5-7500 CPU/16.0 GB DRAM/Nvidia GeForce GTX 1060 6GB)，在此當模型較大&所需的 VRAM 較高時，在此常選擇在windows 環境下 進入 conda 去建構，一方面用conda切割個專案的獨立立執行空間，一方面充分利用 windows系統對於 Nvidia GPU獨有的 shared memory 環境，可以使用系統DRAM充當VRAM，當跑模型的時候，如果用到shared memory 會變慢，但不至於 crash，以便能夠測試 & 部署 & 開發 AI application . **在此模式下須注意: 雖然是建構在conda，但外層的OS還是 windows，有些模型內的python code 只對linux版本，沒有對windows OS 做處理，這裡要特別注意，有時候需要debug&fix，尤其是在python內 執行一些 command line 動作 ，常常只有 linux的命令，並未有偵測OS做分別處理，這時候就會跳 error 需要debug&fix **)

# Autogen + litellm +ollama
*環境 : windows10 + conda 

1. create a folder for this project
`$mkdir autogen_litellm`
`$mkdir litellm`
2. get into the folder then create a conda env for this :
先確認你需要的 python version (here is 3.11)
`$cd autogen_litellm`
`$conda create -n autogen_litellm python=3.11`
check if conda env created successfully ? 
`$conda env list` 
you should see autogen_litellm listed there .
now you have a pytohn 3.11 env . 
3. activate this conda env and get in 
`$conda activate autogen_litellm`
4. install litellm
`$pip install litellm[proxy]`
check litellm installation : `litellm`
5. install ollama 
先新增 channel 不然找不到 ollama package
`$conda config --add channels conda-forge`
`$conda config --set channel_priority strict`
then install ollam 
`$conda install ollama`
check ollama installation : `$ollama --version`
6. start ollama 
`$ollama serv`
this will make ollama server at default port 11434
check http://localhost:11434/
7. run/pull model from ollama
(in activated conda : autogen_litellm)
`$ollama run llama2:chat `
this will download&run llama2:chat model 
if model download & run succesfully ,you will see 'Send a message' prompt in terminal , then you can chat with model now. 
(ollama from anaconda chanel is too old to run new model , ex: phi3 , try those models later)
8. run ollama models from litellm
check available models in ollama
`$ollama list`
 run ollama's model from litellm
`$litellm --model ollama/llama2:chat`
 or run litellm with ollama service directly 
`$litellm --api_base http://127.0.0.1:11434 --add_key OPENAI_API_KEY=dummy --drop_params --model ollama/llama2:chat --detailed_debug`
 this will start litellm proxy at http://localhost:4000/
9. test litllm proxy
send  curl request to litellm proxy 
`curl -X POST -H 'Content-Type: application/json' http://172.26.80.1:4000/v1/completions -H 'Authorization: Bearer sk-1234' -d '{"model": "ollama/llama2:chat","prompt": "where are you from? ","max_tokens": 50,"temperature": 0.7}'`
you will see response from litellm proxy , ollama service , ollama model .
10. autogen 
install autogen : `$pip install autogen`
write our pyhthon code to play 
```python
from autogen import ConversableAgent, UserProxyAgent

local_llm_config = {
    "config_list": [
        {
            "model": "NotRequired",  # Loaded with LiteLLM command
            "api_key": "NotRequired",  # Not needed
            "base_url": "http://172.26.80.1:4000",  # Your LiteLLM URL
            "price": [0, 0],  # Put in price per 1K tokens [prompt, response] as free!
        }
    ],
    "cache_seed": None,  # Turns off caching, useful for testing different models
}


assistant = ConversableAgent("agent", llm_config=local_llm_config)

user_proxy = UserProxyAgent("user", code_execution_config=False)

res = assistant.initiate_chat(user_proxy, message="How can I help you today?")

print(assistant)
```





####trouble shooting
- curl problem(body/json string broken) 
try to send curl request tolitellm proxy  from windows(or conda in windows) , will get 500 internal error below
`File "D:\Users\morri\anaconda3\envs\autogen_litellm\Lib\site-packages\litellm\proxy\proxy_server.py", line 3538, in completion`
問題出在以下這行程式碼
`data = json.loads(body_str)`
curl 送來的 body 壞掉了。如果我們在此行之前，加上以下程式碼，列印收到的 body  string
` print("body_str" :" + body_str)`
`data = json.loads(body_str)`
會發現 收到的body fromat or json string 有問題。
`body_str :'{model:`
斷掉了，後面沒了，所以程式執行 json.load就出錯。 
**如果從 linux 發送 curl 則無問題, ex : in ubuntu  WSL**


- IP of windows host / WSL / conda












