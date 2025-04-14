from appium import webdriver
import threading

# Configuración común (MT4)
COMMON_CAPS = {
    "platformName": "Android",
    "appPackage": "com.metatrader4",  # Ajusta al paquete de MT4
    "appActivity": ".MainActivity",
    "automationName": "UiAutomator2",
    "noReset": True
}

# Lista de dispositivos (ejemplo)
DEVICES = [
    {"udid": "NSXDU17627001880", "port": 4723},
    {"udid": "R92W500PNSL", "port": 4724}
]

# Inicia sesiones
drivers = []
for device in DEVICES:
    driver = webdriver.Remote(
        f'http://localhost:{device["port"]}/wd/hub',
        {**COMMON_CAPS, "udid": device["udid"]}
    )
    drivers.append(driver)