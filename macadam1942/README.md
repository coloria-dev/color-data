# MacAdam (ellipses) data

Extracted from

David L. MacAdam,
Visual Sensitivities to Color Differences in Daylight,
Journal of the Optional Society of America,
Volume 32, May, 1942, Number 5,
<https://doi.org/10.1364/JOSA.32.000247>.

with the help of [Tabula](https://github.com/tabulapdf/tabula).

#### File description

- `table1.dat`: Filters for chromaticity instrument (in Illuminant A).
  Filter number and XYZ values are given; m, x, and y can be computed from
  them.
  ```
  i   X       Y       Z
  ```
- `table2.dat`: Standard deviations of color matching.
  ```
  0 degree filter number;
  90 degree filter number;
  theta degree average setting;
  delta theta degree standard deviation;
  average chromaticity x;
  average chromaticity y;
  Distance from 0 degree point = s;
  delta s standard deviation;
  delta y / delta x;
  ```
- `table3.dat`: Standard deviations of color matching. (Ellipse data.)
  ```
  average chromaticity x;
  average chromaticity y;
  0 degree filter number;
  90 degree filter number;
  theta degree average setting;
  delta theta degree standard deviation;
  delta y / delta x;
  delta s standard deviation;
  ```
