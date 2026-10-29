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

## What the sampler does in frequency

An ideal impulse-train sampler uses

$$
p(t)=\sum_{n=-\infty}^{\infty}\delta(t-nT_s),
$$

so the sampled signal is

$$
x_s(t)=x(t)p(t)=\sum_{n=-\infty}^{\infty}x(nT_s)\delta(t-nT_s).
$$

Multiplication in time becomes convolution in frequency. Because the impulse train also transforms to an impulse train, the sampled spectrum is

$$
X_s(j\omega)=\frac{1}{T_s}
\sum_{k=-\infty}^{\infty}X\bigl(j(\omega-k\omega_s)\bigr).
$$

Sampling therefore creates replicas of the original spectrum centered at integer multiples of $\omega_s$.

## Aliasing as frequency ambiguity

For samples taken at rate $f_s$,

$$
\cos(2\pi f t)
$$

and

$$
\cos[2\pi(f+kf_s)t]
$$

produce identical sample values for any integer $k$. A continuous-time frequency above $f_s/2$ is observed as a lower alias frequency.

One useful calculation is

$$
f_{alias}=|f-kf_s|,
$$

where $k$ is chosen so that $f_{alias}$ lies between 0 and $f_s/2$.

### Worked aliasing example

A 900 Hz sinusoid is sampled at 1 kHz. Choosing $k=1$ gives

$$
f_{alias}=|900-1000|=100\text{ Hz}.
$$

The samples cannot reveal whether the original analog sinusoid was 100 Hz or 900 Hz.

## Reconstruction

If the signal is bandlimited and the spectral replicas do not overlap, an ideal low-pass reconstruction filter can select the central replica. In the time domain, ideal reconstruction is sinc interpolation:

$$
x(t)=\sum_{n=-\infty}^{\infty}x(nT_s)
\mathrm{sinc}\left(\frac{t-nT_s}{T_s}\right).
$$

Real systems approximate this operation. Their nonideal filters motivate guard bands and sampling rates above the theoretical minimum.

## Practical sampling chain

```text
analog signal → anti-alias filter → sample-and-hold → ADC → digital processing
```

The anti-alias filter must come **before** the sampler. Once out-of-band components have aliased into the baseband, a later digital filter cannot determine where they came from.

Other practical issues include:

- quantization error from representing amplitude with finitely many bits;
- clock jitter, which creates timing error;
- finite record length, which limits frequency resolution;
- spectral leakage when the observation interval does not contain an integer number of cycles.

## Common mistakes

- Saying the Nyquist rate is $f_{max}$ rather than $2f_{max}$.
- Confusing sampling rate with the Nyquist frequency $f_s/2$.
- Choosing exactly $2f_{max}$ in a practical system with nonideal filters.
- Believing oversampling can remove aliasing that occurred before the signal reached the ADC.

## Additional practice

1. A 7 kHz sinusoid is sampled at 10 kHz. What alias appears below 5 kHz?
2. A signal is limited to 4 kHz. Why might an engineer choose 12 kHz instead of the theoretical 8 kHz boundary?
3. Where must the anti-alias filter be placed?

<details><summary>Answers</summary>

1. 3 kHz.
2. It provides a transition band for a realizable anti-alias filter.
3. Before sampling and analog-to-digital conversion.

</details>

