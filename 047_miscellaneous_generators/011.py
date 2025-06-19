"""

Write a Python program to create a generator that generates all possible permutations of a string.

abc     =>  abc, acb, bac, bca, cab, cba

print   =>  print, pritn, prnit, prnti, prtin, prtni, pirnt, pirtn, pinrt, pintr, pitrn, pitnr, pnrit, pnrti, pnirt,
            pnitr, pntri, pntir, ptrin, ptrni, ptirn, ptinr, ptnri, ptnir, rpint, rpitn, rpnit, rpnti, rptin, rptni,
            ripnt, riptn, rinpt, rintp, ritpn, ritnp, rnpit, rnpti, rnipt, rnitp, rntpi, rntip, rtpin, rtpni, rtipn,
            rtinp, rtnpi, rtnip, iprnt, iprtn, ipnrt, ipntr, iptrn, iptnr, irpnt, irptn, irnpt, irntp, irtpn, irtnp,
            inprt, inptr, inrpt, inrtp, intpr, intrp, itprn, itpnr, itrpn, itrnp, itnpr, itnrp, nprit, nprti, npirt,
            npitr, nptri, nptir, nrpit, nrpti, nript, nritp, nrtpi, nrtip, niprt, niptr, nirpt, nirtp, nitpr, nitrp,
            ntpri, ntpir, ntrpi, ntrip, ntipr, ntirp, tprin, tprni, tpirn, tpinr, tpnri, tpnir, trpin, trpni, tripn,
            trinp, trnpi, trnip, tiprn, tipnr, tirpn, tirnp, tinpr, tinrp, tnpri, tnpir, tnrpi, tnrip, tnipr, tnirp

"""

from itertools import permutations
import textwrap
from typing import Generator


def permute_string(s: str) -> Generator[str, None, None]:
    yield from ("".join(p) for p in permutations(s, r=len(s)))


def main():
    data = ["abc", "print"]

    for _ in data:
        print("\n".join(textwrap.wrap(" ".join(list(permute_string(_))), width=100)))


if __name__ == "__main__":
    main()
