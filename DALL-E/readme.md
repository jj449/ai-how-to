AI 模型部署、使用，已經做了很多了，大部分大同小異，就是建構 pytohn環境 、CUDA、等等。這裡用 DALL-E文生圖，是因為很多時候 要做視頻的，需要一張圖，所以先弄個 DALL-E來用，主要是因為它 硬體需求小。

為了之後使用方便， 把 DALL-E 做成 docker image 。

1. clone git : `$git clone https://github.com/borisdayma/dalle-mini.git`
   它的 Dockerfile 放在 Docker/ 目錄下
2. `$cd dalle-mini/docker`
3. 依據 Docekr/readme.md 的說明
4. build : `$docker build . -t dalle-mini:latest` 這裡有點久，因為要去拉很多東西。

   ![](assets/20250427_164538_image.png)
5. run 這個 docker :
   docker run --rm --name dallemini -it -p 8888:8888  --gpus all  -v "${PWD}":/workspace dalle-mini:latest

   如果是在 windows 下， 改成 :
   docker run --rm --name dallemini -it -p 8888:8888 --gpus all -v "d:\gg:/workspace" dalle-mini:latest

   用 d:\gg 指定worspace對應到 windows的實體目錄

   成功跑起來的話，會看到

   ![](assets/20250427_165217_image.png)

   而且已經進入 container裡面的 workspace 目錄了。
6. 把 jupyter notebook 跑起來
   `$jupyter notebook --ip 0.0.0.0 --no-browser --allow-root`
   成功的話，會看到下圖

   ![](assets/20250427_171409_image.png)
   這個網址就是 inference 的入口了， 瀏覽器打開即可。
7. double click .ipynb   notebook檔

   ![](assets/20250427_172551_image.png)

   進去就像 CoLab 一樣 ，就一步一步執行下去

   ![](assets/20250427_172927_image.png)
   到每一個 cell 去，然後給他按 執行 ，就會跑了

   ![](assets/20250427_173136_image.png)
   到第4步的時候，需要 wandb.ai 的 API key
8. 然後到 prompt 那哩，輸入你的 提示詞， 然後往下執行，就會生出 圖片了。
9. GG了， out of memory....

   ![](assets/20250430_102625_image.png)

   看來玩這個還要多備點銀彈才行....
10. 把 n_predictions = 2 降低一些看看
    prompts = [
    "A beautiful oriental girl talking on her cell phone, close-up of her face showing her big, bright eyess"
    ]
