import pytesseract
from PIL import Image
import json
import re

# 設置 Tesseract OCR 的路徑，如果你的安裝路徑不在預設位置，需要自行修改
# 在 Windows 上可能是 r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

def ocr_and_extract(image_path):
    """
    對繁體中文公文圖片進行 OCR 並提取關鍵資訊。
    """
    try:
        # 開啟圖片
        img = Image.open(image_path)

        # 執行 OCR，使用繁體中文語言包 (chi_tra)
        text = pytesseract.image_to_string(img, lang='chi_tra')

        # 顯示 OCR 文本以便除錯
        print("--- OCR 文本 ---")
        print(text)
        print("------------------")

        # 初始化提取的資訊
        data = {
            "date": None,
            "sender": None,
            "receiver": None,
            "title": None
        }

        # 提取日期：尋找 "發文日期" 或類似格式
        date_match = re.search(r'(發文日期|中華民國)\s*(\d{2,3}年\d{1,2}月\d{1,2}日)', text)
        if date_match:
            data["date"] = date_match.group(2).strip()

        # 提取發文機關：通常在文件最上方
        # 這個部分比較難通用，需要依賴特定的格式。這裡簡單地取第一行作為發文機關。
        lines = text.split('\n')
        if len(lines) > 0:
            # 嘗試尋找包含 "函" 或 "令" 的發文機關名稱
            for line in lines:
                if "函" in line or "令" in line or "院" in line or "部" in line:
                    data["sender"] = line.strip().split()[0]
                    break
            # 如果沒有找到，則取第一行
            if not data["sender"]:
                data["sender"] = lines[0].strip()

        # 提取受文者：尋找 "受文者" 關鍵字
        receiver_match = re.search(r'受文者：\s*(.+)', text)
        if receiver_match:
            data["receiver"] = receiver_match.group(1).strip()
        
        # 提取主旨：尋找 "主旨" 關鍵字
        title_match = re.search(r'主旨：\s*(.+)', text)
        if title_match:
            data["title"] = title_match.group(1).strip()

        return data

    except Exception as e:
        print(f"處理過程中發生錯誤: {e}")
        return None

if __name__ == "__main__":
    image_file = './demo-pic/roc-mol.jpg'  # 你的公文圖片檔名
    result_data = ocr_and_extract(image_file)

    if result_data:
        # 將結果轉換為 JSON 格式並印出
        json_output = json.dumps(result_data, ensure_ascii=False, indent=2)
        print("\n--- JSON 輸出 ---")
        print(json_output)
        
        # 也可以將結果儲存到檔案
        with open('output.json', 'w', encoding='utf-8') as f:
            f.write(json_output)
            print("\n結果已儲存到 output.json 檔案。")
    else:
        print("無法從圖片中提取資訊。")