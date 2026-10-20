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

