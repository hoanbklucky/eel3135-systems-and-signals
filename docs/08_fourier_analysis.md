# 8. Fourier series and Fourier transform

## Why Fourier series is useful

A periodic waveform can be complicated in time but simple in frequency: it is a sum of a DC value and sinusoidal harmonics. Fourier series lets us replace one difficult periodic-input problem with many easy sinusoidal-input problems.

For an LTI system, the workflow is:

1. calculate the Fourier coefficients of the periodic input;
2. let the system scale and phase-shift each harmonic;
3. add the output harmonics to reconstruct the output.

This is useful for filtering, audio, communications, power electronics, vibration, and circuits driven by pulse or square waves.

Before applying Fourier series to electrical circuits, read [Phasors and impedance for Fourier-series circuits](08a_phasors_and_impedance.md). It derives the phasor and impedance rules used for each harmonic.

## Fundamental frequency and harmonics

If a signal has fundamental period $T_0$, its fundamental angular frequency is

$$
\omega_0=\frac{2\pi}{T_0}.
$$

The allowed Fourier-series frequencies are integer multiples of $\omega_0$:

$$
0,\ \omega_0,\ 2\omega_0,\ 3\omega_0,\ldots
$$

The component at $n\omega_0$ is called the $n$th harmonic. Fourier series does not create arbitrary frequencies between these harmonics.

## Trigonometric Fourier series

One common convention is

$$
x(t)=\frac{a_0}{2}
+\sum_{n=1}^{\infty}
\left[a_n\cos(n\omega_0t)+b_n\sin(n\omega_0t)\right].
$$

The coefficients are calculated over any complete period:

$$
a_0=\frac{2}{T_0}\int_{t_0}^{t_0+T_0}x(t)\,dt,
$$

$$
a_n=\frac{2}{T_0}\int_{t_0}^{t_0+T_0}x(t)\cos(n\omega_0t)\,dt,
$$

$$
b_n=\frac{2}{T_0}\int_{t_0}^{t_0+T_0}x(t)\sin(n\omega_0t)\,dt.
$$

Interpretation:

- $a_0/2$ is the average or DC value;
- $a_n$ is the weight of the cosine at $n\omega_0$;
- $b_n$ is the weight of the sine at $n\omega_0$.

These formulas work because different harmonics are orthogonal over one complete period. Multiplying by one basis sinusoid and integrating cancels the other harmonics.

## Symmetry shortcuts before integrating

Choose a period symmetric about the origin, such as $[-T_0/2,T_0/2]$, and inspect the signal first.

### Even signal

If $x(-t)=x(t)$, the signal is even. An even signal has no sine terms:

$$
b_n=0.
$$

The remaining integrals can be doubled over half a period:

$$
a_0=\frac{4}{T_0}\int_0^{T_0/2}x(t)\,dt,
$$

$$
a_n=\frac{4}{T_0}\int_0^{T_0/2}x(t)\cos(n\omega_0t)\,dt.
$$

### Odd signal

If $x(-t)=-x(t)$, the signal is odd. An odd signal has no DC or cosine terms:

$$
a_0=0,
$$

$$
a_n=0.
$$

Only the sine coefficients remain:

$$
b_n=\frac{4}{T_0}\int_0^{T_0/2}x(t)\sin(n\omega_0t)\,dt.
$$

Symmetry does more than save algebra: it predicts which coefficients must be zero before any calculation.

## Quick odd-signal example

Let $x(t)=t$ for $-\pi<t<\pi$, repeated with period $2\pi$. The signal is odd, so $a_0=a_n=0$ and $\omega_0=1$ rad/s. Then

$$
b_n=\frac{2}{\pi}\int_0^\pi t\sin(nt)\,dt.
$$

Integration by parts gives

$$
b_n=\frac{2(-1)^{n+1}}{n}.
$$

Therefore,

$$
x(t)=2\sin t-\sin(2t)+\frac{2}{3}\sin(3t)-\cdots
$$

The symmetry prediction and the calculated coefficients agree: only sine terms appear.

## Compact amplitude-phase form

The pair

$$
a_n\cos(n\omega_0t)+b_n\sin(n\omega_0t)
$$

can be written as one cosine:

$$
C_n\cos(n\omega_0t+\phi_n).
$$

Expanding the compact form and matching coefficients gives

$$
C_n=\sqrt{a_n^2+b_n^2},
$$

$$
\phi_n=\arg(a_n-jb_n).
$$

On a calculator or in software, evaluate this angle with `atan2(-b_n,a_n)` so the correct quadrant is retained.

For example, if $a_1=3$ and $b_1=4$, then

$$
C_1=5,
$$

$$
\phi_1=-53.1^\circ,
$$

so

$$
3\cos(\omega_0t)+4\sin(\omega_0t)
=5\cos(\omega_0t-53.1^\circ).
$$

## Exponential Fourier series

The same periodic signal can be written as

$$
x(t)=\sum_{k=-\infty}^{\infty}D_k e^{jk\omega_0t},
$$

where

$$
D_k=\frac{1}{T_0}\int_{t_0}^{t_0+T_0}x(t)e^{-jk\omega_0t}\,dt.
$$

For the trigonometric convention used above,

$$
D_0=\frac{a_0}{2},
$$

$$
D_n=\frac{a_n-jb_n}{2},
$$

$$
D_{-n}=\frac{a_n+jb_n}{2}.
$$

For a real signal, $D_{-n}=D_n^*$. The positive- and negative-frequency terms form one real sinusoid; they are not two separate physical oscillations.

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
D_k=\frac{T_1}{T_0}\,\mathrm{sinc}\left(k\frac{T_1}{T_0}\right),
$$

where $\mathrm{sinc}(x)=\sin(\pi x)/(\pi x)$. Also,

$$
D_0=\frac{T_1}{T_0},
$$

the average value or duty cycle. Narrower pulses spread energy across more harmonics.

## Common Fourier-transform pairs

Using $X(j\omega)=\int x(t)e^{-j\omega t}dt$:

| $x(t)$ | $X(j\omega)$ |
|---|---|
| $e^{-at}u(t)$, $a>0$ | $1/(a+j\omega)$ |
| rectangular pulse of width $T$ | $T\,\mathrm{sinc}(\omega T/2\pi)$ |
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

