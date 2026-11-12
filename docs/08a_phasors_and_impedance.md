# 8A. Phasors and impedance for Fourier-series circuits

## Why this background is needed

Fourier series expresses a periodic signal as a DC component plus sinusoidal harmonics. Circuit analysis then asks a second question:

> How does the circuit change the amplitude and phase of each harmonic?

Phasors and impedance answer that question. The complete workflow is

$$
x(t)
\longrightarrow
\text{Fourier harmonics}
\longrightarrow
\text{phasor response at each harmonic}
\longrightarrow
y(t).
$$

The Fourier series identifies the input ingredients. The circuit frequency response tells how the circuit modifies each ingredient.

## Why the $n$th harmonic has frequency $n\omega_0$

For a signal with period $T_0$, the fundamental angular frequency is

$$
\omega_0=\frac{2\pi}{T_0}.
$$

The trigonometric Fourier series contains terms of the form

$$
\cos(n\omega_0t)
\quad\text{and}\quad
\sin(n\omega_0t).
$$

During one fundamental period, the $n$th harmonic completes $n$ cycles. Its angular frequency is therefore

$$
\boxed{\omega_n=n\omega_0}.
$$

| Harmonic | Angular frequency |
|---|---:|
| Fundamental, $n=1$ | $\omega_0$ |
| Second harmonic, $n=2$ | $2\omega_0$ |
| Third harmonic, $n=3$ | $3\omega_0$ |

Each harmonic encounters a different circuit impedance because inductor and capacitor impedances depend on frequency.

## What a phasor represents

Consider one sinusoid written using cosine as the reference:

$$
x(t)=A\cos(\omega t+\phi).
$$

Its phasor is the complex number

$$
\boxed{X=Ae^{j\phi}=A\angle\phi}.
$$

The phasor stores two pieces of information:

- magnitude $A$;
- phase $\phi$.

The common time dependence at frequency $\omega$ is omitted while performing the circuit algebra. The angular frequency must still be recorded separately because the impedances depend on it.

These notes use **peak-amplitude phasors**. Some circuit courses use RMS magnitudes instead. Either convention works if it is used consistently.

### Example: cosine reference

$$
v(t)=5\cos(3t-30^\circ)
$$

has angular frequency $3$ rad/s and phasor

$$
\boxed{V=5\angle-30^\circ}.
$$

### Converting sine to a phasor

Because

$$
\sin\theta=\cos(\theta-90^\circ),
$$

we obtain

$$
A\sin(\omega t+\phi)
=
A\cos(\omega t+\phi-90^\circ).
$$

Therefore,

$$
\boxed{A\sin(\omega t+\phi)
\longleftrightarrow
A\angle(\phi-90^\circ)}.
$$

For example,

$$
4\sin(10t)=4\cos(10t-90^\circ)
$$

corresponds to

$$
V=4\angle-90^\circ.
$$

## Determining a phasor from Fourier coefficients

Suppose the $n$th trigonometric Fourier component is

$$
x_n(t)=a_n\cos(n\omega_0t)+b_n\sin(n\omega_0t).
$$

Write the same component as

$$
x_n(t)=A_n\cos(n\omega_0t+\phi_n).
$$

Its amplitude is

$$
\boxed{A_n=\sqrt{a_n^2+b_n^2}}.
$$

Using the two-argument arctangent to select the correct quadrant,

$$
\boxed{\phi_n=\mathrm{atan2}(-b_n,a_n)}.
$$

The harmonic phasor is then

$$
\boxed{X_n=A_n\angle\phi_n}.
$$

### Example

If

$$
x_n(t)=3\cos(n\omega_0t)+4\sin(n\omega_0t),
$$

then

$$
A_n=\sqrt{3^2+4^2}=5
$$

and

$$
\phi_n=\mathrm{atan2}(-4,3)=-53.1^\circ.
$$

Thus,

$$
x_n(t)=5\cos(n\omega_0t-53.1^\circ)
$$

and

