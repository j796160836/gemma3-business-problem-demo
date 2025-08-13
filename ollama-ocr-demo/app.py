import ollama
import base64
from PIL import Image
import io
import json

def image_to_base64(image_path: str) -> str:
    """
    將圖片轉換為 Base64 字串。
    """
    try:
        with Image.open(image_path) as img:
            buffered = io.BytesIO()
            img.save(buffered, format="JPEG")
            img_byte = buffered.getvalue()
            return base64.b64encode(img_byte).decode('utf-8')
    except FileNotFoundError:
        print(f"錯誤：找不到檔案 '{image_path}'")
        return None
    except Exception as e:
        print(f"處理圖片時發生錯誤：{e}")
        return None
    

def preprocess_image(image_path: str, max_size_kb: int = 500) -> str:
    """
    讀取圖片、轉換為 Base64 字串，並確保檔案大小適中。
    Ollama 對於輸入圖片的 Base64 字串大小有限制，此處進行壓縮處理。
    """
    try:
        with Image.open(image_path) as img:
            # 轉換為 RGB 以處理不同圖片格式
            img = img.convert('RGB')
            
            # 建立一個記憶體中的 BytesIO 物件
            buffered = io.BytesIO()
            img.save(buffered, format="JPEG", quality=85) # 使用 JPEG 格式並調整品質
            
            # 如果檔案過大，則降低品質再次儲存
            while buffered.tell() / 1024 > max_size_kb:
                buffered.seek(0)
                buffered.truncate()
                quality = int(85 * (max_size_kb / (buffered.tell() / 1024))**0.5)
                img.save(buffered, format="JPEG", quality=quality)

            buffered.seek(0)
            img_byte = buffered.getvalue()
            return base64.b64encode(img_byte).decode('utf-8')

    except FileNotFoundError:
        print(f"錯誤：找不到檔案 '{image_path}'")
        return None
    except Exception as e:
        print(f"處理圖片時發生錯誤：{e}")
        return None


def ocr_document_with_llm_model(image_path: str, model: str = "gemma3:4b", host: str = "http://localhost:11434") -> dict:
    """
    使用 Ollama 部署的 LLM 模型進行 OCR 並擷取指定欄位。
    """
    # 1. 圖片前處理並轉換為 Base64
    image_base64 = image_to_base64(image_path)
    if not image_base64:
        return None

    # 2. 設計精確的 Prompt
    # prompt = """
    # #zh_tw 你是一位專業的 OCR 助理，專門辨識繁體中文的政府公文。
    # 請辨識這張圖片中的公文內容，並嚴格按照以下 JSON 格式輸出指定的四個欄位：
    # - 發文字號 (doc_number)
    # - 發文日期 (date)
    # - 發文者 (sender)
    # - 受文者 (receiver)
    # - 主旨 (title)

    # 如果某個欄位在圖片中找不到，請將其值設為 "N/A"。
    # 你的回答**只能**包含 JSON 物件，不要有任何其他說明或文字。
    # """
    prompt = """
    你是一位專業的台灣政府公文辨識助手。
        請辨識這張圖片中的文字，並嚴格按照以下要求，抽取出指定的四個欄位資訊，並以一個 JSON 物件格式回傳。

    1. 發文字號 (JSON key: "doc_number")
    2. 發文日期 (JSON key: "date")
    3. 發文機關 在標題 XXX 函 (JSON key: "sender")
    4. 受文者 (JSON key: "receiver")
    5. 主旨 (JSON key: "title")

    如果某個欄位在圖片中找不到，請將其值設為 "N/A"。
    你的回覆**只能**包含一個沒有任何額外說明的 JSON 物件。
    """
#     prompt = """
# You are a document parsing assistant designed to extract structured data from PDFs for automated uploading and validations.

# Extract the following fields from the document text:

# doc_number: Extract from the '發文字號' field.

# sender: the sender name for issuing.

# receiver: the receiver name for issuing.

# date: Extract from the '發文日期' field, Format as YYYY/MM/DD.

# title: the document title. Extract from the '主旨' field.

# Ensure the output is a valid JSON object with the following structure:
# {
#     "doc_number": "string",
#     "sender": "string",
#     "receiver": "string",
#     "date": "YYYY/MM/DD",
#     "title": "string"
# }

# If any field is not found, set its value to "N/A". Do not include any additional text or explanations in your response.
#     """

    # prompt = """
    # You are a professional OCR assistant specialized in recognizing documents.
    # Please recognize all the text in this image.
    # """

    try:
        # 3. 呼叫 Ollama API
        client = ollama.Client(host=host)

        response = client.chat(
            model=model,
            messages=[
                {
                    'role': 'user',
                    'content': prompt,
                    'images': [image_base64]
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
    # 將 'your_document_image.jpg' 替換為你的公文圖片路徑
    image_file_path = 'demo-pic/roc-mol.jpg'
    host = "http://localhost:11434"  # Ollama 服務的主機地址
    # 使用的模型名稱 
    # model = "qwen2.5vl:7b"
    # model = "qwen2.5vl:3b"
    model = "gemma3:27b"
    # model = "gemma3n:e4b"
    
    # 執行 OCR 辨識
    extracted_data = ocr_document_with_llm_model(image_file_path, model=model, host=host)

    # 輸出結果
    if extracted_data:
        print("辨識成功！")
        print(json.dumps(extracted_data, indent=2, ensure_ascii=False))