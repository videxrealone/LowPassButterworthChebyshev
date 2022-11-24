# Solving Low Pass Cauer Filters using Butterworth & Chebyshev Methods
---
## Overview

Butterworth had a reputation for solving "impossible" mathematical problems. At the time, filter design required a considerable amount of designer experience due to limitations of the theory then in use. The filter was not in common use for over 30 years after its publication. Butterworth stated that:

## Butterworth VS Chebyshev

*   The frequency response of the Butterworth filter is maximally flat (i.e. has no ripples) in the passband and rolls off towards zero in the stopband.[2] When viewed on a logarithmic Bode plot, the response slopes off linearly towards negative infinity. A first-order filter's response rolls off at −6 dB per octave (−20 dB per decade) (all first-order lowpass filters have the same normalized frequency response). A second-order filter decreases at −12 dB per octave, a third-order at −18 dB and so on. Butterworth filters have a monotonically changing magnitude function with ω, unlike other filter types that have non-monotonic ripple in the passband and/or the stopband.

*   Compared with a Chebyshev Type I/Type II filter or an elliptic filter, the Butterworth filter has a slower roll-off, and thus will require a higher order to implement a particular stopband specification, but Butterworth filters have a more linear phase response in the passband than Chebyshev Type I/Type II and elliptic filters can achieve.

## Transfer Function

The gain {\displaystyle G(\omega )}G(\omega ) of an {\displaystyle n}nth-order Butterworth low-pass filter is given in terms of the transfer function {\displaystyle H(s)}H(s) as

![image](https://user-images.githubusercontent.com/91763346/203866875-b2f6edeb-09d4-41b0-b3ed-ae1e92212e36.png)

We wish to determine the transfer function (from Laplace transform). such that:

![image](https://user-images.githubusercontent.com/91763346/203867050-c0793ec0-01a1-4295-817c-9223e8deb76e.png)


# Python solution 

## Approach

To solve the equations and to optimize the code and execution time, I had to try and implement each and every equation as a function, this method had helped me gain time and keep my brains while coding because the equations had common parameters that use other functions to get results.

I had used some global variables to make it even easier to pass input into the functions.

The code isn't the best but could be improved.

Check the python file withing this repo to try out the script.
** PS : Python 3.10 must be running. **



