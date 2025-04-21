import requests
import time
import random

# بيانات Telegram
TELEGRAM_TOKEN = "7724250065:AAGZ_Io0YYakLmFl96WV7lZQ"
CHAT_ID = "7147989291"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

def get_fake_signal():
    signals = ["شراء", "بيع"]
    decision = random.choices(signals, weights=[0.55, 0.45])[0]
    return decision

def get_fake_result():
    return random.choice(["ربح", "خسارة"])

send_telegram("تم تشغيل البوت بنجاح، جاري مراقبة السوق ...")

while True:
    decision = get_fake_signal()
    result = get_fake_result()
    msg = f"صفقة جديدة: {decision} - النتيجة: {result}"
    send_telegram(msg)
    time.sleep(60)
