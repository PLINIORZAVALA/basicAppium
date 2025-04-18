Comando para ejecutar appium en consola: appium --port 4725
____________________________________________________________
STRUCTURE: POST http://localhost:4725/session
{
  "desiredCapabilities": {
    "platformName": "Android",
    "deviceName": "HUAWEI CAM-L03",
    "udid": "NSXDU17627001880",
    "appPackage": "com.huawei.camera",
    "appActivity": ".CameraActivity",
    "automationName": "UiAutomator2",
    "noReset": true
  }
}
ERROR: 
{
    "value": {
        "error": "invalid argument",
        "message": "Some of the provided parameters are not known\nYou have provided none",
        "stacktrace": "BadParametersError: Some of the provided parameters are not known\nYou have provided none\n    at checkParams (C:\\Users\\USUARI0\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\@appium\\base-driver\\lib\\protocol\\protocol.js:126:15)\n    at asyncHandler (C:\\Users\\USUARI0\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\@appium\\base-driver\\lib\\protocol\\protocol.js:364:7)\n    at C:\\Users\\USUARI0\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\@appium\\base-driver\\lib\\protocol\\protocol.js:514:15\n    at Layer.handle [as handle_request] (C:\\Users\\USUARI0\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\express\\lib\\router\\layer.js:95:5)\n    at next (C:\\Users\\USUARI0\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\express\\lib\\router\\route.js:149:13)\n    at Route.dispatch (C:\\Users\\USUARI0\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\express\\lib\\router\\route.js:119:3)\n    at Layer.handle [as handle_request] (C:\\Users\\USUARI0\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\express\\lib\\router\\layer.js:95:5)\n    at C:\\Users\\USUARI0\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\express\\lib\\router\\index.js:284:15\n    at Function.process_params (C:\\Users\\USUARI0\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\express\\lib\\router\\index.js:346:12)\n    at next (C:\\Users\\USUARI0\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\express\\lib\\router\\index.js:280:10)\n    at logger (C:\\Users\\USUARI0\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\morgan\\index.js:144:5)\n    at Layer.handle [as handle_request] (C:\\Users\\USUARI0\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\express\\lib\\router\\layer.js:95:5)\n    at trim_prefix (C:\\Users\\USUARI0\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\express\\lib\\router\\index.js:328:13)\n    at C:\\Users\\USUARI0\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\express\\lib\\router\\index.js:286:9\n    at Function.process_params (C:\\Users\\USUARI0\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\express\\lib\\router\\index.js:346:12)\n    at next (C:\\Users\\USUARI0\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\express\\lib\\router\\index.js:280:10)\n    at jsonParser (C:\\Users\\USUARI0\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\body-parser\\lib\\types\\json.js:122:7)\n    at Layer.handle [as handle_request] (C:\\Users\\USUARI0\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\express\\lib\\router\\layer.js:95:5)\n    at trim_prefix (C:\\Users\\USUARI0\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\express\\lib\\router\\index.js:328:13)\n    at C:\\Users\\USUARI0\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\express\\lib\\router\\index.js:286:9\n    at Function.process_params (C:\\Users\\USUARI0\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\express\\lib\\router\\index.js:346:12)\n    at next (C:\\Users\\USUARI0\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\express\\lib\\router\\index.js:280:10)"
    },
    "sessionId": null
}
EJECUCION EN CONSOLA: appium --port 4725
___________________________________________________________________________________________________________________________
Comando para saver el appPackage: adb shell pm list packages
"appPackage": "package:com.huawei.camera"

Comando para saber: adb shell dumpsys activity activities | findstr ResumedActivity
"appActivity": ".CameraActivity"

Instalación de driver aiautomator2 : appium driver install uiautomator2
"automationName": "UiAutomator2"

