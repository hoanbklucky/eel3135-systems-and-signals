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

## Finding the integration limits

For causal $x(t)$ and $h(t)$,

$$
y(t)=\int_0^t x(\tau)h(t-\tau)d\tau,
$$

but only when both signals truly begin at zero and have unlimited support afterward. For finite-duration signals, determine the intersection of their support intervals.

If $x(\tau)$ is nonzero on $[a,b]$ and $h(t-\tau)$ is nonzero when $\tau\in[t-d,t-c]$, then integrate over

$$
[a,b]\cap[t-d,t-c].
$$

The formula changes when the endpoints of that intersection change order.

## Worked example: two rectangular pulses

Let


$$
x(t)=u(t)-u(t-2),\qquad h(t)=u(t)-u(t-1).
$$

$x(\tau)$ is active on $0\le\tau<2$, while $h(t-\tau)$ is active on $t-1<\tau\le t$. The convolution equals the length of the overlap:

$$
y(t)=
\begin{cases}
0, & t<0,\\
t, & 0\le t<1,\\
1, & 1\le t<2,\\
3-t, & 2\le t<3,\\
0, & t\ge3.
\end{cases}
$$

Interpretation: the output rises while the shorter pulse increasingly overlaps the longer one, stays flat during full overlap, and falls as the overlap disappears.

## Worked example: step response from impulse response

If

$$
h(t)=e^{-2t}u(t),\qquad x(t)=u(t),
$$

then

$$
y(t)=\int_0^t e^{-2(t-\tau)}d\tau
=\frac{1-e^{-2t}}{2}u(t).
$$

The output begins at zero and approaches $1/2$. The number $1/2$ is also the area under $h(t)$, which equals the DC gain of this stable system.

## Properties that save work

$$
x*h=h*x,
$$

$$
x*(h_1+h_2)=x*h_1+x*h_2,
$$

$$
(x*h_1)*h_2=x*(h_1*h_2).
$$

The last property explains cascaded LTI systems: the overall impulse response is the convolution of the component impulse responses.

## Common mistakes

- Reversing $h(\tau)$ but forgetting to shift it to $h(t-\tau)$.
- Using the same limits for every $t$ even though the overlap changes.
- Convolving for the total response when nonzero initial conditions are present. Convolution with $h(t)$ gives the zero-state response.
- Losing units: if $h(t)$ has units of inverse time, integration restores the output units.

## Practice

1. Compute $u(t)*e^{-t}u(t)$.
2. What is $x(t)*\delta(t-3)$?
3. Two causal pulses have durations 2 s and 5 s. Over what total duration can their convolution be nonzero?

<details><summary>Answers</summary>

1. $(1-e^{-t})u(t)$.
2. $x(t-3)$.
3. From first contact until last contact: $2+5=7$ seconds.

</details>

