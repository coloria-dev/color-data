Data sources:

- https://law.resource.org/pub/us/cfr/ibr/003/cie.15.2004.tables.xls
- https://github.com/colour-science/colour/blob/2c6156405f48934553dacbf8be4ae26b40486992/colour/colorimetry/datasets/illuminants/sds.py

#### D

These files give the data to construct the D50, D55, D64, and D75 illuminants.
From CIE 15:2004. Colorimetry, 3rd edition, 2004 (page 69, note 5):

The method required to calculate the values for the relative spectral power
distributions of illuminants D50, D55, D65, and D75, in Table T.1 is as follows

1. Multiply the nominal correlated colour temperature (5000 K, 5500 K 6500 K or 7500
   K) by 1.4388/1.4380.
2. Calculate XD and YD using the equations given in the text.
3. Calculate M1 and M2 using the equations given in the text.
4. Round M1 and M2 to three decimal places.
5. Calculate S(lambda) every 10 nm by
   S(lambda) = S0(lambda) + M1 S1(lambda) + M2 S2(lambda)
   using values of S0(lambda), S1(lambda) and S2(lambda) from Table T.2.
6. Interpolate the 10 nm values of S(lambda) linearly to obtain values at intermediate
   wavelengths.

The standard gives values every 5nm, but every other value is just an interpolation from
10nm data. No idea why they are listed in the standard.
