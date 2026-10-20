# 10. Cumulative problem-solving guide

This module is a decision guide for problems that combine several course ideas. The goal is not to memorize one procedure, but to choose a representation that exposes the requested information.

## Start by classifying the question

| If the question asks for… | Start with… |
|---|---|
| linearity, time invariance, causality | the system definition or $h(t)$ |
| zero-state output in time | convolution or $H(s)X(s)$ |
| response with initial conditions | the unilateral Laplace transform |
| qualitative decay or oscillation | poles |
| sinusoidal steady state | $H(j\omega)$ |
| spectral content | Fourier series or Fourier transform |
| safe sampling rate | bandwidth and spectral replicas |

## Universal prediction checklist

Before calculation, write down:

1. **Support:** when can the response be nonzero?
2. **Modes:** which poles can create terms in the response?
3. **Behavior:** should the response grow, decay, oscillate, or approach a constant?
4. **Initial value:** what should happen at $t=0^+$?
5. **Final behavior:** does a final value exist?
6. **Units:** are the result and independent variable expressed consistently?

These predictions make algebraic errors easier to detect.

## End-to-end example

Consider the causal LTI system

$$
H(s)=\frac{2}{(s+1)(s+3)}
$$

driven from zero state by

$$
x(t)=4u(t),\qquad X(s)=\frac4s.
$$

### 1. Predict the response form

The input pole at zero permits a constant. The system poles at $-1$ and $-3$ permit two decaying exponentials:

$$
y(t)=C_0+C_1e^{-t}+C_2e^{-3t}.
$$

The system is stable because its poles are in the open left half-plane.

### 2. Form the zero-state transform

$$
Y(s)=H(s)X(s)=\frac{8}{s(s+1)(s+3)}.
$$

### 3. Calculate the coefficients

$$
Y(s)=\frac{8/3}{s}-\frac{4}{s+1}+\frac{4/3}{s+3}.
$$

Therefore

$$
y(t)=\left(\frac83-4e^{-t}+\frac43e^{-3t}\right)u(t).
$$

### 4. Interpret and check

- Initial value: $8/3-4+4/3=0$, as expected for this strictly proper zero-state system.
- Final value: $8/3$.
- DC-gain check: $H(0)=2/3$, so a step of height 4 produces $4H(0)=8/3$.
- Dominant pole: $-1$, so the $e^{-t}$ term governs the late transient.

One solution has now connected input poles, system poles, stability, partial fractions, initial value, final value, and DC gain.

## When initial conditions are nonzero

Do not use $Y=HX$ as the total response. Choose one of two valid routes:

### Route A: transform the differential equation once

Retain every initial-condition term. The resulting $Y(s)$ is the total response.

### Route B: use superposition

1. Set the input to zero and calculate $Y_{zi}(s)$.
2. Set initial conditions to zero and calculate $Y_{zs}(s)=H(s)X(s)$.
3. Add the two contributions.

Route B is often more instructive because it shows which physical cause produces each contribution.

## Choosing between Laplace and Fourier methods

Use Laplace methods when initial conditions, transients, differential equations, and pole locations matter. Use Fourier methods when the main question concerns frequency content, bandwidth, filtering, or sinusoidal steady state.

For a stable system, the frequency response can be obtained from the transfer function:

$$
H(j\omega)=H(s)|_{s=j\omega}.
$$

The two methods are related, but they answer different questions efficiently.

## Exam-quality solution template

A clear solution normally includes:

1. the governing relation;
2. the predicted response form or qualitative behavior;
3. the essential algebra;
4. the final answer with $u(t)$ when causality needs to be explicit;
5. one physical or mathematical check.

Avoid presenting only a final expression. A correct expression with no interpretation does not demonstrate that you understand the system.

## Cumulative practice

### Problem 1: response modes

For

$$
H(s)=\frac{s+4}{(s+2)[(s+1)^2+9]},\qquad X(s)=\frac{5}{s},
$$

predict the form of the causal zero-state response without calculating coefficients.

### Problem 2: stability and sinusoidal response

A system has

$$
H(s)=\frac{10}{(s+2)(s+5)}.
$$

Is it BIBO stable? Write the expression needed to find the steady-state output for $x(t)=3\cos(4t)$.

### Problem 3: sampling

A sensor signal is bandlimited to 2.5 kHz, but a practical anti-alias filter needs a 1 kHz transition band. Suggest a reasonable minimum sampling rate and justify it.

<details><summary>Solutions</summary>

### Problem 1

The input pole at zero supplies a constant. The real system pole at $-2$ supplies $e^{-2t}$. The complex pair $-1\pm j3$ supplies a damped sinusoid:

$$
y_{zs}(t)=C_0+C_1e^{-2t}+e^{-t}[C_2\cos(3t)+C_3\sin(3t)].
$$

### Problem 2

The system is stable because both poles are negative. Evaluate

$$
H(j4)=\frac{10}{(j4+2)(j4+5)}.
$$

Then

$$
y_{ss}(t)=3|H(j4)|\cos[4t+\angle H(j4)].
$$

### Problem 3

The theoretical Nyquist boundary is 5 kHz, but this leaves no transition band. A sampling rate of at least 7 kHz lets an anti-alias filter transition from 2.5 kHz to the Nyquist frequency at 3.5 kHz. A standard rate above that value may be preferable in implementation.

</details>
