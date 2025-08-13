import ollama

def anonymize_text_with_gemma(text_to_anonymize: str, model: str='gemma3:4b', host: str='http://localhost:11434') -> str:
    """
    使用 Ollama 上的 Gemma 模型對文字進行個資隱碼，並將中間字替換為 'O'。

    Args:
        text_to_anonymize (str): 包含個資的原始文字。
        model (str): 使用的模型名稱，預設值為 'gemma3:4b'。
        host (str): Ollama 伺服器的主機地址，預設值為 'http://localhost:11434'。

    例如：
    王小明 -> 王O明
    0912345678 -> 0OOOOOOO8

    Returns:
        str: 經過隱碼處理後的文字。
    """
    # 定義新的提示詞 (Prompt)，明確指示隱碼規則
    prompt_template = f"""
    作為一個個資隱碼處理器，請你仔細閱讀以下文字，並將其中所有的個人資訊（包含姓名、電話號碼、電子郵件、身分證字號、地址）進行遮蔽。

    請根據以下規則進行替換：
    - 姓名、電話號碼、電子郵件、地址和身分證字號的第一個和最後一個字元保留，中間的所有字元都用 'O' 替代。
    例如：
    王小明 -> 王O明
    0912345678 -> 0OOOOOOO8
    wang.xiaoming@example.com -> wOOOOOOOOOOO@e.com
    台北市信義區忠孝東路一段1號 -> 臺OOOOOOOOOOOOO1號
    A123456789 -> AOOOOOOOO9

    以下是需要處理的文字：
    {text_to_anonymize}
    """
    try:
        response = ollama.chat(
            model='gemma3:4b',  # 指定使用的模型
            messages=[{'role': 'user', 'content': prompt_template}]
        )
        return response['message']['content']
    except Exception as e:
        print(f"與 Ollama 伺服器溝通時發生錯誤: {e}")
        return "隱碼失敗，請檢查 Ollama 服務是否正在運行。"

# --- 主程式執行 ---
if __name__ == "__main__":
    host = "http://localhost:11434"
    model = "gemma3:4b"

    # 測試範例
    sample_text = "您好，我的名字是王小明，電話是0912345678。我的信箱是wang.xiaoming@example.com，住址是台北市信義區忠孝東路一段1號，身分證字號是A123456789。"
    anonymized_result = anonymize_text_with_gemma(sample_text, model=model, host=host)

    print("--- 原始文字 ---")
    print(sample_text)
    print("\n--- 隱碼後文字 (使用 Gemma) ---")
    print(anonymized_result)