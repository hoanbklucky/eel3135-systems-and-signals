# 3. Impulse response and convolution

## Central idea

An LTI system is completely characterized by its impulse response $h(t)$. The zero-state output is

$$
y(t)=x(t)*h(t)=\int_{-\infty}^{\infty}x(\tau)h(t-\tau)\,d\tau.
$$

## Why convolution appears

Represent the input as a continuum of shifted impulses:

$$
x(t)=\int_{-\infty}^{\infty}x(\tau)\delta(t-\tau)\,d\tau.
$$

The response to $\delta(t-\tau)$ is $h(t-\tau)$. Linearity weights that response by $x(\tau)$, and integration adds all delayed responses.

## Graphical procedure

To compute $x(t)*h(t)$:

1. rename the independent variable in one signal to $\tau$;
2. reverse and shift the other signal to form $h(t-\tau)$;
3. identify the overlap interval;
4. multiply and integrate over the overlap;
5. repeat when the overlap pattern changes.

The breakpoints come from changes in overlap, not from memorized formulas.

## Useful checks

- Convolution is commutative: $x*h=h*x$.
- If $x(t)=\delta(t)$, then $y(t)=h(t)$.
- For causal signals, the convolution integral reduces to the interval where both signals are active.

