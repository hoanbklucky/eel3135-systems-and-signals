# 2. Systems and LTI properties

## Learning goals

You should be able to test linearity and time invariance, then connect causality and BIBO stability to the impulse response.

## Linearity

A system $T\{\cdot\}$ is linear when

$$
T\{a x_1(t)+b x_2(t)\}=aT\{x_1(t)\}+bT\{x_2(t)\}.
$$

Test the complete expression. A constant added independently of the input usually breaks linearity.

## Time invariance

If $x(t)\mapsto y(t)$, a time-invariant system must satisfy

$$
x(t-t_0)\mapsto y(t-t_0).
$$

The system cannot react differently merely because the same experiment starts later.

## Causality and stability

For a continuous-time LTI system:

- causality requires $h(t)=0$ for $t<0$;
- BIBO stability requires $\int_{-\infty}^{\infty}|h(t)|dt<\infty$.

These statements describe different properties. A causal system need not be stable.

## Concept checks

1. Is $y(t)=3x(t)+2$ linear?
2. Is $y(t)=x(t-2)$ time invariant?
3. Is $h(t)=e^t u(t)$ causal? Is it BIBO stable?

<details><summary>Answers</summary>

1. No. Zero input produces output 2.
2. Yes.
3. It is causal but not BIBO stable.

</details>

