from utils import device_info

def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': device_info.get_android_version(),
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': device_info.get_udid(),
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
}
