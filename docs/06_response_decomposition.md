# 6. Zero-input, zero-state, and total response

## One response, three different questions

Several common terms describe a system response, but they do not all describe the same split.

| Decomposition | Question answered | Components |
|---|---|---|
| by cause | What produced the response? | zero-input response + zero-state response |
| by differential equation | Which part follows the homogeneous equation, and which part is a particular solution? | natural response + forced response |
| by long-term behavior | Which terms vanish, and which terms remain? | transient response + steady-state response |

```mermaid
flowchart TD
    T[Total response y(t)]
    T --> C[Decomposition by cause]
    C --> ZI[Zero-input response]
    C --> ZS[Zero-state response]
    T --> E[Decomposition by equation]
    E --> N[Natural response]
    E --> F[Forced response]
    T --> L[Decomposition by long-term behavior]
    L --> TR[Transient response]
    L --> SS[Steady-state response]
```

These are three independent ways to describe the same total response. The terms across different rows are generally not interchangeable.

## Decomposition by cause

For a linear system,

$$
y(t)=y_{zi}(t)+y_{zs}(t).
$$

- The **zero-input response** comes from initial stored energy. Set the applied input to zero and keep the initial conditions.
- The **zero-state response** comes from the applied input. Set every initial condition to zero and keep the input.

This decomposition describes two conceptual experiments. It does not classify terms by whether they decay or remain.

## Decomposition by differential equation

For a linear differential equation, the total solution can also be written as

$$
y(t)=y_n(t)+y_f(t).
$$

- The **natural response** is the homogeneous-solution part. Its modes come from the system's characteristic roots, or equivalently its poles.
- The **forced response** is a particular solution associated with the applied input.

The natural response is not automatically equal to the zero-input response. Turning on an input while the system starts from rest can require system-pole terms in the zero-state response so that the initial conditions remain zero.

Terminology varies across textbooks. Some authors use *natural response* as another name for the zero-input response. This module uses *natural response* for the homogeneous component of the complete solution, which makes the three decompositions distinct. When reading another source, check how it defines the term.

## Decomposition by long-term behavior

When a meaningful steady state exists,

$$
y(t)=y_{tr}(t)+y_{ss}(t).
$$

- The **transient response** contains terms that approach zero as $t\to\infty$.
- The **steady-state response** is the part that remains after the transient terms vanish.

A steady-state response does not have to be constant. It may be sinusoidal or periodic. A forced term can also be transient when the input itself decays.

## One example classified three ways

Consider the first-order system

$$
y'(t)+2y(t)=2u(t),
\qquad y(0^-)=3.
$$

The following expressions describe the response for $t\ge0$.

### By cause

Set the input to zero and retain the initial condition:

$$
y_{zi}(t)=3e^{-2t}.
$$

Set the initial condition to zero and retain the step input:

$$
y_{zs}(t)=1-e^{-2t}.
$$

Therefore,

$$
y(t)=y_{zi}(t)+y_{zs}(t)
=1+2e^{-2t}.
$$

### By differential equation

The homogeneous equation $y'+2y=0$ supplies the natural mode $e^{-2t}$. A constant particular solution supplies the forced term. For the complete response,

$$
y_n(t)=2e^{-2t},
\qquad
y_f(t)=1.
$$

Notice that $y_n(t)\ne y_{zi}(t)$. The zero-state response contains the additional natural-form term $-e^{-2t}$ needed to satisfy its zero initial condition.

### By long-term behavior

Because $e^{-2t}\to0$,

$$
y_{tr}(t)=2e^{-2t},
\qquad
y_{ss}(t)=1.
$$

The same response can therefore be summarized as

| Classification | First component | Second component |
|---|---|---|
| by cause | $y_{zi}=3e^{-2t}$ | $y_{zs}=1-e^{-2t}$ |
| by equation | $y_n=2e^{-2t}$ | $y_f=1$ |
| by long-term behavior | $y_{tr}=2e^{-2t}$ | $y_{ss}=1$ |

This example shows why the labels cannot be substituted for one another.

## RLC example

Let

$$
D(s)=s^2+2s+5,
$$

with $i(0^-)=2$, $v_C(0^-)=10$, and applied voltage $10u(t)$, so $V(s)=10/s$.

The transformed circuit equation can be organized by physical cause:

$$
D(s)I(s)=\underbrace{s i(0^-)-v_C(0^-)}_{\text{initial energy}}+\underbrace{sV(s)}_{\text{applied input}}.
$$

### Zero-input response

Set $V(s)=0$:

$$
I_{zi}(s)=\frac{2s-10}{D(s)}.
$$

### Zero-state response

Set the initial conditions to zero:

$$
I_{zs}(s)=\frac{s(10/s)}{D(s)}=\frac{10}{D(s)}.
$$

### Total response

Add the independently calculated contributions:

$$
I(s)=I_{zi}(s)+I_{zs}(s)
=\frac{(2s-10)+10}{D(s)}
=\frac{2s}{D(s)}.
$$

The $-10$ and $+10$ are not an arbitrary algebraic split. They come from different physical causes and happen to cancel for these values.

