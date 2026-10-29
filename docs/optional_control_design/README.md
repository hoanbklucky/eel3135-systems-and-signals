# Optional extension: root locus and stability margins

This module extends the feedback ideas from [Module 7A](../07a_feedback_controls.md). It is not required for the main Systems and Signals sequence. Use it if you want to see how engineers move from analyzing a closed-loop system to making an informed gain choice.

## Learning goals

After studying this module, you should be able to:

- explain what a root locus shows;
- sketch the important features of a simple root locus;
- use a characteristic equation to find the stable range of a gain;
- define gain crossover, phase crossover, phase margin, and gain margin;
- calculate margins for a specific loop transfer function;
- connect pole locations and margins to likely transient behavior.

The purpose is interpretation, not memorizing every root-locus rule.

## The example used throughout

Consider a unity negative-feedback system with forward-path transfer function

$$
G(s)=\frac{K}{s(s+2)(s+4)},
$$

and feedback-path transfer function

$$
H(s)=1.
$$

The closed-loop transfer function is

$$
T(s)=\frac{G(s)}{1+G(s)}
=\frac{K}{s(s+2)(s+4)+K}.
$$

Therefore the closed-loop characteristic equation is

$$
s^3+6s^2+8s+K=0.
$$

Changing $K$ changes the roots of this polynomial. Those roots are the closed-loop poles, so changing $K$ changes stability and transient response.

## 1. Root locus: where do the closed-loop poles go?

The root locus is the set of all closed-loop pole locations as a real gain $K$ varies from zero to infinity.

It answers a practical question:

> If I change only the gain, which pole patterns and response shapes are possible?

For the example, the open-loop poles are

$$
0,\quad -2,\quad -4,
$$

and there are no finite open-loop zeros.

At $K=0$, the closed-loop poles begin at the open-loop poles. As $K$ increases, the three branches move away from those starting locations. Because there are no finite zeros, all three branches eventually go to infinity.

### Real-axis portions

A point on the real axis belongs to the root locus when the number of real open-loop poles and zeros to its right is odd.

For this example, the real-axis portions are

$$
(-\infty,-4)
\quad\text{and}\quad
(-2,0).
$$

Thus the poles at $0$ and $-2$ move toward one another before leaving the real axis. The pole at $-4$ moves left.

### Asymptotes

There are three poles and no zeros, so the three branches have asymptote angles

$$
60^\circ,\quad 180^\circ,\quad 300^\circ.
$$

Their common centroid is

$$
\sigma_a
=\frac{(0-2-4)-0}{3}
=-2.
$$

The asymptotes predict the large-gain directions; they are not the exact branch shapes near the poles.

### Breakaway point

From the characteristic equation,

$$
K=-s(s+2)(s+4).
$$

A real-axis breakaway candidate satisfies

$$
\frac{dK}{ds}=0.
$$

Therefore

$$
3s^2+12s+8=0,
$$

which gives

$$
s=-2\pm\frac{2\sqrt3}{3}.
$$

Only

$$
s\approx-0.845
$$

lies on a real-axis root-locus segment. Substituting it into $K=-s(s+2)(s+4)$ gives

$$
K\approx3.08.
$$

At this gain, the two real poles between $-2$ and $0$ meet and then become a complex-conjugate pair. This is the point where the response changes from a sum of nonoscillatory modes to an oscillatory mode.

## 2. Exact stability range from the Routh test

The root locus gives a geometric picture. The Routh test gives the exact gain range for stability.

For

$$
s^3+6s^2+8s+K,
$$

the first column of the Routh array is

$$
1,\quad 6,\quad \frac{48-K}{6},\quad K.
$$

Every first-column entry must have the same sign for all closed-loop poles to lie in the open left half-plane. Hence

$$
0<K<48.
$$

At $K=48$, a conjugate pole pair reaches the imaginary axis. The auxiliary equation is

$$
6s^2+48=0,
$$

so the crossing occurs at

$$
s=\pm j\sqrt8=\pm j2\sqrt2.
$$

The third pole is at $-6$. Therefore:

- $0<K<48$: asymptotically stable;
- $K=48$: marginal boundary with sustained oscillation;
- $K>48$: unstable.

This calculation also checks the root-locus prediction.

## 3. Why frequency-domain margins are useful

The root locus studies closed-loop poles as a parameter changes. Stability margins study how close the frequency response of the open loop is to the critical condition

$$
L(j\omega)=-1,
$$

where

$$
L(s)=G(s)H(s)
$$

is the loop transfer function.

For unity feedback in this example,

$$
L(s)=\frac{K}{s(s+2)(s+4)}.
$$

Two frequencies are important:

- **Gain-crossover frequency** $\omega_{gc}$: the frequency where $|L(j\omega)|=1$.
- **Phase-crossover frequency** $\omega_{pc}$: the frequency where $\angle L(j\omega)=-180^\circ$.

The margins are then

$$
\mathrm{PM}=180^\circ+\angle L(j\omega_{gc}),
$$

and

$$
\mathrm{GM}=\frac{1}{|L(j\omega_{pc})|}.
$$

In decibels,

