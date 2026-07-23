import logging
import json

# ตั้งค่า Logging
logging.basicConfig(
    filename='agent_trace.log',
    level=logging.INFO,
    format='%(asctime)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_trace(event_type, message):
    logging.info(f"{event_type} | {message}")

def append_sale(item, qty):
    # Guardrail ดัก Error
    if qty <= 0:
        raise ValueError("quantity must be positive")
    return "row appended at A12"

def run_agent(user_message, mock_llm_json):
    log_trace("user_input", user_message)
    log_trace("llm_response", mock_llm_json)
    
    try:
        action = json.loads(mock_llm_json)
        if action["tool"] == "append_sale":
            result = append_sale(action["args"]["item"], action["args"]["qty"])
            log_trace("tool_result", result)
            print("✅ สำเร็จ:", result)
            
    except Exception as e:
        log_trace("tool_error", f"{type(e).__name__} {str(e)}")
        print("❌ เกิดข้อผิดพลาด:", e)

if __name__ == "__main__":
    run_agent("บันทึกขายลาเต้น้ำผึ้ง 3 แก้ว", '{"tool": "append_sale", "args": {"item": "ลาเต้น้ำผึ้ง", "qty": 3}}')
    run_agent("บันทึกขายชาไข่มุก -2 แก้ว", '{"tool": "append_sale", "args": {"item": "ชาไข่มุก", "qty": -2}}')