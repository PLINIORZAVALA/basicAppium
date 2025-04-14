from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

def run_test():
    try:
        print("Configurando capabilities...")
        caps = {
            "platformName": "Android",
            "deviceName": "Android Device",
            "udid": "R92W500PNSL",  # ¡Verifica que este UDID es correcto!
            "appPackage": "com.android.settings",
            "appActivity": ".Settings",
            "automationName": "UiAutomator2",
            "noReset": True
        }

        print("Inicializando driver...")
        driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        
        print("Abriendo configuración de WiFi...")
        wifi_btn = driver.find_element(AppiumBy.XPATH, "//*[contains(@text, 'Wi-Fi')]")
        wifi_btn.click()
        time.sleep(3)
        
    except Exception as e:
        print(f"ERROR durante la ejecución: {str(e)}")
    finally:
        if 'driver' in locals():
            driver.quit()
        print("Prueba finalizada")

if __name__ == "__main__":
    run_test()