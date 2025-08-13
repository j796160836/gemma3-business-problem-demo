import easyocr
import json
import ollama

def parse_text_with_ollama(full_text: str, model: str="gemma3:4b", host: str='http://localhost:11434'):
    prompt = f"""
你是一位專業的台灣政府公文辨識助手。
    幫我從以下的文字中，嚴格按照以下要求，抽取出指定的四個欄位資訊，並以一個 JSON 物件格式回傳。

    1. 發文字號 (JSON key: "doc_number")
    2. 發文日期 (JSON key: "date")
    3. 發文機關 在標題 XXX 函 (JSON key: "sender")
    4. 受文者 (JSON key: "receiver")
    5. 主旨 (JSON key: "title")

    如果某個欄位在圖片中找不到，請將其值設為 "N/A"。
    你的回覆**只能**包含一個沒有任何額外說明的 JSON 物件。

    輸入的文字：
    ```
    {full_text}
    ```
    """

    try:
        client = ollama.Client(host=host)
        response = client.chat(
                model=model,
                messages=[
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ],
                # 設定 format 為 'json' 可讓模型更傾向於輸出 JSON 格式
                format='json'
        )
        # 4. 解析回傳的 JSON 結果
        response_content = response['message']['content']
        # 嘗試直接解析 JSON
        try:
            return json.loads(response_content)
        except json.JSONDecodeError:
            # 如果模型回傳的不是標準 JSON（例如包含了前後的 ```json ... ```），則嘗試從中提取
            print("模型回傳的不是標準 JSON，嘗試提取...")
            json_match = response_content[response_content.find('{'):response_content.rfind('}')+1]
            if json_match:
                return json.loads(json_match)
            else:
                print("錯誤：無法從模型的回應中解析出 JSON。")
                print("模型原始回應：", response_content)
                return None

    except Exception as e:
        print(f"與 Ollama 互動時發生錯誤：{e}")
        return None


# --- 主程式執行 ---
if __name__ == "__main__":
    sample_pic = 'demo-pic/roc-mol.jpg'
    host = 'http://localhost:11434'  # Ollama 伺服器的地址
    model = 'gemma3:4b'  # 使用 Ollama 的 Gemma 3 模型
    # model = 'gemma3:27b'  # 使用 Ollama 的 Gemma 3 模型
    # model = 'gemma3n:e4b'  # 使用 Ollama 的 Gemma 3n 模型
    # model = 'gpt-oss:20b'  # 使用 Ollama 的 GPT-OSS 20B 模型
    # model = 'deepseek-r1:1.5b'  # 使用 Ollama 的 Deepseek 模型
    # model = 'deepseek-r1:7b'  # 使用 Ollama 的 Deepseek 模型

    reader = easyocr.Reader(['ch_tra', 'en'])  # ch_tra: 繁體中文

    results = reader.readtext(sample_pic, detail=0, paragraph=True)
    full_text = "\n".join(results)

    print("\n--- 從圖片中識別的文字 ---\n")
    print(full_text)
    print("\n--- 使用 Ollama 模型解析文字 ---\n")
    fields = parse_text_with_ollama(full_text, model=model, host=host)
    print(json.dumps(fields, ensure_ascii=False, indent=2))