$$
X_n=5\angle-53.1^\circ.
$$

## Impedance

Impedance is the phasor-domain ratio of voltage to current at a specified angular frequency:

$$
\boxed{Z(j\omega)=\frac{V}{I}}.
$$

It plays the role that resistance plays in a DC circuit, but it can change both magnitude and phase.

## Resistor impedance

The resistor law is

$$
v_R(t)=Ri_R(t).
$$

The phasors therefore satisfy

$$
V_R=RI_R,
$$

so

$$
\boxed{Z_R=R}.
$$

The resistor impedance does not depend on frequency and produces no voltage-current phase shift.

## Inductor impedance

The inductor law is

$$
v_L(t)=L\frac{di_L(t)}{dt}.
$$

For a sinusoid at angular frequency $\omega$, differentiation becomes multiplication by $j\omega$. Thus,

$$
V_L=j\omega L I_L,
$$

and

$$
\boxed{Z_L=j\omega L=\omega L\angle90^\circ}.
$$

Consequences:

- at DC, $\omega=0$ and $Z_L=0$, so an ideal inductor behaves like a short circuit in steady state;
- the impedance magnitude $|Z_L|=\omega L$ increases with frequency;
- inductor voltage leads inductor current by $90^\circ$.

For the $n$th Fourier harmonic,

$$
\boxed{Z_{L,n}=jn\omega_0L}.
$$

## Capacitor impedance

The capacitor law is

$$
i_C(t)=C\frac{dv_C(t)}{dt}.
$$

For a sinusoid at angular frequency $\omega$,

$$
I_C=j\omega C V_C.
$$

Therefore,

$$
\boxed{Z_C=\frac{V_C}{I_C}=\frac{1}{j\omega C}=-\frac{j}{\omega C}}.
$$

In polar form,

$$
\boxed{Z_C=\frac{1}{\omega C}\angle-90^\circ}.
$$

Consequences:

- at DC, $|Z_C|$ approaches infinity, so an ideal capacitor behaves like an open circuit in steady state;
- the impedance magnitude $|Z_C|=1/(\omega C)$ decreases with frequency;
- capacitor current leads capacitor voltage by $90^\circ$.

For the $n$th Fourier harmonic,

$$
\boxed{Z_{C,n}=\frac{1}{jn\omega_0C}}.
$$

## Comparison of the three elements

| Element | Impedance | At DC | As frequency increases |
|---|---|---|---|
| Resistor | $R$ | $R$ | unchanged |
| Inductor | $j\omega L$ | short circuit | magnitude increases |
| Capacitor | $1/(j\omega C)$ | open circuit | magnitude decreases |

## Applying an LTI circuit to Fourier harmonics

For the $n$th harmonic, evaluate the circuit at

$$
\omega_n=n\omega_0.
$$

If $X_n$ is the input phasor and $H(j\omega)$ is the circuit frequency response, then

$$
\boxed{Y_n=H(jn\omega_0)X_n}.
$$

This equation means:

- $|H(jn\omega_0)|$ scales the harmonic amplitude;
- the phase of $H(jn\omega_0)$ shifts the harmonic phase;
- the harmonic frequency remains $n\omega_0$.

The procedure is:

1. calculate or identify the Fourier harmonics of the input;
2. convert each harmonic to a phasor;
3. evaluate the circuit at that harmonic frequency;
4. calculate the output phasor;
5. convert the output phasors back to sinusoids and add them;
6. handle the DC term separately by evaluating the circuit at $\omega=0$.

## Worked RL example: output across the inductor

Consider a series RL circuit with

$$
R=5\ \Omega,
\qquad
L=2\ \mathrm{H},
$$

and measure the output across the inductor.

The frequency response follows from the voltage divider:

$$
H_L(j\omega)
=
\frac{Z_L}{Z_R+Z_L}
=
\frac{j\omega L}{R+j\omega L}.
$$

Suppose the input is a pulse train that equals one from $0$ to $1$ second and zero from $1$ to $2$ seconds, repeating every $2$ seconds. Then

