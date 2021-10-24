import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

def giris_yap(meeting_id): #bizim zoom meetinglerinde şifre olmadığı için 2. bir argüman almıyoruz fonksiyonun içine ama sizinkiler şifreli ise "meeting_id"nin yanına "password" koyup aşağıda aynı şekilde tanımlarsanız sorunsuz çalışır.
    #Zoom uygulamasını açıyoruz.
    subprocess.call(["C:/Users/.../Zoom/bin/Zoom.exe"]) #içerideki linki kendi pcnizde zoomun bulunduğu uzantıyı koyun.
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
df = pd.read_csv("zamanlayici.csv") # zamanlama,meeting_id'ye karşılık gelecek şekilde başlamasını istediğiniz zamanı ve meeting kodunu giriyoruz.

while True:
    now = datetime.now().strftime("%H:%M") #zaman dilimimizi saat:dakika olarak verdiğimizi belirtiyoruz.
    if now in str(df["zamanlama"]):
        row = df.loc[df["zamanlama"] == now]
        m_id = str(row.iloc[0,1])

        giris_yap(01231231234) # fonksiyonumuzu çağırıp çalıştırdığımız yer buraya kendi meeting_id'nizi yazın.
        time.sleep(40)
        print("Giriş Yapıldı!")



