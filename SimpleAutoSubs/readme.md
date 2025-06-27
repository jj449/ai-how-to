### SimpleAutoSubs Flask API 服務建置與成功測試總結 (基於 `cu12.x` CUDA 版本)

原 :  [https://github.com/SeidSmatti/SimpleAutoSubs](https://https://github.com/SeidSmatti/SimpleAutoSubs)

### 原始說明 cu11.7 => 實際使用 cu12.x 編譯才會成功，執行才不會 error。

這個總結涵蓋了從環境準備、程式碼修正到最終成功運行 Flask API 並透過 cURL 請求處理影片的全過程，並將其中 CUDA 相關的部分指向 `cu12.x` 版本。

---

#### 1. 專案目標

目標是建立一個基於 Flask 的 RESTful API 服務，該服務能夠接收影片 URL，利用 `SimpleAutoSubs` 核心模組（預期會使用 GPU 加速，支援 CUDA 12.x）進行語音轉文字和字幕嵌入，最終返回帶有字幕的影片下載連結。

---

#### 2. 環境準備與依賴安裝

* **Python 虛擬環境** ：
  * 使用 `conda` 或 `venv` 創建並啟用虛擬環境，例如 `simpleautosubs_env`。
  * **重要** ：所有後續的 Python 套件安裝都在此虛擬環境中進行，確保專案依賴的隔離性。
* **CUDA Toolkit (cu12.x)** ：
  * 確保系統已安裝 **CUDA Toolkit 12.x 版本** 。這是為了讓 `SimpleAutoSubs` 及其底層的深度學習框架（如 PyTorch 或 TensorFlow）能夠利用 GPU 進行加速。
  * 通常需要從 NVIDIA 官網下載並安裝對應的 CUDA Toolkit 版本。
* **PyTorch/TensorFlow (支援 cu12.x)** ：
  * 根據 `SimpleAutoSubs` 內部使用的深度學習框架，安裝對應的 **支援 CUDA 12.x 的 PyTorch 或 TensorFlow 版本** 。例如，對於 PyTorch，可能需要執行類似 `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121`（具體指令依 PyTorch 官方文檔為準）。
* **核心 Python 套件安裝** ：
  * 在已啟用的虛擬環境中，安裝 Flask 及其他必要的套件：
    **Bash**

    ```
    pip install Flask requests uuid
    ```
  * 確保 `SimpleAutoSubs` 核心模組（如 `transcriber`, `embedder`）所需的所有依賴也已滿足。

---

#### 3. `app.py` 核心 API 服務程式碼修正

原始 `app.py` 程式碼存在多處 Python 語法錯誤，經過以下修正：

* **語法修正** ：
  * 所有缺少冒號 `:` 的語句（如 `def function():`, `try:`, `except Exception as e:`, `if condition:`, `for item in list:`, `with open(...):`, `if __name__ == '__main__':` 等）均已補上。
  * 所有字串（包括日誌訊息、f-string 中的文字、JSON 鍵值等）都用單引號 `'` 或雙引號 `"` 正確包裹。
  * f-string 中嵌入變數時，確保使用大括號 `{}` 包裹變數名。
  * Windows 路徑如 `D:\SimpleAutoSubs` 修正為 `D:\\SimpleAutoSubs` 或使用原始字串 `r'D:\SimpleAutoSubs'`。
* **核心模組導入路徑** ：
  * 確保 `sys.path.append('D:\\SimpleAutoSubs')` 正確指向 `SimpleAutoSubs` 專案的根目錄，以便成功導入 `transcriber` 和 `embedder` 模組。
* **`BASE_SERVER_URL` 配置** ：
  * `BASE_SERVER_URL = "http://127.0.0.1:5009"`：此變數用於構建返回給客戶端的輸出影片 URL。
* **Flask 應用運行埠號** ：
  * **關鍵修正** ：在 `if __name__ == '__main__':` 區塊中，將 `app.run` 的 `port` 參數設置為 `5009`，與 `BASE_SERVER_URL` 中的埠號保持一致：
    **Python**

    ```
    app.run(host='0.0.0.0', port=5009, debug=True)
    ```
  * `0.0.0.0` 允許 Flask 應用在所有可用的網絡接口上監聽請求。
* **錯誤處理與日誌** ：
  * 增加了 `try...except` 塊來處理模組導入失敗、下載影片失敗、影片處理錯誤等情況，並通過 `logging` 模組輸出詳細的日誌訊息。
  * JSON 響應中包含 `error_code` 和 `error_msg`，提供更清晰的錯誤提示。
* **靜態文件服務** ：
  * `@app.route('/out_video/<path:filename>')`：設置了路由來服務 `out_video` 目錄下的處理後影片，使其可通過 URL 訪問。

---

#### 4. Flask API 啟動

在虛擬環境啟動的命令提示字元中，執行 `app.py`：

**Bash**

```
(simpleautosubs_env) D:\SimpleAutoSubs>python app.py
```

成功啟動後，控制台應顯示類似以下訊息，確認服務運行在指定埠號：

```
 * Running on http://127.0.0.1:5009/ (Press CTRL+C to quit)
 * Running on http://192.168.1.xxx:5009
```

---

#### 5. 使用 cURL 進行 API 測試

在服務成功運行後，使用 `cURL` 工具發送 POST 請求到 API 端點。

* **cURL 命令範例** ：
  **Bash**

  ```
  curl -X POST \
    -H "Content-Type: application/json" \
    -d '{
      "video_url": "https://aix.soshow.app/thrump2.mp4",
      "model_size": "base",
      "use_gpu": true,
      "include_timecodes": true,
      "language": "zh"
    }' \
    http://127.0.0.1:5009/process_video
  ```
* **請求參數說明** ：

  * `video_url`: 待處理影片的 URL。
  * `model_size`: Whisper 模型大小（例如 `base`, `medium`, `large-v3` 等）。
  * `use_gpu`: 是否啟用 GPU 加速（需配合 CUDA 12.x 環境）。
  * `include_timecodes`: 字幕是否包含時間碼。
  * `language`: 語音語言，`autodetect` 或指定語言代碼（如 `zh`, `en`）。
* **成功響應** ：
  成功執行 cURL 命令後，收到類似以下 JSON 響應：
  **JSON**

  ```
  {
    "error_code": 0,
    "error_msg": "",
    "out_url": "http://127.0.0.1:5009/out_video/1b0362df-6fcb-4a9f-85b3-f0d3208ada65.mp4"
  }
  ```
  這表示影片處理成功，並返回了帶有字幕的影片的下載 URL。
