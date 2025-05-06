紀錄一些如何建構&使用 AI model 的過程 ，供自己參考，including  environment constructing , necessary system config (linux/windows/WSL/conda...)  & python coding ...and so on

vtuber  [open LLM VTuber]([ai-how-to/Open_LLM_Vtuber at main · jj449/ai-how-to](https://github.com/jj449/ai-how-to/tree/main/Open_LLM_Vtuber)https://https://github.com/jj449/ai-how-to/tree/main/Open%20LLM%20Vtube)

[fine-tuning with CoLab]([ai-how-to/fine_tuning_colab_hagging_facce at main · jj449/ai-how-to](https://github.com/jj449/ai-how-to/tree/main/fine_tuning_colab_hagging_facce))

[文生影片 WAN2.1]([ai-how-to/WAN2.1 at main · jj449/ai-how-to](https://github.com/jj449/ai-how-to/tree/main/WAN2.1))

[prompt engineering 以 文字生圖 Flux1.0為例](https://[ai-how-to/prompt_engineering_以flux為例 at main · jj449/ai-how-to](https://github.com/jj449/ai-how-to/tree/main/prompt_engineering_%E4%BB%A5flux%E7%82%BA%E4%BE%8B))

[multi-agents with GraphRag]([ai-how-to/multi_agents_with_RAG at main · jj449/ai-how-to](https://github.com/jj449/ai-how-to/tree/main/multi_agents_with_RAG))

**很多使用者是在windows環境下，用conda 環境跑， 在此模式下須注意: 雖然是建構在conda，但外層的OS還是 windows，有些模型內的python code 只對linux版本，沒有對windows OS 做處理，這裡指的主要是在python內執行 命令列 部分，例如拷貝檔案等動作，常只有 linux的命令，並未有偵測OS做分別處理，這時候就會跳 error 需要debug&fix **)
