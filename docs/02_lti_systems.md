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

## How to test a system systematically

### Linearity: use the superposition test

Compute both

$$
T\{a x_1+b x_2\}
\quad\text{and}\quad
aT\{x_1\}+bT\{x_2\}.
$$

The system is linear only if they agree for every input and every scalar $a,b$.

Example: $T\{x(t)\}=t\,x(t)$ is linear because multiplication by the known function $t$ distributes over sums and scalar multiples. It is not time invariant, because the coefficient multiplying the input depends on the absolute clock time.

### Time invariance: compare two experiments

Let $y_1(t)=T\{x(t)\}$. Then apply the shifted input:

$$
y_2(t)=T\{x(t-t_0)\}.
$$

The system is time invariant if $y_2(t)=y_1(t-t_0)$ for every $x$ and $t_0$.

Example: $y(t)=x(2t)$ is not time invariant:

$$
T\{x(t-t_0)\}=x(2t-t_0),
$$

but shifting the original output gives $x(2t-2t_0)$.

## Why the impulse response characterizes an LTI system

Any input can be decomposed into shifted impulses:

$$
x(t)=\int_{-\infty}^{\infty}x(\tau)\delta(t-\tau)d\tau.
$$

An LTI system responds to $\delta(t-\tau)$ with $h(t-\tau)$. Linearity then gives

$$
y(t)=\int_{-\infty}^{\infty}x(\tau)h(t-\tau)d\tau.
$$

This is why knowing $h(t)$ is equivalent to knowing the zero-state input-output behavior of the system.

## Memory and invertibility

- An LTI system is memoryless only when $h(t)=K\delta(t)$.
- A system with impulse response $h(t)$ has an LTI inverse if another impulse response $h^{-1}(t)$ satisfies

$$
h(t)*h^{-1}(t)=\delta(t).
$$

An algebraic inverse may be noncausal or unstable, so invertibility does not automatically mean practical realizability.

## Worked classification example

Consider

$$
y(t)=\int_{t-1}^{t}x(\tau)d\tau.
$$

- It is linear because integration is linear.
- It is time invariant because the one-second integration window shifts with the input.
- It is causal because only values $\tau\le t$ are used.
- It is BIBO stable: if $|x(t)|\le M$, then $|y(t)|\le M$.
- Its impulse response is $h(t)=u(t)-u(t-1)$.

## Common mistakes

- Assuming multiplication by $t$ is nonlinear. It is linear but time varying.
- Checking only additivity and forgetting homogeneity.
- Calling a system stable because one chosen input produces a bounded output.
- Confusing causality with “no delay.” A causal system may contain delay; it simply cannot depend on future input.

## Concept checks

1. Is $y(t)=3x(t)+2$ linear?
2. Is $y(t)=x(t-2)$ time invariant?
3. Is $h(t)=e^t u(t)$ causal? Is it BIBO stable?
4. Classify $y(t)=x(t)^2$ for linearity.
5. Is $y(t)=x(t+1)$ causal?
6. Is $h(t)=e^{-3t}u(t)$ BIBO stable?

<details><summary>Answers</summary>

1. No. Zero input produces output 2.
2. Yes.
3. It is causal but not BIBO stable.
4. Nonlinear.
5. No. It depends on a future input value.
6. Yes, because $\int_0^\infty e^{-3t}dt=1/3$.

</details>

