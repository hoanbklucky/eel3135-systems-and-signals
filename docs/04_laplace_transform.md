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

## Transform pairs worth understanding

Do not memorize a long table without patterns. The most useful pairs are

| $x(t)$ | $X(s)$ |
|---|---|
| $u(t)$ | $1/s$ |
| $e^{-at}u(t)$ | $1/(s+a)$ |
| $t^n u(t)$ | $n!/s^{n+1}$ |
| $\cos(\omega t)u(t)$ | $s/(s^2+\omega^2)$ |
| $\sin(\omega t)u(t)$ | $\omega/(s^2+\omega^2)$ |

Two properties generate many additional pairs:

$$
x(t-t_0)u(t-t_0)\longleftrightarrow e^{-st_0}X(s),
$$

$$
e^{at}x(t)\longleftrightarrow X(s-a).
$$

The first represents time delay; the second shifts poles in the $s$-plane.

## Worked example: direct transform

Find the Laplace transform of

$$
x(t)=3e^{-2t}u(t)-4e^{-5t}u(t).
$$

By linearity,

$$
X(s)=\frac{3}{s+2}-\frac{4}{s+5}
=\frac{-s+7}{(s+2)(s+5)}.
$$

The poles at $-2$ and $-5$ reveal the two exponential modes. Combining the fractions does not change those modes unless a pole-zero cancellation occurs.

## Worked inverse: predict before calculating

Suppose

$$
Y(s)=\frac{2s+7}{(s+1)(s+3)}.
$$

Before finding coefficients, the distinct poles predict

$$
y(t)=C_1e^{-t}+C_2e^{-3t}.
$$

Now write

$$
\frac{2s+7}{(s+1)(s+3)}=\frac{A}{s+1}+\frac{B}{s+3}.
$$

Using cover-up,

$$
A=\left.\frac{2s+7}{s+3}\right|_{s=-1}=\frac52,
\qquad
B=\left.\frac{2s+7}{s+1}\right|_{s=-3}=-\frac12.
$$

Therefore

$$
y(t)=\left(\frac52e^{-t}-\frac12e^{-3t}\right)u(t).
$$

Check: $y(0^+)=2$, which agrees with $\lim_{s\to\infty}sY(s)=2$.

## Repeated and complex poles

For

$$
Y(s)=\frac{1}{(s+2)^2},
$$

the repeated pole produces

$$
y(t)=te^{-2t}u(t).
$$

For

$$
Y(s)=\frac{s+2}{(s+2)^2+9},
$$

the poles are $-2\pm j3$, so

$$
y(t)=e^{-2t}\cos(3t)u(t).
$$

If the numerator were 3 instead of $s+2$, the result would be $e^{-2t}\sin(3t)u(t)$.

## Solving a differential equation with initial conditions

Consider

$$
y''+3y'+2y=x(t),
$$

with $y(0^-)=1$, $y'(0^-)=0$, and $x(t)=u(t)$. Transforming term by term gives

$$
[s^2Y-s]+3[sY-1]+2Y=\frac1s.
$$

Therefore

$$
Y(s)=\frac{s+3+1/s}{(s+1)(s+2)}.
$$

This is the **total response** because both the input and initial conditions are present. Module 6 shows how to compute their contributions separately.

## Initial- and final-value checks

When there is no impulse at the origin,

$$
y(0^+)=\lim_{s\to\infty}sY(s).
$$

The final-value theorem is

$$
\lim_{t\to\infty}y(t)=\lim_{s\to0}sY(s),
$$

but only if every pole of $sY(s)$ lies strictly in the open left half-plane. Always check the poles before using it.

## Common mistakes

- Dropping $y(0^-)$ or $y'(0^-)$ in derivative transforms.
- Starting partial fractions before factoring and predicting the response form.
- Omitting the $t$ factor caused by repeated poles.
- Applying the final-value theorem to an unstable or sustained-oscillatory response.
- Treating a zero as if it creates a time-domain mode. Poles create modes; zeros change or cancel their weights.

## Practice

1. Predict the form of the inverse transform of $1/[(s+1)^2(s+4)]$.
2. Find $\mathcal L^{-1}\{(s+4)/[(s+2)^2+4]\}$.
3. Can the final-value theorem be used for $Y(s)=1/(s^2+4)$?

<details><summary>Answers</summary>

1. $(C_1e^{-t}+C_2te^{-t}+C_3e^{-4t})u(t)$.
2. $e^{-2t}[\cos(2t)+\sin(2t)]u(t)$, after writing $s+4=(s+2)+2$.
3. No. The poles remain on the imaginary axis, so the response does not converge to a final value.

</details>

