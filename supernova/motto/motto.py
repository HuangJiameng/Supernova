import argparse
from supernova.utils import md5_encoding
import supernova.toybox.verifyMottoJiamengHuang

def verifyMotto(P: argparse.Namespace):
    name = P.name
    motto = P.motto
    is_verified = False
    if name == "DPTechnology":
        is_verified = verifyMottoDPTechnology(motto)
    elif name == "JiamengHuang":
        is_verified = verifyMottoJiamengHuang(motto)
    else:
        assert RuntimeError("Your input name is not valid for this test!")

    if is_verified:
        print(f"Your input '{motto}' matches with {name}'s motto! ")
    else:
        print(f"Your input '{motto}' doesn't match with {name}'s motto! ")


def verifyMottoDPTechnology(public_string: str) -> bool:
    '''

    Verify if a public string is DP Technology's motto.

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
    if md5_string == "894f4cc4639856a9345e8c686818528f":
        is_verified = True
    return is_verified