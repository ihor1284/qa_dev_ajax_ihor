import subprocess

def get_udid() -> str:
    """
    Retrieves the Unique Device Identifier (UDID) of the connected Android device.

    :return: The UDID of the connected Android device as a string.
    :rtype: str
    """
    result = subprocess.check_output(['adb', 'devices']).decode('utf-8')
    udid = result.strip().split('\n')[1].split('\t')[0]

    return udid

def get_android_version() -> str:
    """
    Returns the Android version of the device.

    :return: A string representing the Android version.
    :rtype: str
    """
    android_version = subprocess.check_output(['adb', 'shell', 'getprop', 'ro.build.version.release']).decode('utf-8').strip()
    
    return android_version

