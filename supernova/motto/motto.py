import argparse
from supernova.utils import md5_encoding
from supernova.toybox.JiamengHuang import verifyMottoJiamengHuang
from supernova.toybox.H import verifyMottoH
from supernova.toybox.He import verifyMottoHe
from supernova.toybox.Li import verifyMottoLi
from supernova.toybox.Be import verifyMottoBe
from supernova.toybox.B import verifyMottoB
from supernova.toybox.C import verifyMottoC
from supernova.toybox.N import verifyMottoN
from supernova.toybox.O import verifyMottoO
from supernova.toybox.F import verifyMottoF
from supernova.toybox.Ne import verifyMottoNe
from supernova.toybox.Na import verifyMottoNa
from supernova.toybox.Mg import verifyMottoMg
from supernova.toybox.Al import verifyMottoAl
from supernova.toybox.Si import verifyMottoSi
from supernova.toybox.P import verifyMottoP
from supernova.toybox.S import verifyMottoS
from supernova.toybox.Cl import verifyMottoCl
from supernova.toybox.Ar import verifyMottoAr
from supernova.toybox.K import verifyMottoK
from supernova.toybox.Ca import verifyMottoCa
from supernova.toybox.Sc import verifyMottoSc
from supernova.toybox.Ti import verifyMottoTi
from supernova.toybox.V import verifyMottoV
from supernova.toybox.Cr import verifyMottoCr
from supernova.toybox.Mn import verifyMottoMn
from supernova.toybox.Fe import verifyMottoFe
from supernova.toybox.Co import verifyMottoCo
from supernova.toybox.Ni import verifyMottoNi
from supernova.toybox.Cu import verifyMottoCu
from supernova.toybox.Zn import verifyMottoZn
from supernova.toybox.Ga import verifyMottoGa
from supernova.toybox.Ge import verifyMottoGe
from supernova.toybox.As import verifyMottoAs
from supernova.toybox.Se import verifyMottoSe
from supernova.toybox.Br import verifyMottoBr
from supernova.toybox.Kr import verifyMottoKr
from supernova.toybox.Rb import verifyMottoRb
from supernova.toybox.Sr import verifyMottoSr
from supernova.toybox.Y import verifyMottoY
from supernova.toybox.Zr import verifyMottoZr
from supernova.toybox.Nb import verifyMottoNb
from supernova.toybox.Mo import verifyMottoMo
from supernova.toybox.Te import verifyMottoTe
from supernova.toybox.Ru import verifyMottoRu
from supernova.toybox.Rh import verifyMottoRh
from supernova.toybox.Pd import verifyMottoPd
from supernova.toybox.Ag import verifyMottoAg
from supernova.toybox.Cd import verifyMottoCd
from supernova.toybox.In import verifyMottoIn
from supernova.toybox.Sn import verifyMottoSn
from supernova.toybox.Sb import verifyMottoSb
from supernova.toybox.Te import verifyMottoTe
from supernova.toybox.I import verifyMottoI
from supernova.toybox.Xe import verifyMottoXe
from supernova.toybox.Cs import verifyMottoCs
from supernova.toybox.Ba import verifyMottoBa
from supernova.toybox.La import verifyMottoLa
from supernova.toybox.Ce import verifyMottoCe
from supernova.toybox.Pr import verifyMottoPr
from supernova.toybox.Nd import verifyMottoNd
from supernova.toybox.Pm import verifyMottoPm
from supernova.toybox.Sm import verifyMottoSm
from supernova.toybox.Eu import verifyMottoEu
from supernova.toybox.Gd import verifyMottoGd
from supernova.toybox.Tb import verifyMottoTb
from supernova.toybox.Dy import verifyMottoDy
from supernova.toybox.Ho import verifyMottoHo
from supernova.toybox.Er import verifyMottoEr
from supernova.toybox.Tm import verifyMottoTm
from supernova.toybox.Yb import verifyMottoYb
from supernova.toybox.Lu import verifyMottoLu
from supernova.toybox.Hf import verifyMottoHf
from supernova.toybox.Ta import verifyMottoTa
from supernova.toybox.W import verifyMottoW
from supernova.toybox.Re import verifyMottoRe
from supernova.toybox.Os import verifyMottoOs
from supernova.toybox.Ir import verifyMottoIr
from supernova.toybox.Pt import verifyMottoPt
from supernova.toybox.Au import verifyMottoAu
from supernova.toybox.Hg import verifyMottoHg
from supernova.toybox.Tl import verifyMottoTl
from supernova.toybox.Pb import verifyMottoPb
from supernova.toybox.Bi import verifyMottoBi
from supernova.toybox.Po import verifyMottoPo
from supernova.toybox.At import verifyMottoAt
from supernova.toybox.Rn import verifyMottoRn
from supernova.toybox.Fr import verifyMottoFr
from supernova.toybox.Ra import verifyMottoRa
from supernova.toybox.Ac import verifyMottoAc
from supernova.toybox.Th import verifyMottoTh
from supernova.toybox.Pa import verifyMottoPa
from supernova.toybox.U import verifyMottoU
from supernova.toybox.Np import verifyMottoNp
from supernova.toybox.Pu import verifyMottoPu
from supernova.toybox.Am import verifyMottoAm
from supernova.toybox.Cm import verifyMottoCm
from supernova.toybox.Bk import verifyMottoBk
from supernova.toybox.Cf import verifyMottoCf
from supernova.toybox.Es import verifyMottoEs
from supernova.toybox.Fm import verifyMottoFm
from supernova.toybox.Md import verifyMottoMd
from supernova.toybox.No import verifyMottoNo
from supernova.toybox.Lr import verifyMottoLr
from supernova.toybox.Rf import verifyMottoRf
from supernova.toybox.Db import verifyMottoDb
from supernova.toybox.Sg import verifyMottoSg
from supernova.toybox.Bh import verifyMottoBh
from supernova.toybox.Hs import verifyMottoHs
from supernova.toybox.Mt import verifyMottoMt
from supernova.toybox.Ds import verifyMottoDs
from supernova.toybox.Rg import verifyMottoRg
from supernova.toybox.Cn import verifyMottoCn
from supernova.toybox.Nh import verifyMottoNh
from supernova.toybox.Fl import verifyMottoFl
from supernova.toybox.Mc import verifyMottoMc
from supernova.toybox.Lv import verifyMottoLv
from supernova.toybox.Ts import verifyMottoTs
from supernova.toybox.Og import verifyMottoOg
from supernova.toybox.Uue import verifyMottoUue

