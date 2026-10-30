# 4. Laplace transform

## Learning goals

After studying this module, you should be able to:

- explain why the unilateral Laplace transform is useful for causal LTI systems;
- calculate transforms from a short table and a small set of properties;
- retain initial conditions when transforming differential equations;
- predict an inverse transform from its pole pattern before finding coefficients;
- calculate inverse transforms for distinct, repeated, and complex-conjugate poles;
- connect pole locations with decay, growth, oscillation, and stability;
- use the initial- and final-value theorems as checks.

This module focuses on causal signals and the unilateral Laplace transform. The main goal is to connect the algebra in the $s$-domain with physical behavior in time.

## Why introduce another transform?

Time-domain analysis remains the foundation of systems and signals, but several operations can require substantial calculation:

$$
y(t)=x(t)*h(t),
$$

$$
a_ny^{(n)}+\cdots+a_1y'+a_0y=b_mx^{(m)}+\cdots+b_0x.
$$

The Laplace transform converts these operations into algebra:

| Time-domain operation | $s$-domain operation |
|---|---|
| convolution | multiplication |
| differentiation | multiplication by $s$, plus initial-condition terms |
| integration | division by $s$ |
| time delay | multiplication by $e^{-sT}$ |

For example,

$$
y(t)=x(t)*h(t)
\quad\longleftrightarrow\quad
Y(s)=X(s)H(s).
$$

The transform does more than shorten a calculation. Factoring an $s$-domain denominator reveals the exponential and oscillatory modes that may appear in the time-domain response.

## Definition of the unilateral Laplace transform

For a causal signal $x(t)$, the unilateral Laplace transform is

$$
X(s)=\mathcal L\{x(t)\}
=\int_{0^-}^{\infty}x(t)e^{-st}\,dt,
$$

where

$$
s=\sigma+j\omega.
$$

The kernel can be separated as

$$
e^{-st}=e^{-\sigma t}e^{-j\omega t}.
$$

The factor $e^{-\sigma t}$ supplies exponential weighting. The factor $e^{-j\omega t}$ carries sinusoidal information. This is why the Laplace transform can describe both growth or decay and oscillation.

The lower limit $0^-$ allows initial conditions immediately before switching to appear in derivative formulas. For ordinary functions without an impulse at the origin, integrating from $0$ gives the same calculation.

## A transform calculated from the definition

Let

$$
x(t)=e^{-at}u(t).
$$

Then

$$
X(s)=\int_0^\infty e^{-at}e^{-st}\,dt
=\int_0^\infty e^{-(s+a)t}\,dt
=\frac{1}{s+a}.
$$

Therefore,

$$
\boxed{e^{-at}u(t)\longleftrightarrow\frac{1}{s+a}}.
$$

This pair already contains an important connection: a pole at $s=-a$ produces the time-domain mode $e^{-at}$.

## Transform pairs worth understanding

Do not begin by memorizing a long table. Learn the following patterns, then use properties to generate new pairs.

| $x(t)$ | $X(s)$ |
|---|---|
| $\delta(t)$ | $1$ |
| $u(t)$ | $1/s$ |
| $e^{-at}u(t)$ | $1/(s+a)$ |
| $t^n u(t)$ | $n!/s^{n+1}$ |
| $\cos(\omega_0t)u(t)$ | $s/(s^2+\omega_0^2)$ |
| $\sin(\omega_0t)u(t)$ | $\omega_0/(s^2+\omega_0^2)$ |
| $e^{-at}\cos(\omega_0t)u(t)$ | $(s+a)/[(s+a)^2+\omega_0^2]$ |
| $e^{-at}\sin(\omega_0t)u(t)$ | $\omega_0/[(s+a)^2+\omega_0^2]$ |

The denominator shows the pole pattern. For example,

$$
(s+a)^2+\omega_0^2=0
$$

gives the poles

$$
s=-a\pm j\omega_0.
$$

The real part sets the exponential envelope, while the imaginary part sets the oscillation frequency.

## Properties that do the calculation

Suppose

$$
x(t)\longleftrightarrow X(s).
$$