$$
T_0=2\ \mathrm{s},
\qquad
\omega_0=\frac{2\pi}{T_0}=\pi\ \mathrm{rad/s}.
$$

Its Fourier series is

$$
v_s(t)
=
\frac{1}{2}
+
\frac{2}{\pi}
[
\sin(\pi t)
+\frac{1}{3}\sin(3\pi t)
+\frac{1}{5}\sin(5\pi t)
+\cdots
].
$$

For odd $n$, the source harmonic is

$$
v_{s,n}(t)=\frac{2}{n\pi}\sin(n\pi t),
$$

so its phasor is

$$
V_{s,n}=\frac{2}{n\pi}\angle-90^\circ.
$$

Because $\omega_n=n\pi$,

$$
j\omega_nL=j(n\pi)(2)=j2n\pi.
$$

The $n$th output harmonic is therefore

$$
\boxed{
V_{o,n}
=
\frac{j2n\pi}{5+j2n\pi}V_{s,n}
}.
$$

The notation $V_{o,n}$ and $V_{s,n}$ matters: this voltage-divider calculation applies to one harmonic at a time.

For the DC component, $\omega=0$ and $Z_L=0$. Therefore,

$$
H_L(0)=0,
$$

so the output has no DC component. Because the output is across the inductor, this circuit behaves like a high-pass filter: higher harmonics experience a larger output-to-input ratio.

## RC example: output across the capacitor

For a series RC circuit with the output across the capacitor,

$$
H_C(j\omega)
=
\frac{Z_C}{R+Z_C}.
$$

Substituting $Z_C=1/(j\omega C)$ gives

$$
\boxed{H_C(j\omega)=\frac{1}{1+j\omega RC}}.
$$

For the $n$th Fourier harmonic,

$$
\boxed{V_{o,n}=\frac{1}{1+jn\omega_0RC}V_{s,n}}.
$$

At DC, $H_C(0)=1$, so the average value passes. As $n$ increases, the output magnitude decreases. The higher harmonics that create sharp edges are attenuated, so a square-wave output becomes smoother and more sinusoidal.

## Common mistakes

- Using $\omega_0$ for every harmonic instead of $n\omega_0$.
- Treating $V_s$ as the entire nonsinusoidal waveform inside one phasor calculation. Each harmonic needs its own phasor $V_{s,n}$.
- Forgetting to convert sine into the cosine-reference phasor.
- Combining phasors that have different frequencies. Phasor addition is valid only for sinusoids at the same frequency.
- Forgetting to handle the DC term separately.
- Confusing capacitor impedance with capacitor admittance. The admittance is $Y_C=j\omega C$, while the impedance is $Z_C=1/(j\omega C)$.
- Assuming that low capacitor impedance always means a large output. The answer depends on where the output is measured.

## Practice

1. A periodic signal has $T_0=0.5$ s. What are $\omega_0$ and $\omega_3$?
2. Convert $6\sin(4t+20^\circ)$ into a cosine-reference phasor.
3. Find the impedance of a $0.1$ H inductor at $\omega=20$ rad/s.
4. Find the impedance of a $100\ \mu\mathrm{F}$ capacitor at $\omega=50$ rad/s.
5. Why must the DC component be treated separately in a phasor calculation?

<details><summary>Answers</summary>

1. $\omega_0=4\pi$ rad/s and $\omega_3=12\pi$ rad/s.
2. $6\sin(4t+20^\circ)=6\cos(4t-70^\circ)$, so the phasor is $6\angle-70^\circ$.
3. $Z_L=j\omega L=j(20)(0.1)=j2\ \Omega$.
4. $Z_C=1/[j(50)(100\times10^{-6})]=-j200\ \Omega$.
5. DC has $\omega=0$. Inductors and capacitors reach limiting short-circuit or open-circuit behavior, and the ordinary sinusoidal phasor picture no longer represents a rotating component.

</details>
