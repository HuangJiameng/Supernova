from supernova.utils import md5_encoding

def verifyMottoJiamengHuang(public_string: str) -> bool:
    '''

    Verify if a public string is JiamengHuang's motto.

    Parameters:
    ---------
    public_string: string, a public string from user input.

    Returns:
    -------
    is_verified: bool, if the string matches with the certain motto,
        return True.
    '''
    md5_string = md5_encoding(public_string)
    is_verified = False
    if md5_string == "2418e06198cb88fca52e2d20658e16fa":
        is_verified = True
    return is_verified
