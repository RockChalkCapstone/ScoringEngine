import pwd


def check_user_exists(userName: str) -> bool:
    """
    Checks if user exists on the machine

    Parameters
    ----------
    userName : str
        Username of user being checked for existence

    Returns
    -------
    bool
        True if user exists
        False if user does not exist

    """
    try:
    # Searches /etc/passwd for entry with username userName
        pwd.getpwnam(userName)
        print(True)
        return True
    except KeyError:
        print(False)
        return False