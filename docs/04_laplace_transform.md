# 4. Laplace transform

## Purpose

The Laplace transform converts common system operations into algebra:

$$
x(t)*h(t)\longleftrightarrow X(s)H(s),
$$

and, for the unilateral transform,

$$
\mathcal{L}\{y'(t)\}=sY(s)-y(0^-).
$$

Initial conditions therefore appear explicitly when transforming differential equations.

## A reliable workflow

1. Transform each term and retain the initial conditions.
2. Collect all terms containing $Y(s)$.
3. Solve algebraically for $Y(s)$.
4. Factor the denominator and predict the time-domain form from its poles.
5. Use partial fractions to find coefficients.
6. Check the initial value and, when permitted, the final value.

## Partial fractions predict time functions

Distinct real poles:

$$
\frac{A}{s-p_1}+\frac{B}{s-p_2}
\longleftrightarrow
Ae^{p_1t}+Be^{p_2t}.
$$

A repeated pole $p$ produces powers of time:

$$
\frac{A}{s-p}+\frac{B}{(s-p)^2}
\longleftrightarrow
Ae^{pt}+Bte^{pt}.
$$

A complex-conjugate pair $\sigma\pm j\omega$ produces

$$
e^{\sigma t}\left[C_1\cos(\omega t)+C_2\sin(\omega t)\right].
$$

Poles determine the available modes. Partial-fraction coefficients determine their weights.

