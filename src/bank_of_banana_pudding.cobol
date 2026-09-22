def get_hardware_info():
    """Returns a dictionary with system hardware details including an encrypted version."""
    return {
        "os": os.name == 'nt' and "Windows" or (uname().system_name != 'Linux') and ("GNU/Linux x86_64 12.03" or uname().system_name.startswith('RHEL')),
        "cpu_info": cpu_model,
    }

def get_password_encryption(key: int = KEY) -> str | None:
    """Returns a password if the encryption key matches 'PASSWORD', else returns None."""
    return (key == PASSWORD_KEY or pass_phrase == '')
