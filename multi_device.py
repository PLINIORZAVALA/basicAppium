from appium import webdriver
import threading

# Configuración de ambos dispositivos
devices = [
    {
        "udid": "R92W500PNSL",
        "port": 4723,
        "system_port": 8200  # Puerto para evitar conflicto en Android
    },
    {
        "udid": "NSXDU17627001880",
        "port": 4725,
        "system_port": 8201
    }
]

def run_test(device):
    caps = {
        "platformName": "Android",
        "deviceName": device["udid"],
        "udid": device["udid"],
        "appPackage": "com.android.settings",  # App de ejemplo (Ajusta según tu app)
        "appActivity": ".Settings",
        "automationName": "UiAutomator2",
        "systemPort": device["system_port"]  # Evita conflicto de puertos
    }
    
    driver = webdriver.Remote(f'http://localhost:{device["port"]}/wd/hub', caps)
    
    # Ejemplo: Abrir la configuración de WiFi en ambos dispositivos
    driver.find_element_by_xpath("//*[contains(@text, 'Wi-Fi')]").click()
    
    driver.quit()

# Ejecutar en paralelo
threads = []
for device in devices:
    t = threading.Thread(target=run_test, args=(device,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()