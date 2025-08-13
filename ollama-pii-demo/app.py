import logging
import ollama

def anonymize_text(text_to_anonymize: str, model: str='gemma3:4b', host: str='http://localhost:11434') -> str:
    """
    使用 Ollama 上的 Gemma 模型對文字進行個資隱碼。

    Args:
        text_to_anonymize (str): 包含個資的原始文字。
        model (str): 使用的模型名稱，預設值為 'gemma3:4b'。
        host (str): Ollama 伺服器的主機地址，預設值為 'http://localhost:11434'。

    Returns:
        str: 經過隱碼處理後的文字。
    """

    # 定義提示詞 (Prompt)
    prompt_template = f"""
    作為一個個資隱碼處理器，請你仔細閱讀以下文字，並將其中所有的個人資訊（包含姓名、電話號碼、電子郵件、身分證字號、地址）進行遮蔽。

    請根據以下規則進行替換：
    - 姓名替換為 [姓名]
    - 電話號碼替換為 [電話]
    - 電子郵件替換為 [電子郵件]
    - 地址替換為 [地址]
    - 身分證字號替換為 [身分證字號]

    以下是需要處理的文字：
    {text_to_anonymize}
    """

    # 使用 ollama.chat 方法與模型互動
    try:
        client = ollama.Client(host=host)
    
        response = client.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt_template}]
        )
        # 返回模型的回應內容
        return response['message']['content']
    except Exception as e:
        print(f"與 Ollama 伺服器溝通時發生錯誤: {e}")
        logging.exception("")
        return "隱碼失敗，請檢查 Ollama 服務是否正在運行。"

# --- 主程式執行 ---
if __name__ == "__main__":
    host = "http://localhost:11434"
    model = "gemma3:4b"
    # model = "gemma3n:e4b"
    # model = "qwen2.5vl:7b"
    # model = 'deepseek-r1:1.5b'  # 使用 Ollama 的 Deepseek 模型
    # model = 'deepseek-r1:7b'  # 使用 Ollama 的 Deepseek 模型

    # 測試範例
    sample_text = "您好，我的名字是王小明，電話是0912345678。我的信箱是wang.xiaoming@example.com，住址是台北市信義區忠孝東路一段1號，身分證字號是A123456789。"

    anonymized_result = anonymize_text(sample_text, model=model, host=host)

    print("--- 原始文字 ---")
    print(sample_text)
    print("\n--- 隱碼後文字 ---")
    print(anonymized_result)