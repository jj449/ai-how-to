check basic  for ollama & litellm basic.

prepare embedding model ， ex:nomic-embed-text
`$ollama pull nomic-embed-text`

check if model exist

`$ollama list`

embedding model don't need to run , just acceaa via api，

Ex: curl http://localhost:11434/api/embeddings -d '{"model": "nomic-embed-text:latest","prompt": "Llamas are members of the camelid family"}'

(curl in windows terminal not working, use git bash instead)

![](https://github.com/jj449/ai-how-to/tree/main/multi_agents_with_RAG/assets/2024-12-14-14-57-53.png)


use conda env 'autogen_litellm' previously established .

`$conda activate autogen_litellm `

install GraphRAG

`$pip install graphrag`

create a folder forrag indexer

`**mkdir** -p ./ragdir/input`

input 就是要放資料的地方 。

`graphrag init --root  ./rag_graph`

rag indexer 會將 rag_graph`inpu folder 裡的東西 進行 初始化 .並產生 .env、settings.yaml檔案。

![](../assets/2024-12-07-14-21-43.png)

設定檔 setting.yaml

執行 indexing

`graphrag index --root rag_graph`

### trouble shooting

garphrag index  error while    create_base_entity_graph AttributeError: 'list' object has no attribute 'on_error'
![](../assets/2024-12-08-10-03-08.png)