## Why superposition allows the split

For a linear differential equation, the solution produced by two independent causes equals the sum of the solutions produced by each cause separately. Here the causes are:

1. stored energy represented by the initial conditions;
2. the external input applied for $t\ge0$.

Thus we perform two physically meaningful experiments:

| Experiment | Initial conditions | Applied input | Result |
|---|---|---|---|
| Zero input | retained | set to zero | $y_{zi}(t)$ |
| Zero state | set to zero | retained | $y_{zs}(t)$ |

Adding the two results reconstructs the actual experiment.

## Finish the RLC inverse transforms

Since

$$
D(s)=(s+1)^2+4,
$$

rewrite the zero-input numerator:

$$
2s-10=2(s+1)-12.
$$

Therefore

$$
i_{zi}(t)=e^{-t}[2\cos(2t)-6\sin(2t)]u(t).
$$

For the zero-state response,

$$
I_{zs}(s)=\frac{10}{(s+1)^2+4},
$$

so

$$
i_{zs}(t)=5e^{-t}\sin(2t)u(t).
$$

The total response is

$$
i(t)=e^{-t}[2\cos(2t)-\sin(2t)]u(t).
$$

Check the initial current:

$$
i(0^+)=2+0=2\text{ A}.
$$

Both contributions contain the system modes $-1\pm j2$. The initial conditions and input determine their different weights.

## Transfer function and zero-state response

The transfer function is defined with zero initial conditions:

$$
H(s)=\left.\frac{Y(s)}{X(s)}\right|_{\text{zero initial conditions}}.
$$

Therefore

$$
Y_{zs}(s)=H(s)X(s).
$$

This equation does **not** include the zero-input response. If initial energy is present, calculate $Y_{zi}(s)$ separately or transform the differential equation while retaining its initial-condition terms.

## System poles versus input poles in the ZSR

Suppose

$$
H(s)=\frac{s+1}{(s+2)(s+3)},\qquad X(s)=\frac{3}{s+5}.
$$

Then

$$
Y_{zs}(s)=\frac{3(s+1)}{(s+5)(s+2)(s+3)}.
$$

Before calculating coefficients, predict

$$
y_{zs}(t)=C_1e^{-5t}+C_2e^{-2t}+C_3e^{-3t}.
$$

The $-5$ input pole supplies the forced-response mode; the $-2$ and $-3$ system poles supply transient modes. Partial fractions determine how strongly each appears.

For this example,

$$
Y_{zs}(s)=-\frac{2}{s+5}-\frac{1}{s+2}+\frac{3}{s+3},
$$

so

$$
y_{zs}(t)=(-2e^{-5t}-e^{-2t}+3e^{-3t})u(t).
$$

The coefficients sum to zero, consistent with $y_{zs}(0^+)=0$ for this strictly proper system.

## Important qualifications

- A natural response is transient only when its modes decay. An unstable natural response grows instead of disappearing.
- A forced response can be transient. For example, an input $e^{-5t}u(t)$ can produce a forced term proportional to $e^{-5t}$ that eventually vanishes.
- A zero-state response can contain system-pole modes as well as an input-related mode.
- A zero-input response can contain every system mode excited by the initial conditions.
- A steady-state response may be constant, sinusoidal, or periodic. Some responses never approach a steady state.
- The labels depend on the question being asked. Always state which decomposition you are using.
- Some textbooks use natural response and zero-input response interchangeably. Follow the stated definition rather than assuming that every source uses the same convention.

## Common mistakes

- Using $H(s)X(s)$ for the total response when initial conditions are nonzero.
- Splitting a final numerator arbitrarily instead of recomputing ZIR and ZSR from their definitions.
- Assuming the ZIR contains only one term. It generally contains all excited system modes.
- Calling every system-pole term the ZIR. System-pole terms may also appear in the ZSR.
- Treating zero-state and forced response as synonyms.
- Treating natural and transient response as synonyms without checking whether the natural modes decay.
- Calling a constant the only possible steady state. A sinusoid can also be a steady-state response.

## Practice

1. What do you set to zero to calculate the ZIR?
2. What do you set to zero to calculate the ZSR?
3. For $H(s)=1/[(s+1)(s+4)]$ and $X(s)=5/(s+6)$, predict the possible ZSR modes if there are no cancellations.
4. For $y_{zs}(t)=(1-e^{-2t})u(t)$, identify the transient and steady-state parts.
5. A stable system is driven by $e^{-5t}u(t)$, and its forced response contains $Ce^{-5t}u(t)$. Is this forced term transient or steady state?
6. Why is the zero-state response generally not identical to the forced response?

<details><summary>Answers</summary>

1. The external input; retain the initial conditions.
2. All initial conditions; retain the input.
3. $e^{-t}$, $e^{-4t}$, and $e^{-6t}$.
4. The transient is $-e^{-2t}u(t)$, and the steady-state part is $u(t)$.
5. It is a forced term because it comes from the input, and it is transient because it approaches zero.
6. The zero-state response may include system-pole terms needed to satisfy zero initial conditions, in addition to an input-related particular solution.

</details>

