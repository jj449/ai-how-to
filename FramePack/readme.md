由圖片生成影片。

[github在這裡](https://[GitHub - lllyasviel/FramePack: Lets make video diffusion practical!](https://github.com/lllyasviel/FramePack))

主要特性是從輸入的照片，預測照片中人物的下一個動作，然後一個一個下去產生影片。Packing Input Frame Context in Next-Frame Prediction Models for Video Generation.

這個github也做的很方便，甚至有 one click 包，直接就能用。

整包下載回來後，記得執行 updat.bat 。

然後執行 run.bat 就行了，

![](assets/20250501_125948_image.png)

在本機 7860 port 產生了 inference ，瀏覽器前往

![](assets/20250501_130057_image.png)

先用 chatGpt產生一張照片，

![](assets/20250501_130615_image.png)

是不是很厲害?

聽說 Gemini (Google AI Studio) 現在做圖片的功能，好像比 chatGPT還厲害了，有空可去試試看。

然後把照片傳到 FramePack 去，

在 terminal 的 FramePack inference 那裡，可以看見完整的運作過程


![](assets/20250501_132230_image.png)

前端可看到經過 text encoding . vae encoding ....

又GG了.... out of memory

![](assets/20250501_132306_image.png)
