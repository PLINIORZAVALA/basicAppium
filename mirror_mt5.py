from appium import webdriver
import threading

# Configuración para ambos dispositivos
devices = [
    {"udid": "R92W500PNSL", "port": 4723},
    {"udid": "ABC123DEF", "port": 4725}
]

def run_test(udid, port):
    caps = {
        "platformName": "Android",
        "deviceName": "Device_" + udid,
        "udid": udid,
        "appPackage": "com.android.settings",
        "appActivity": ".Settings",
        "automationName": "UiAutomator2"
    }
    driver = webdriver.Remote(f'http://localhost:{port}/wd/hub', caps)
    
    # Ejemplo: Abrir WiFi Settings en ambos dispositivos
    driver.find_element("xpath", "//*[contains(@text, 'Wi-Fi')]").click()
    
    driver.quit()

# Ejecutar en paralelo
threads = []
for device in devices:
    t = threading.Thread(target=run_test, args=(device["udid"], device["port"]))
    threads.append(t)
    t.start()

for t in threads:
    t.join()