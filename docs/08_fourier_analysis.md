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

