import subprocess

def get_udid():
    """
    Retrieves the unique device identifier (UDID) using the Android Debug Bridge (ADB).

    Returns:
        str: The UDID of the connected device.

    Raises:
        subprocess.CalledProcessError: If there is an error while calling the `adb devices` command.
    """
    try:
        result = subprocess.check_output(['adb', 'devices']).decode('utf-8')
        udid = result.strip().split('\n')[1].split('\t')[0]

        return udid
    except subprocess.CalledProcessError as e:
        print(f'Error call adb: {e}')
    
    return None

def get_android_version():
    """
    Get the version of the Android operating system.

    :return: The version of the Android operating system as a string.
    :rtype: str or None
    """
    try:
        android_version = subprocess.check_output(['adb', 'shell', 'getprop', 'ro.build.version.release']).decode('utf-8').strip()
        
        return android_version

    except subprocess.CalledProcessError as e:
        print(f'Error call adb: {e}')
    
    return None