The most useful unilateral-transform properties are:

| Property | Time domain | $s$-domain | Typical use |
|---|---|---|---|
| linearity | $ax(t)+by(t)$ | $aX(s)+bY(s)$ | combine known pairs |
| time delay | $x(t-T)u(t-T)$ | $e^{-sT}X(s)$ | delayed signals |
| exponential shift | $e^{at}x(t)$ | $X(s-a)$ | shifted poles |
| time scaling, $a>0$ | $x(at)$ | $X(s/a)/a$ | compressed or expanded signals |
| time differentiation | $x'(t)$ | $sX(s)-x(0^-)$ | differential equations |
| time integration | $\int_0^t x(\tau)d\tau$ | $X(s)/s$ | accumulators |
| multiplication by $t$ | $tx(t)$ | $-dX(s)/ds$ | polynomial-weighted signals |
| convolution | $x(t)*h(t)$ | $X(s)H(s)$ | LTI system response |

For a second derivative,

$$
\mathcal L\{x''(t)\}
=s^2X(s)-sx(0^-)-x'(0^-).
$$

The pattern continues for higher derivatives. Each derivative adds one power of $s$ and one additional initial-condition term.

### Example: linearity

Find the transform of

$$
x(t)=3e^{-2t}u(t)-4e^{-5t}u(t).
$$

Using linearity,

$$
X(s)=\frac{3}{s+2}-\frac{4}{s+5}
=\frac{-s+7}{(s+2)(s+5)}.
$$

The combined fraction still contains poles at $-2$ and $-5$. Combining fractions does not change the available modes unless a pole-zero cancellation occurs.

### Example: time delay

Start with

$$
tu(t)\longleftrightarrow\frac{1}{s^2}.
$$

Then

$$
x(t)=2(t-3)u(t-3)
$$

has transform

$$
X(s)=\frac{2e^{-3s}}{s^2}.
$$

The exponential factor $e^{-3s}$ represents a delay of three seconds. It does not represent a pole at $-3$.

## Convolution, transfer functions, and initial conditions

For a causal LTI system initially at rest,

$$
y(t)=x(t)*h(t)
$$

becomes

$$
Y(s)=X(s)H(s),
$$

where

$$
H(s)=\mathcal L\{h(t)\}
=\left.\frac{Y(s)}{X(s)}\right|_{\text{zero initial conditions}}.
$$

The zero-initial-condition qualification matters. If a system starts with stored energy, then $H(s)X(s)$ gives only the zero-state response. The total response also contains a zero-input contribution:

$$
y(t)=y_{zi}(t)+y_{zs}(t).
$$

The detailed calculation appears in [Module 6: Zero-input, zero-state, and total response](06_response_decomposition.md).

## Differential equations become algebraic equations

Consider

$$
y''+3y'+2y=x(t),
$$

with

$$
y(0^-)=1,
\qquad
y'(0^-)=0,
\qquad
x(t)=u(t).
$$

Transform each term while retaining the initial conditions:

$$
[s^2Y(s)-s]+3[sY(s)-1]+2Y(s)=\frac{1}{s}.
$$

Collect the terms containing $Y(s)$:

$$
(s^2+3s+2)Y(s)=s+3+\frac{1}{s}.
$$

Therefore,

$$
Y(s)=\frac{s^2+3s+1}{s(s+1)(s+2)}.
$$

Partial fractions give

$$
Y(s)=\frac{1/2}{s}+\frac{1}{s+1}-\frac{1/2}{s+2}.
$$

Hence,

$$
y(t)=\left(\frac12+e^{-t}-\frac12e^{-2t}\right)u(t).
$$

This is the total response because the transformed equation retained both the applied input and the nonzero initial condition.

## Inverse Laplace transform: predict before calculating

The inverse Laplace transform converts $X(s)$ back to $x(t)$. For rational transforms, partial fractions expose the standard transform pairs.

Use this sequence:

1. Simplify the expression and factor the denominator.
2. Locate and classify the poles.
3. Predict the required time-domain form.
4. Write the correct partial-fraction structure.
5. Find the coefficients.
6. Interpret and check the result.