def verifyMotto(P: argparse.Namespace):
    name = P.name
    motto = P.motto
    is_verified = False
    if name == "DPTechnology":
        is_verified = verifyMottoDPTechnology(motto)
    elif name == "JiamengHuang":
        is_verified = verifyMottoJiamengHuang(motto)
    elif name == "H":
        is_verified = verifyMottoH(motto)
    elif name == "He":
        is_verified = verifyMottoHe(motto)
    elif name == "Li":
        is_verified = verifyMottoLi(motto)
    elif name == "Be":
        is_verified = verifyMottoBe(motto)
    elif name == "B":
        is_verified = verifyMottoB(motto)
    elif name == "C":
        is_verified = verifyMottoC(motto)
    elif name == "N":
        is_verified = verifyMottoN(motto)
    elif name == "O":
        is_verified = verifyMottoO(motto)
    elif name == "F":
        is_verified = verifyMottoF(motto)
    elif name == "Ne":
        is_verified = verifyMottoNe(motto)
    elif name == "Na":
        is_verified = verifyMottoNa(motto)
    elif name == "Mg":
        is_verified = verifyMottoMg(motto)
    elif name == "Al":
        is_verified = verifyMottoAl(motto)
    elif name == "Si":
        is_verified = verifyMottoSi(motto)
    elif name == "P":
        is_verified = verifyMottoP(motto)
    elif name == "S":
        is_verified = verifyMottoS(motto)
    elif name == "Cl":
        is_verified = verifyMottoCl(motto)
    elif name == "Ar":
        is_verified = verifyMottoAr(motto)
    elif name == "K":
        is_verified = verifyMottoK(motto)
    elif name == "Ca":
        is_verified = verifyMottoCa(motto)
    elif name == "Sc":
        is_verified = verifyMottoSc(motto)
    elif name == "Ti":
        is_verified = verifyMottoTi(motto)
    elif name == "V":
        is_verified = verifyMottoV(motto)
    elif name == "Cr":
        is_verified = verifyMottoCr(motto)
    elif name == "Mn":
        is_verified = verifyMottoMn(motto)
    elif name == "Fe":
        is_verified = verifyMottoFe(motto)
    elif name == "Co":
        is_verified = verifyMottoCo(motto)
    elif name == "Ni":
        is_verified = verifyMottoNi(motto)
    elif name == "Cu":
        is_verified = verifyMottoCu(motto)
    elif name == "Zn":
        is_verified = verifyMottoZn(motto)
    elif name == "Ga":
        is_verified = verifyMottoGa(motto)
    elif name == "Ge":
        is_verified = verifyMottoGe(motto)
    elif name == "As":
        is_verified = verifyMottoAs(motto)
    elif name == "Se":
        is_verified = verifyMottoSe(motto)
    elif name == "Br":
        is_verified = verifyMottoBr(motto)
    elif name == "Kr":
        is_verified = verifyMottoKr(motto)
    elif name == "Rb":
        is_verified = verifyMottoRb(motto)
    elif name == "Sr":
        is_verified = verifyMottoSr(motto)
    elif name == "Y":
        is_verified = verifyMottoY(motto)
    elif name == "Zr":
        is_verified = verifyMottoZr(motto)
    elif name == "Nb":
        is_verified = verifyMottoNb(motto)
    elif name == "Mo":
        is_verified = verifyMottoMo(motto)
    elif name == "Te":
        is_verified = verifyMottoTe(motto)
    elif name == "Ru":
        is_verified = verifyMottoRu(motto)
    elif name == "Rh":
        is_verified = verifyMottoRh(motto)
    elif name == "Pd":
        is_verified = verifyMottoPd(motto)
    elif name == "Ag":
        is_verified = verifyMottoAg(motto)
    elif name == "Cd":
        is_verified = verifyMottoCd(motto)
    elif name == "In":
        is_verified = verifyMottoIn(motto)
    elif name == "Sn":
        is_verified = verifyMottoSn(motto)
    elif name == "Sb":
        is_verified = verifyMottoSb(motto)
    elif name == "Te":
        is_verified = verifyMottoTe(motto)
    elif name == "I":
        is_verified = verifyMottoI(motto)
    elif name == "Xe":
        is_verified = verifyMottoXe(motto)
    elif name == "Cs":
        is_verified = verifyMottoCs(motto)
    elif name == "Ba":
        is_verified = verifyMottoBa(motto)
    elif name == "La":
        is_verified = verifyMottoLa(motto)
    elif name == "Ce":
        is_verified = verifyMottoCe(motto)
    elif name == "Pr":
        is_verified = verifyMottoPr(motto)
    elif name == "Nd":
        is_verified = verifyMottoNd(motto)
    elif name == "Pm":
        is_verified = verifyMottoPm(motto)
    elif name == "Sm":
        is_verified = verifyMottoSm(motto)
    elif name == "Eu":
        is_verified = verifyMottoEu(motto)
    elif name == "Gd":
        is_verified = verifyMottoGd(motto)
    elif name == "Tb":
        is_verified = verifyMottoTb(motto)
    elif name == "Dy":
        is_verified = verifyMottoDy(motto)
    elif name == "Ho":
        is_verified = verifyMottoHo(motto)
    elif name == "Er":
        is_verified = verifyMottoEr(motto)
    elif name == "Tm":
        is_verified = verifyMottoTm(motto)
    elif name == "Yb":
        is_verified = verifyMottoYb(motto)
    elif name == "Lu":
        is_verified = verifyMottoLu(motto)
    elif name == "Hf":
        is_verified = verifyMottoHf(motto)
    elif name == "Ta":
        is_verified = verifyMottoTa(motto)
    elif name == "W":
        is_verified = verifyMottoW(motto)
    elif name == "Re":
        is_verified = verifyMottoRe(motto)
    elif name == "Os":
        is_verified = verifyMottoOs(motto)
    elif name == "Ir":
        is_verified = verifyMottoIr(motto)
    elif name == "Pt":
        is_verified = verifyMottoPt(motto)
    elif name == "Au":
        is_verified = verifyMottoAu(motto)
    elif name == "Hg":
        is_verified = verifyMottoHg(motto)
    elif name == "Tl":
        is_verified = verifyMottoTl(motto)
    elif name == "Pb":
        is_verified = verifyMottoPb(motto)
    elif name == "Bi":
        is_verified = verifyMottoBi(motto)
    elif name == "Po":
        is_verified = verifyMottoPo(motto)
    elif name == "At":
        is_verified = verifyMottoAt(motto)
    elif name == "Rn":
        is_verified = verifyMottoRn(motto)
    elif name == "Fr":
        is_verified = verifyMottoFr(motto)
    elif name == "Ra":
        is_verified = verifyMottoRa(motto)
    elif name == "Ac":
        is_verified = verifyMottoAc(motto)
    elif name == "Th":
        is_verified = verifyMottoTh(motto)
    elif name == "Pa":
        is_verified = verifyMottoPa(motto)
    elif name == "U":
        is_verified = verifyMottoU(motto)
    elif name == "Np":
        is_verified = verifyMottoNp(motto)
    elif name == "Pu":
        is_verified = verifyMottoPu(motto)
    elif name == "Am":
        is_verified = verifyMottoAm(motto)
    elif name == "Cm":
        is_verified = verifyMottoCm(motto)
    elif name == "Bk":
        is_verified = verifyMottoBk(motto)
    elif name == "Cf":
        is_verified = verifyMottoCf(motto)
    elif name == "Es":
        is_verified = verifyMottoEs(motto)
    elif name == "Fm":
        is_verified = verifyMottoFm(motto)
    elif name == "Md":
        is_verified = verifyMottoMd(motto)
    elif name == "No":
        is_verified = verifyMottoNo(motto)
    elif name == "Lr":
        is_verified = verifyMottoLr(motto)
    elif name == "Rf":
        is_verified = verifyMottoRf(motto)
    elif name == "Db":
        is_verified = verifyMottoDb(motto)
    elif name == "Sg":
        is_verified = verifyMottoSg(motto)
    elif name == "Bh":
        is_verified = verifyMottoBh(motto)
    elif name == "Hs":
        is_verified = verifyMottoHs(motto)
    elif name == "Mt":
        is_verified = verifyMottoMt(motto)
    elif name == "Ds":
        is_verified = verifyMottoDs(motto)
    elif name == "Rg":
        is_verified = verifyMottoRg(motto)
    elif name == "Cn":
        is_verified = verifyMottoCn(motto)
    elif name == "Nh":
        is_verified = verifyMottoNh(motto)
    elif name == "Fl":
        is_verified = verifyMottoFl(motto)
    elif name == "Mc":
        is_verified = verifyMottoMc(motto)
    elif name == "Lv":
        is_verified = verifyMottoLv(motto)
    elif name == "Ts":
        is_verified = verifyMottoTs(motto)
    elif name == "Og":
        is_verified = verifyMottoOg(motto)
    elif name == "Uue":
        is_verified = verifyMottoUue(motto)
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