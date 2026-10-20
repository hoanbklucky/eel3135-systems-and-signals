# 6. Zero-input, zero-state, and total response

## The decomposition

For a linear system,

$$
y(t)=y_{zi}(t)+y_{zs}(t).
$$

- The **zero-input response** comes from initial stored energy. Set the applied input to zero and keep the initial conditions.
- The **zero-state response** comes from the applied input. Set every initial condition to zero and keep the input.

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

## Natural, forced, transient, and steady-state language

These terms overlap but are not identical:

- **Natural response:** modes associated with the system's characteristic roots.
- **Forced response:** modes introduced by the input.
- **Transient response:** terms that vanish as $t\to\infty$.
- **Steady-state response:** the part that remains after transients vanish.

A forced response can itself decay. For example, an input $e^{-5t}u(t)$ creates a forced term proportional to $e^{-5t}$, but that term still vanishes eventually.

## Common mistakes

- Using $H(s)X(s)$ for the total response when initial conditions are nonzero.
- Splitting a final numerator arbitrarily instead of recomputing ZIR and ZSR from their definitions.
- Assuming the ZIR contains only one term. It generally contains all excited system modes.
- Calling every system-pole term the ZIR. System-pole terms may also appear in the ZSR.

## Practice

1. What do you set to zero to calculate the ZIR?
2. What do you set to zero to calculate the ZSR?
3. For $H(s)=1/[(s+1)(s+4)]$ and $X(s)=5/(s+6)$, predict the possible ZSR modes if there are no cancellations.

<details><summary>Answers</summary>

1. The external input; retain the initial conditions.
2. All initial conditions; retain the input.
3. $e^{-t}$, $e^{-4t}$, and $e^{-6t}$.

</details>

