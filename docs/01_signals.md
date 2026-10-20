# 1. Signals and operations

## Learning goals

After this module, you should be able to classify a signal and interpret time shifting, time scaling, reversal, and amplitude scaling.

## Start with meaning

A continuous-time signal assigns a value to every time $t$. Before manipulating a formula, ask:

- What physical quantity does the vertical axis represent?
- What are the units of time?
- At what times can the signal be nonzero?
- Is the signal bounded, periodic, or finite-energy?

## Elementary signals

The unit step is

$$
u(t)=\begin{cases}0,&t<0\\1,&t>0.\end{cases}
$$

A delayed step $u(t-t_0)$ turns on at $t=t_0$.

The impulse $\delta(t)$ is defined by its sampling property:

$$
\int_{-\infty}^{\infty}x(t)\delta(t-t_0)\,dt=x(t_0).
$$

## Time transformations

For $x(at-b)$, find the important time by solving $at-b=0$. Then determine whether the signal is compressed, expanded, or reversed.

Example:

$$
y(t)=x(2t-4)=x\bigl(2(t-2)\bigr).
$$

The factor 2 compresses the signal by 2, and the feature originally at zero appears at $t=2$.

## A dependable method for time transformations

For $y(t)=x(at-b)$, rewrite the argument as

$$
at-b=a\left(t-\frac{b}{a}\right).
$$

Then work from the inside out:

1. the feature that occurred at $t=0$ in $x(t)$ moves to $t=b/a$;
2. $|a|>1$ compresses time and $0<|a|<1$ expands time;
3. $a<0$ also reverses time.

Do not interpret $x(2t-4)$ as a shift by 4. The zero of the argument is at $t=2$.

### Worked example: transforming a pulse

Let

$$
x(t)=u(t)-u(t-2),
$$

which is one on $0\le t<2$. Find where $y(t)=x(3-2t)$ is nonzero.

The original pulse is active when its argument lies between 0 and 2:

$$
0\le 3-2t<2.
$$

Solving both inequalities gives

$$
\frac{1}{2}<t\le\frac{3}{2}.
$$

The negative coefficient reverses the pulse, and its magnitude 2 compresses its duration from 2 seconds to 1 second.

## Even and odd decomposition

Every signal can be written as the sum of an even and an odd part:

$$
x(t)=x_e(t)+x_o(t),
$$

where

$$
x_e(t)=\frac{x(t)+x(-t)}{2},\qquad
x_o(t)=\frac{x(t)-x(-t)}{2}.
$$

This decomposition becomes useful in Fourier analysis because even signals contribute cosine-like components and odd signals contribute sine-like components.

## Energy, power, and periodicity

Signal energy is

$$
E=\int_{-\infty}^{\infty}|x(t)|^2dt.
$$

Average power is

$$
P=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}|x(t)|^2dt.
$$

A nonzero finite-duration pulse usually has finite energy and zero average power. A nonzero periodic signal usually has infinite energy but finite average power.

For a continuous-time sinusoid $\cos(\omega_0t+\phi)$,

$$
T_0=\frac{2\pi}{|\omega_0|}.
$$

For a sum of sinusoids to be periodic, their frequency ratios must be rational.

## Common mistakes

- Moving a signal in the wrong direction: $x(t-t_0)$ is delayed, not advanced.
- Applying amplitude intuition to time scaling: $x(2t)$ changes duration, not height.
- Treating $u(0)$ as important in ordinary waveform calculations. A value at one isolated time does not change an integral.
- Confusing $\delta(t)$ with a very tall ordinary pulse. The impulse is a distribution defined through integration.

## Concept checks

1. At what time does $u(3t-6)$ turn on?
2. Does $x(-2t)$ include reversal, compression, or both?
3. Write a rectangular pulse that is one from $t=1$ through $t=4$.
4. Find the period of $3\cos(4t-1)$.
5. Is $e^{-2t}u(t)$ an energy signal or a power signal?
6. Find the even part of $x(t)=1+t$.

<details><summary>Answers</summary>

1. $t=2$.
2. Reversal and compression by 2.
3. $u(t-1)-u(t-4)$.
4. $T_0=\pi/2$.
5. It is an energy signal: $E=\int_0^\infty e^{-4t}dt=1/4$.
6. $x_e(t)=[(1+t)+(1-t)]/2=1$.

</details>

