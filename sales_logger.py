import os
import json
import gspread
import requests
from datetime import datetime

# 1. โหลดข้อมูลหุ่นยนต์จาก Secret
service_account_info = json.loads(os.environ['GOOGLE_SERVICE_ACCOUNT_JSON'])
gc = gspread.service_account_from_dict(service_account_info)

# 2. เปิด Google Sheet (ใส่ ID Sheet ของคุณ)
SHEET_ID = '1aDOsLgbJ3MpNYtHgufCNDWSICiSSrYCBSaEtgOtMxhw' 
sh = gc.open_by_key(SHEET_ID)
worksheet = sh.sheet1

# 3. เพิ่มข้อมูลลง Sheet
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
row = [now, "เอสเพรสโซ่", 2, 50, 100]
worksheet.append_row(row)
print("✅ บันทึกข้อมูลลง Sheet สำเร็จ:", row)

# 4. ส่งข้อความเข้า Telegram
bot_token = os.environ['TELEGRAM_BOT_TOKEN']
chat_id = os.environ['TELEGRAM_CHAT_ID']
message = f"รายงานยอดขายล่าสุด: \nเวลา: {now}\nเมนู: เอสเพรสโซ่\nจำนวน: 2 แก้ว\nยอดรวม: 100 บาท"

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
payload = {"chat_id": chat_id, "text": message}
response = requests.post(url, json=payload)

if response.status_code == 200:
    print("✅ ส่งข้อความเข้า Telegram สำเร็จ")
else:
    print("❌ เกิดข้อผิดพลาดในการส่ง Telegram:", response.text)