The pole pattern should predict the response form before the coefficient algebra begins.

## Pole patterns and required response forms

| Pole pattern | Required partial-fraction terms | Time-domain form |
|---|---|---|
| distinct real $p_1,p_2$ | $A/(s-p_1)+B/(s-p_2)$ | $Ae^{p_1t}+Be^{p_2t}$ |
| repeated $p$, multiplicity $m$ | $A_1/(s-p)+\cdots+A_m/(s-p)^m$ | $(C_0+C_1t+\cdots+C_{m-1}t^{m-1})e^{pt}$ |
| complex pair $\sigma\pm j\omega$ | numerator over $(s-\sigma)^2+\omega^2$ | $e^{\sigma t}[C_1\cos(\omega t)+C_2\sin(\omega t)]$ |

Poles determine the available modes. Partial-fraction coefficients determine their weights. Zeros can change a coefficient or cancel a pole, but zeros do not create independent modes.

## Case 1: distinct real poles

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

The pole at $-1$ produces the slower mode, so it dominates the late-time transient. As a check, $y(0^+)=2$, which agrees with $\lim_{s\to\infty}sY(s)=2$.

## Case 2: a repeated pole

Consider

$$
Y(s)=\frac{1}{(s+1)(s+2)^2}.
$$

The repeated pole at $-2$ requires both first- and second-power terms:

$$
Y(s)=\frac{A}{s+1}+\frac{B}{s+2}+\frac{C}{(s+2)^2}.
$$

Solving for the coefficients gives

$$
Y(s)=\frac{1}{s+1}-\frac{1}{s+2}-\frac{1}{(s+2)^2}.
$$

Thus,

$$
y(t)=\left(e^{-t}-e^{-2t}-te^{-2t}\right)u(t).
$$

The repeated pole adds the factor $t$. It does not create oscillation.

## Case 3: complex-conjugate poles

Consider

$$
Y(s)=\frac{2s+10}{s^2+4s+13}.
$$

Complete the square:

$$
s^2+4s+13=(s+2)^2+9.
$$

Rewrite the numerator to match the cosine and sine pairs:

$$
2s+10=2(s+2)+6.
$$

Therefore,

$$
Y(s)=
2\frac{s+2}{(s+2)^2+9}
+2\frac{3}{(s+2)^2+9}.
$$

The inverse transform is

$$
y(t)=2e^{-2t}[\cos(3t)+\sin(3t)]u(t).
$$

The poles are $-2\pm j3$. The real part $-2$ sets the decaying envelope, and the imaginary part $3$ sets the oscillation frequency in rad/s.

## What the poles tell you before algebra

For a causal rational response, a pole $p$ produces a mode based on $e^{pt}$.

| Pole location | Qualitative behavior |
|---|---|
| negative real | decaying exponential |
| positive real | growing exponential |
| repeated real | exponential multiplied by powers of $t$ |
| $\sigma\pm j\omega$, $\sigma<0$ | decaying oscillation |
| $\sigma\pm j\omega$, $\sigma>0$ | growing oscillation |
| $\pm j\omega$ | sustained oscillation |

Among stable modes, the pole closest to the imaginary axis usually decays most slowly and dominates the late-time response. A cancellation or a very small coefficient can weaken that mode, so the full expression still matters.

For system stability and additional pole interpretation, continue to [Module 5: Poles and time-domain responses](05_poles_and_responses.md).

## Properness and polynomial terms

Partial fractions apply directly when the rational function is proper:

$$
\deg N(s)<\deg D(s).
$$

If the numerator degree is greater than or equal to the denominator degree, perform polynomial division first. The polynomial part corresponds to impulses or derivatives of impulses. Many introductory exercises use strictly proper rational functions so that the inverse consists only of ordinary causal functions.

## Initial- and final-value checks

### Initial-value theorem

If the signal has no impulse at $t=0$,

$$
x(0^+)=\lim_{s\to\infty}sX(s).
$$

For the distinct-pole example,

$$
\lim_{s\to\infty}s\frac{2s+7}{(s+1)(s+3)}=2.
$$

