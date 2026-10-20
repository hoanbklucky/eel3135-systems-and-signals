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

## Concept checks

1. At what time does $u(3t-6)$ turn on?
2. Does $x(-2t)$ include reversal, compression, or both?
3. Write a rectangular pulse that is one from $t=1$ through $t=4$.

<details><summary>Answers</summary>

1. $t=2$.
2. Reversal and compression by 2.
3. $u(t-1)-u(t-4)$.

</details>

