這裡紀錄一些如何建構&使用 AI model 的過程 ，供自己參考，including  environment constructing , necessary system config (linux/windows/WSL/conda...)  & python coding ...and so on 
### **- 就是 AI model to service How To -**

(由於硬體環境限制 (a crappy old pc with i5-7500 CPU/16.0 GB DRAM/Nvidia GeForce GTX 1060 6GB)，在此當模型較大&所需的 VRAM 較高時，在此常選擇在windows 環境下 進入 conda 去建構，一方面用conda切割個專案的獨立立執行空間，一方面充分利用 windows系統對於 Nvidia GPU獨有的 shared memory 環境，可以使用系統DRAM充當VRAM，當跑模型的時候，如果用到shared memory 會變慢，但不至於 crash，以便能夠測試 & 部署 & 開發 AI application . **在此模式下須注意: 雖然是建構在conda，但外層的OS還是 windows，有些模型內的python code 只對linux版本，沒有對windows OS 做處理，這裡要特別注意，有時候需要debug&fix，尤其是在python內 執行一些 command line 動作 ，常常只有 linux的命令，並未有偵測OS做分別處理，這時候就會跳 error **)

## Autogen + litellm +ollama
環境 : windows10 + conda 

1. create a folder for this project
`$mkdir autogen_litellm`
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
6. 






