import easyocr
import re
import json

reader = easyocr.Reader(['ch_tra', 'en'])  # ch_tra: 繁體中文

results = reader.readtext('demo-pic/roc-mol.jpg', detail=0, paragraph=True)
full_text = "\n".join(results)

# 假設政府公文格式穩定，以下簡單規則提取欄位
def extract_field(pattern, text, greedy=False):
    flags = re.MULTILINE
    match = re.search(pattern, text, flags)
    # if greedy:
    #     match = re.search(pattern, text, flags | re.DOTALL)
    # else:
    #     match = re.search(pattern, text, flags)
    return match.group(1).strip() if match else ""

fields = {
    "doc_number": extract_field(r"發\s*文\s*字\s*號[:：]\s*(.+號)", full_text, greedy=False),
    "date": extract_field(r"發文日期[:：]?\s*!?(\s*中?華?民國?\s*\d+\s*年\s*\d+\s*月+\s*\d+\s*日+)", full_text, greedy=False),
    "sender": extract_field(r"(.+?)\s+函\s+", full_text, greedy=False),
    "receiver": extract_field(r"受\s*文\s*者\s*[:：]\s*([\u4e00-\u9fff\w]+)", full_text, greedy=False),
    "title": extract_field(r"主\s*旨\s*[:：](.+?)\s*(?=說明|$)", full_text, greedy=False)
}

print(full_text)
print("\nExtracted Fields:")
print(json.dumps(fields, ensure_ascii=False, indent=2))
