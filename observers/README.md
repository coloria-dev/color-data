### Classical observers

- CIE 1931 2 degrees standard observer.
- CIE 1964 10 degrees standard observer.
- CIE (2012) 2-deg XYZ physiologically-relevant colour matching functions

Sources:
- <https://www.rit.edu/cos/colorscience/rc_useful_data.php> (360-830 nm, 5 nm steps)
- <https://law.resource.org/pub/us/cfr/ibr/003/cie.15.2004.tables.xls> (380-780 nm, 5 nm
  steps)

The CIE Technical Report Colorimetry (from where the above data are) says:

> Section 11 provides abridged tables that can be used in many practical calculations.
> On the use of these tables see Section 7.2. The values of relative spectral power
> distribution of CIE standard illuminant 065 given in Table T.1 at 5 nm intervals are
> consistent with the values from 300 nm to 830 nm at 1 nm intervals and with six
> significant figures given in CIE standard illuminants for colorimetry (CIE, 1998c).
> They have been taken from the tables of the Standard.

On

- <http://cvrl.ioo.ucl.ac.uk/cie.htm>
- <https://www.biblioteca.iqfr.csic.es/images/REPOSITORIO/CIE/ISO_CIE11664-1.pdf>

one can find 1nm data that is consistent with the data in the above XLS files and also
matches 1nm the checksums. Hence, assume that this is the actual standard data; use it
here.

### New observers

Sources:
- <http://cvrl.ioo.ucl.ac.uk/cie.htm>

> These 2-deg colour matching functions are linear transformations of the 2-deg cone
> fundamentals of Stockman & Sharpe (2000), ratified by the CIE (2006) as the new
> physiologically-relevant fundamental CIE CMFs.
>
> The transformation produces CMFs similar to the original 1931 x, y and z CMFs, a
> colour space still favoured by many engineers and scientists.
> [...]

The new observers improve upon the old ones in some aspects, for example the sums of
their values. In the old observers, the sums over x, y, and z differ by around 3.0-e2,
leading to funny tristimulus whitepoint for the equal-energy observer. (Should be [100,
100, 100].) In the new observers, the sum difference is only about 3.0e-6.
