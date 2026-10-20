# 9. Sampling

## Why sampling can work

Sampling multiplies a continuous-time signal by an impulse train. In frequency, this creates shifted copies of the original spectrum.

If the original signal is bandlimited to $|\omega|\leq\omega_m$, the copies do not overlap when

$$
\omega_s>2\omega_m.
$$

Equivalently,

$$
f_s>2f_{max}.
$$

This is the Nyquist sampling condition.

## Aliasing

When spectral copies overlap, different continuous-time frequencies produce the same samples. The ambiguity cannot be removed after sampling.

An anti-aliasing low-pass filter is therefore placed before the sampler to limit the input bandwidth.

## Concept check

A signal contains frequencies up to 3 kHz.

1. What is the theoretical minimum sampling rate?
2. Why would an engineer normally choose a higher rate?

<details><summary>Answers</summary>

1. Strictly greater than 6 kHz.
2. Real filters do not have instantaneous transitions, so a guard band is needed.

</details>