The time-domain result gives the same value:

$$
y(0^+)=\frac52-\frac12=2.
$$

### Final-value theorem

The final-value theorem is

$$
\lim_{t\to\infty}x(t)=\lim_{s\to0}sX(s),
$$

but only when every pole of $sX(s)$ lies strictly in the open left half-plane.

For

$$
X(s)=\frac{4}{s(s+4)},
$$

the only pole of $sX(s)=4/(s+4)$ is at $-4$, so

$$
x(\infty)=\lim_{s\to0}\frac{4}{s+4}=1.
$$

Do not use the theorem for

$$
X(s)=\frac{1}{s^2+1}.
$$

The poles at $\pm j$ produce a sustained sinusoid, so no final value exists.

The initial- and final-value theorems check a result. They do not replace factoring the denominator and examining the poles.

## A reliable problem-solving workflow

### Direct transform

1. Identify standard signal components.
2. Apply linearity and the relevant shift or scaling property.
3. Simplify only after the transform structure is clear.
4. Inspect the poles and zeros for a qualitative check.

### Differential equation

1. Transform every derivative and retain the initial conditions.
2. Collect all terms containing the output transform.
3. Solve algebraically for the output transform.
4. Factor the denominator and predict the response form.
5. Use partial fractions and transform pairs.
6. Check initial and final values when the theorem conditions hold.

### Inverse transform

1. Check whether the rational function is proper.
2. Factor and classify the poles.
3. Write the required time-domain form before solving coefficients.
4. Use cover-up for distinct poles and coefficient matching for the remaining terms.
5. Interpret decay, growth, oscillation, and the dominant mode.

## Common mistakes

- Dropping $x(0^-)$ or $x'(0^-)$ from derivative transforms.
- Treating $H(s)X(s)$ as the total response when initial conditions are nonzero.
- Starting coefficient algebra before predicting the response form.
- Writing only one term for a repeated pole.
- Forgetting to complete the square for a complex-conjugate pole pair.
- Treating a zero as though it creates a time-domain mode.
- Applying the final-value theorem without checking the poles of $sX(s)$.
- Interpreting an imaginary part in hertz instead of rad/s.
- Mistaking the delay factor $e^{-sT}$ for an exponential time-domain mode.

## Practice

1. Find the transform of $4e^{-3t}u(t)-2u(t)$.
2. Use a property to find the transform of $(t-2)u(t-2)$.
3. Predict the inverse-transform form of $1/[(s+1)^2(s+4)]$ before finding any coefficients.
4. Find the inverse transform of $(s+4)/[(s+2)^2+4]$.
5. Solve $y'+2y=u(t)$ for $y(0^-)=3$ using the unilateral Laplace transform.
6. Can the final-value theorem be used for $X(s)=1/(s^2+4)$? Explain using its poles.

<details><summary>Answers</summary>

1. $X(s)=4/(s+3)-2/s$.
2. $X(s)=e^{-2s}/s^2$.
3. $(C_1e^{-t}+C_2te^{-t}+C_3e^{-4t})u(t)$.
4. Write $s+4=(s+2)+2$ to obtain $e^{-2t}[\cos(2t)+\sin(2t)]u(t)$.
5. $Y(s)=(3s+1)/[s(s+2)]=\frac{1/2}{s}+\frac{5/2}{s+2}$, so $y(t)=[1/2+(5/2)e^{-2t}]u(t)$.
6. No. The poles at $\pm j2$ remain on the imaginary axis, so the time-domain signal does not approach a constant.

</details>

## Further study

- B. P. Lathi and Roger Green, *Linear Systems and Signals*, Chapter 4.
- [MIT OpenCourseWare, 6.003 Signals and Systems, Lecture 6: Laplace Transform](https://live.ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/pages/lecture-notes/)
- [MIT OpenCourseWare, RES.6-007 Signals and Systems, Laplace-transform readings](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/pages/readings/)
- [University of Waterloo, Laplace-transform properties and examples](https://ece.uwaterloo.ca/~dwharder/Maple/laplace_transform/)

