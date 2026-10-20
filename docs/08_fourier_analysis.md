# 8. Fourier series and Fourier transform

## Fourier series

A periodic signal can be represented as a sum of harmonically related complex exponentials:

$$
x(t)=\sum_{k=-\infty}^{\infty}D_k e^{jk\omega_0t},
$$

where

$$
D_k=\frac{1}{T_0}\int_{t_0}^{t_0+T_0}x(t)e^{-jk\omega_0t}\,dt.
$$

The coefficient $D_k$ tells how much of the frequency $k\omega_0$ appears in the signal.

## Fourier transform

For an aperiodic signal,

$$
X(j\omega)=\int_{-\infty}^{\infty}x(t)e^{-j\omega t}\,dt.
$$

The inverse transform reconstructs the signal:

$$
x(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}X(j\omega)e^{j\omega t}\,d\omega.
$$

## LTI filtering

Convolution in time becomes multiplication in frequency:

$$
y(t)=x(t)*h(t)
\quad\Longleftrightarrow\quad
Y(j\omega)=X(j\omega)H(j\omega).
$$

The system scales and phase-shifts each frequency component according to $H(j\omega)$.

## Checks

- A real time-domain signal has conjugate-symmetric spectrum.
- Narrow features in time generally require broad frequency content.
- Time delay changes phase but not magnitude.

## Interpreting the complex Fourier-series coefficients

For a real periodic signal,

$$
D_{-k}=D_k^*.
$$

Thus negative-frequency coefficients are not extra physical sinusoids; together with their positive-frequency partners, they produce real cosine and sine components.

The line spectrum occurs only at integer multiples $k\omega_0$. A signal with sharp transitions generally needs many harmonics to reproduce those transitions accurately.

## Worked Fourier-series example: a rectangular pulse train

Consider a periodic signal of period $T_0$ that equals one for $|t|<T_1/2$ during each period and zero otherwise. With $\omega_0=2\pi/T_0$,

$$
D_k=\frac{1}{T_0}\int_{-T_1/2}^{T_1/2}e^{-jk\omega_0t}dt.
$$

For $k\ne0$,

$$
D_k=\frac{T_1}{T_0}\operatorname{sinc}\left(k\frac{T_1}{T_0}\right),
$$

where $\operatorname{sinc}(x)=\sin(\pi x)/(\pi x)$. Also,

$$
D_0=\frac{T_1}{T_0},
$$

the average value or duty cycle. Narrower pulses spread energy across more harmonics.

## Common Fourier-transform pairs

Using $X(j\omega)=\int x(t)e^{-j\omega t}dt$:

| $x(t)$ | $X(j\omega)$ |
|---|---|
| $e^{-at}u(t)$, $a>0$ | $1/(a+j\omega)$ |
| rectangular pulse of width $T$ | $T\operatorname{sinc}(\omega T/2\pi)$ |
| $\delta(t-t_0)$ | $e^{-j\omega t_0}$ |
| $1$ | $2\pi\delta(\omega)$ |

The exact sinc notation varies among textbooks, so always check whether sinc means $\sin x/x$ or $\sin(\pi x)/(\pi x)$.

## Properties with physical meaning

### Time shift

$$
x(t-t_0)\longleftrightarrow e^{-j\omega t_0}X(j\omega).
$$

A delay changes phase but not spectral magnitude.

### Time scaling

$$
x(at)\longleftrightarrow\frac{1}{|a|}X\left(j\frac{\omega}{a}\right).
$$

Compressing a signal in time expands its spectrum.

### Differentiation

$$
\frac{dx}{dt}\longleftrightarrow j\omega X(j\omega).
$$

Differentiation emphasizes high frequencies, which explains why differentiators also amplify high-frequency noise.

### Parseval's relation

$$
\int_{-\infty}^{\infty}|x(t)|^2dt
=\frac{1}{2\pi}\int_{-\infty}^{\infty}|X(j\omega)|^2d\omega.
$$

Signal energy can be calculated in either domain.

## Filtering example

Suppose an input consists of two sinusoids,

$$
x(t)=\cos(2t)+0.5\cos(20t),
$$

and the system has $|H(j2)|\approx1$ but $|H(j20)|\approx0.05$. The low-frequency component passes almost unchanged, while the high-frequency component becomes only $0.025$ in amplitude. Frequency-domain multiplication makes the filtering effect visible without separately solving for the complete time response.

## Common mistakes

- Mixing hertz $f$ and angular frequency $\omega$.
- Forgetting the $1/(2\pi)$ factor in the inverse-transform convention used here.
- Treating negative frequency as a separate physical oscillation for real signals.
- Assuming every signal has an ordinary Fourier transform; impulses may be required.
- Confusing Fourier-series line spectra with the continuous spectrum of an aperiodic signal.

## Practice

1. What happens to $|X(j\omega)|$ when $x(t)$ is delayed?
2. If a pulse becomes narrower in time, what happens to its main spectral width?
3. Why does an ideal low-pass filter smooth sharp corners?

<details><summary>Answers</summary>

1. It is unchanged; only phase changes.
2. It becomes wider.
3. Sharp corners require high-frequency components, which the low-pass filter removes.

</details>

