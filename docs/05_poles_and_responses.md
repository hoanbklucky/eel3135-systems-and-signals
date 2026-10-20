# 5. Poles and time-domain responses

## Read the poles before doing algebra

For a causal rational response, a pole $p$ contributes a mode proportional to $e^{pt}$.

| Pole pattern | Time-domain behavior |
|---|---|
| negative real pole | decaying exponential |
| positive real pole | growing exponential |
| repeated real pole | exponential multiplied by powers of $t$ |
| $\sigma\pm j\omega$ | oscillation at $\omega$ inside an $e^{\sigma t}$ envelope |

For example, poles at $-2\pm j5$ allow the form

$$
y(t)=e^{-2t}[C_1\cos(5t)+C_2\sin(5t)]u(t).
$$

The real part $-2$ determines decay. The imaginary part 5 determines angular frequency.

## System poles and input poles

When

$$
Y(s)=H(s)X(s),
$$
the poles of $H(s)$ supply system modes and the poles of $X(s)$ supply forced-response modes. Cancellations may remove a mode, so inspect the simplified product.

## Stability

For a causal rational LTI system, BIBO stability requires every pole of $H(s)$ to lie strictly in the open left half-plane.

Do not infer stability merely because one particular response looks bounded. Stability is a system property.

## From a denominator to a waveform

Given a second-order denominator

$$
D(s)=s^2+2\alpha s+(\alpha^2+\omega_d^2),
$$

the poles are $-\alpha\pm j\omega_d$. The corresponding natural response has the form

$$
y_n(t)=e^{-\alpha t}[C_1\cos(\omega_dt)+C_2\sin(\omega_dt)].
$$

- $\alpha$ controls the exponential envelope.
- $\omega_d$ controls how rapidly the waveform oscillates.
- $C_1$ and $C_2$ depend on initial conditions and excitation; they do not move the poles.

The approximate settling time associated with a dominant real part $-\alpha$ is often estimated as

$$
T_s\approx\frac{4}{\alpha}
$$

for a 2% criterion.

## Pole patterns for a standard second-order system

For

$$
H(s)=\frac{\omega_n^2}{s^2+2\zeta\omega_n s+\omega_n^2},
$$

the damping ratio $\zeta$ describes the pole pattern:

| Damping | Poles | Qualitative response |
|---|---|---|
| $\zeta>1$ | distinct negative real | overdamped, no oscillation |
| $\zeta=1$ | repeated negative real | critically damped |
| $0<\zeta<1$ | complex with negative real part | underdamped, decaying oscillation |
| $\zeta=0$ | imaginary-axis pair | sustained oscillation |
| $\zeta<0$ | right-half-plane real part | growing, unstable response |

## Worked comparison

Compare three denominators:

1. $(s+1)(s+4)$: modes $e^{-t}$ and $e^{-4t}$. The $-1$ pole is dominant because it decays more slowly.
2. $(s+2)^2$: modes $e^{-2t}$ and $te^{-2t}$. The repeated pole introduces a polynomial factor.
3. $(s+2)^2+25$: modes $e^{-2t}\cos(5t)$ and $e^{-2t}\sin(5t)$. The envelope decays as $e^{-2t}$ while the oscillation frequency is 5 rad/s.

The pole locations let you sketch these behaviors before any partial-fraction calculation.

## What zeros do

Zeros do not create independent modes, but they shape the coefficients and can cancel poles. For example,

$$
H(s)=\frac{s+2}{(s+2)(s+5)}=\frac{1}{s+5}
$$

has only the $-5$ mode after cancellation. In physical models, an exact cancellation may be fragile because component values and models are never exact.

A zero can also suppress a response at a particular frequency. If $H(j\omega_0)=0$, a sinusoid at $\omega_0$ produces zero steady-state output.

## Dominant poles

Among stable poles, the poles closest to the imaginary axis decay most slowly and usually dominate late-time behavior. This is an approximation, not a guarantee: a nearby zero or a very small coefficient can weaken a nominally dominant mode.

## Common mistakes

- Calling complex poles unstable merely because they are complex. Their real parts determine growth or decay.
- Reading $5$ in $-2\pm j5$ as hertz. It is angular frequency in rad/s; $f=5/(2\pi)$ Hz.
- Inferring BIBO stability from the poles of a particular $Y(s)$ rather than from $H(s)$.
- Ignoring cancellations before listing the response modes.

## Practice

1. Predict the natural-response form for poles at $-1$, $-3$, and $-3$.
2. Which pole dominates: $-0.5$ or $-8$?
3. What behavior is produced by poles at $1\pm j4$?

<details><summary>Answers</summary>

1. $C_1e^{-t}+C_2e^{-3t}+C_3te^{-3t}$.
2. $-0.5$, because it decays more slowly.
3. An oscillation at 4 rad/s inside a growing $e^t$ envelope; the system is unstable if these are poles of $H(s)$.

</details>

