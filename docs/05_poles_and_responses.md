# 5. Poles and time-domain responses

## Read the poles before doing algebra

For a causal rational response, a pole $p$ contributes a mode proportional to $e^{pt}$.

| Pole pattern | Time-domain behavior |
|---|---|
| negative real pole | decaying exponential |
| positive real pole | growing exponential |
| repeated real pole | exponential multiplied by powers of $t$ |
| $\sigma\pm j\omega$ | oscillation at $\omega$ inside an $e^{\sigma t}$ envelope |

For example, poles at $-2\pm j5$ allow the form

$$
y(t)=e^{-2t}[C_1\cos(5t)+C_2\sin(5t)]u(t).
$$

The real part $-2$ determines decay. The imaginary part 5 determines angular frequency.

## System poles and input poles

When

$$
Y(s)=H(s)X(s),
$$
the poles of $H(s)$ supply system modes and the poles of $X(s)$ supply forced-response modes. Cancellations may remove a mode, so inspect the simplified product.

## Stability

For a causal rational LTI system, BIBO stability requires every pole of $H(s)$ to lie strictly in the open left half-plane.

Do not infer stability merely because one particular response looks bounded. Stability is a system property.

