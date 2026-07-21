import os
import json
import gspread
from datetime import datetime

# 1. โหลดข้อมูลหุ่นยนต์จาก Secret
service_account_info = json.loads(os.environ['GOOGLE_SERVICE_ACCOUNT_JSON'])
gc = gspread.service_account_from_dict(service_account_info)

# 2. เปิด Google Sheet (เอา ID จาก URL ของ Sheet มาใส่)
# ตัวอย่าง ID: 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms
SHEET_ID = '1aDOsLgbJ3MpNYtHgufCNDWSICiSSrYCBSaEtgOtMxhw' 
sh = gc.open_by_key(SHEET_ID)
worksheet = sh.sheet1

# 3. เพิ่มข้อมูลลง Sheet
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
row = [now, "เอสเพรสโซ่", 2, 50, 100]
worksheet.append_row(row)

print("✅ บันทึกข้อมูลลง Sheet สำเร็จ:", row)