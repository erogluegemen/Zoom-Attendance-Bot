import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

def giris_yap(meeting_id):
    #Zoom uygulamasını açıyoruz.
    subprocess.call(["C:/Users/Erogl/AppData/Roaming/Zoom/bin/Zoom.exe"])
    time.sleep(10)

    #Giris butonuna tıklatıyoruz.
    join_btn = pyautogui.locateCenterOnScreen("join_button.png")
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    #MeetingID'yi yazdırıyoruz.
    meeting_id_btn = pyautogui.locateCenterOnScreen("meeting_id_button.png")
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.click()
    pyautogui.write(meeting_id)

    #Kamera-Mikrafon erişimlerini kapattırıyoruz.
    media_btn = pyautogui.locateAllOnScreen("media_btn.png")
    for btn in media_btn:
        pyautogui.moveTo(btn)
        pyautogui.click()
        time.sleep(2)

    #Son olarak katıl butonuna basıyoruz.
    join_btn = pyautogui.locateCenterOnScreen("join_btn.png")
    pyautogui.moveTo(join_btn)
    pyautogui.click()

#Zamanlayıcıyı ayarlıyoruz.
df = pd.read_csv("zamanlayici.csv")

while True:
    now = datetime.now().strftime("%H:%M") #zaman dilimimizi saat:dakika olarak verdiğimizi belirtiyoruz.
    if now in str(df["zamanlama"]):
        row = df.loc[df["zamanlama"] == now]
        m_id = str(row.iloc[0,1])

        giris_yap("93279307629")
        time.sleep(40)
        print("Giriş Yapıldı!")