$$
\mathrm{GM}_{dB}=20\log_{10}(\mathrm{GM}).
$$

Positive margins are evidence of stability for the nominal loop, but a comfortable design normally needs more than margins that are barely positive.

## 4. Worked margin example: choose $K=12$

Let

$$
L(s)=\frac{12}{s(s+2)(s+4)}.
$$

Its magnitude is

$$
|L(j\omega)|
=\frac{12}{\omega\sqrt{\omega^2+4}\sqrt{\omega^2+16}},
$$

and its phase is

$$
\angle L(j\omega)
=-90^\circ
-\tan^{-1}\left(\frac{\omega}{2}\right)
-\tan^{-1}\left(\frac{\omega}{4}\right).
$$

### Gain margin

At phase crossover,

$$
\tan^{-1}\left(\frac{\omega}{2}\right)
+\tan^{-1}\left(\frac{\omega}{4}\right)
=90^\circ.
$$

For positive arguments, this occurs when

$$
\frac{\omega}{2}\frac{\omega}{4}=1,
$$

so

$$
\omega_{pc}=\sqrt8\approx2.828\ \mathrm{rad/s}.
$$

At that frequency, the denominator magnitude is $48$, so

$$
|L(j\omega_{pc})|=\frac{12}{48}=0.25.
$$

Therefore

$$
\mathrm{GM}=4,
$$

or

$$
\mathrm{GM}_{dB}=20\log_{10}(4)\approx12.04\ \mathrm{dB}.
$$

The gain could be multiplied by four before reaching the stability boundary. This agrees with the Routh result: $12\times4=48$.

### Phase margin

The gain-crossover condition is

$$
\omega^2(\omega^2+4)(\omega^2+16)=12^2.
$$

Solving gives

$$
\omega_{gc}\approx1.224\ \mathrm{rad/s}.
$$

At that frequency,

$$
\angle L(j\omega_{gc})\approx-138.47^\circ.
$$

Hence

$$
\mathrm{PM}
=180^\circ-138.47^\circ
\approx41.53^\circ.
$$

The loop is stable and has a moderate phase margin. Its closed-loop response should be underdamped but not close to sustained oscillation.

## 5. Connecting the two design views

For the same example:

- The **root locus** shows how every closed-loop pole moves as $K$ varies.
- The **Routh test** proves that the stable range is $0<K<48$.
- The **gain margin** at $K=12$ says the loop can tolerate a gain factor of four before reaching the boundary.
- The **phase margin** gives a practical indication of relative damping and robustness to additional phase lag.

These are not four unrelated calculations. They are different views of the same feedback loop.

## 6. What margins do and do not guarantee

Margins are most directly interpreted for a standard single-loop feedback system. They summarize distance from the critical point, but they do not completely describe the time response.

Keep these cautions in mind:

- A larger phase margin often corresponds to less overshoot, but it is not an exact overshoot formula for every system.
- A large gain margin does not guarantee a fast response.
- Pole-zero cancellations can hide important internal dynamics.
- Time delays add phase lag and can reduce phase margin sharply.
- A design should be checked in both the frequency and time domains.

## 7. Optional software verification

The calculations can be checked with the Python Control Systems Library:

```python
import control as ct
import matplotlib.pyplot as plt

# Base loop: K is varied by root_locus.
L0 = ct.tf([1], [1, 6, 8, 0])
ct.root_locus(L0, grid=True)
plt.show()

# Margin calculation for K = 12.
L12 = 12 * L0
gain_margin, phase_margin, phase_cross, gain_cross = ct.margin(L12)

print("gain margin factor:", gain_margin)
print("phase margin (deg):", phase_margin)
print("phase-crossover frequency (rad/s):", phase_cross)
print("gain-crossover frequency (rad/s):", gain_cross)
```

Expected values are approximately:

```text
gain margin factor: 4.00
phase margin: 41.53 degrees
phase-crossover frequency: 2.828 rad/s
gain-crossover frequency: 1.224 rad/s
```

Use software to verify the reasoning, not to replace the characteristic equation and frequency-response interpretation.

## Practice

1. For the example loop, classify stability at $K=3$, $K=12$, $K=48$, and $K=60$.
2. Explain what happens to the two branches that start at $0$ and $-2$ near $K=3.08$.
3. For $K=24$, determine the gain margin from the known stability boundary.
4. Why can an added time delay make a loop unstable even though it does not change the Bode magnitude?
5. State one question answered well by root locus and one answered well by stability margins.

<details><summary>Answers</summary>

1. $K=3$ and $K=12$ are stable; $K=48$ is the marginal boundary; $K=60$ is unstable.
2. They meet near $s=-0.845$ and leave the real axis as a complex-conjugate pair, introducing an oscillatory closed-loop mode.
3. The gain can increase from $24$ to $48$, so the gain margin is $2$, or approximately $6.02$ dB.
4. A delay contributes phase lag. It can reduce the phase margin until the loop reaches the critical $-180^\circ$ condition at unity magnitude.
5. Root locus shows how closed-loop poles move with gain. Margins show how close a chosen loop is to the critical frequency-domain stability condition.

</details>
