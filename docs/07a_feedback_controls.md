# 7A. Feedback and control applications

## Learning goals

After studying this module, you should be able to:

- derive the closed-loop transfer function of a negative-feedback system;
- distinguish open-loop poles from closed-loop poles;
- determine stability from the closed-loop characteristic equation;
- predict how a gain change affects damping and oscillation;
- explain how feedback changes reference tracking and disturbance response;
- recognize that feedback can improve performance without guaranteeing stability.

This module uses feedback to connect block diagrams, transfer functions, poles, stability, and time response. Detailed controller design belongs in a later controls course.

## Why use feedback?

An open-loop system acts without comparing its output with the desired result. A feedback system measures the output and uses the difference between the desired and measured signals to drive the plant.

For negative feedback,

$$
e(t)=r(t)-y_m(t).
$$

The error signal tells the system how far the measured output is from the reference. The controller and plant respond to that error.

Feedback can:

- reduce the effect of parameter changes;
- improve reference tracking;
- reduce the effect of some disturbances;
- change the transient response;
- move the system poles and therefore change stability.

These effects depend on the loop transfer function. Feedback does not automatically improve every property.

## Standard negative-feedback system

Let $G(s)$ denote the forward-path transfer function and $H(s)$ denote the feedback-path transfer function. With zero initial conditions,

$$
E(s)=R(s)-H(s)Y(s),
$$

and

$$
Y(s)=G(s)E(s).
$$

Substitute the error equation:

$$
Y(s)=G(s)[R(s)-H(s)Y(s)].
$$

Collect the output terms:

$$
[1+G(s)H(s)]Y(s)=G(s)R(s).
$$

Therefore the closed-loop transfer function is

$$
\boxed{
T(s)=\frac{Y(s)}{R(s)}
=\frac{G(s)}{1+G(s)H(s)}
}
$$

for negative feedback.

For unity feedback, $H(s)=1$, so

$$
T(s)=\frac{G(s)}{1+G(s)}.
$$

## The closed-loop poles

The closed-loop poles are roots of the denominator of the simplified closed-loop transfer function. They satisfy the characteristic equation

$$
1+G(s)H(s)=0.
$$

Do not use the poles of $G(s)$ alone to classify the closed-loop response. Closing the loop changes the denominator and usually moves the poles.

For a causal rational closed-loop system, BIBO stability requires every closed-loop pole to lie strictly in the open left half-plane.

## Worked example: gain changes the poles

Consider a unity-feedback system with

$$
G(s)=\frac{K}{s(s+2)},
\qquad H(s)=1.
$$

The closed-loop transfer function is

$$
T(s)=\frac{K}{s(s+2)+K}
=\frac{K}{s^2+2s+K}.
$$

The characteristic equation is

$$
s^2+2s+K=0,
$$

so the poles are

$$
s=-1\pm\sqrt{1-K}.
$$

### Case 1: $0<K<1$

The poles are distinct negative real numbers. The response is stable and overdamped.

For $K=0.5$,

$$
s=-1\pm\sqrt{0.5}
\approx-0.293,\ -1.707.
$$

The pole near $-0.293$ dominates the slow part of the response.

### Case 2: $K=1$

The poles coincide at $s=-1$. The response is critically damped.

### Case 3: $K>1$

The poles become

$$
s=-1\pm j\sqrt{K-1}.
$$

The response is stable and underdamped. The real part remains $-1$, while the oscillation frequency increases with $K$.

For $K=4$,

$$
s=-1\pm j\sqrt3.
$$

Increasing $K$ in this example speeds the oscillation and reduces the damping ratio. It does not move the real part farther left once the poles become complex.

## Connection with the standard second-order form

Compare

$$
s^2+2s+K
$$

with

$$
s^2+2\zeta\omega_n s+\omega_n^2.
$$

Then

$$
\omega_n=\sqrt K,
\qquad
\zeta=\frac{1}{\sqrt K}.
$$

As $K$ increases, the natural frequency increases and the damping ratio decreases. The step response becomes faster initially but develops more overshoot.

This tradeoff is a central control idea: changing gain changes both speed and transient shape.

## Reference tracking

For a stable closed-loop system with a unit-step reference,

$$
R(s)=\frac{1}{s}.
$$

The final-value theorem gives

$$
y(\infty)=\lim_{s\to0}sT(s)R(s)=T(0),
$$

provided the final-value conditions hold.

For the worked example,

$$
T(0)=\frac{K}{K}=1
$$

for $K>0$. Thus the stable system reaches the unit-step reference with zero steady-state error.

Always check closed-loop stability before using the final-value theorem.

## Output disturbances

Suppose a disturbance $D(s)$ enters at the plant output in a unity-feedback system. Then

$$
Y(s)=G(s)[R(s)-Y(s)]+D(s).
$$

Solving for the output gives

$$
Y(s)=\frac{G(s)}{1+G(s)}R(s)
+\frac{1}{1+G(s)}D(s).
$$

Define the sensitivity function

$$
S(s)=\frac{1}{1+G(s)}.
$$

The output disturbance passes through $S(s)$. If $|G(j\omega)|$ is large at a disturbance frequency, then $|S(j\omega)|$ is small and feedback reduces that disturbance.

Disturbance rejection therefore depends on frequency. A loop may reject slow disturbances while doing little to high-frequency disturbances.

## Measurement noise

Suppose measurement noise $N(s)$ is added to the measured output. For unity feedback,

$$
E(s)=R(s)-Y(s)-N(s),
$$

so

$$
Y(s)=\frac{G(s)}{1+G(s)}R(s)
-\frac{G(s)}{1+G(s)}N(s).
$$

Define the complementary sensitivity function

$$
T(s)=\frac{G(s)}{1+G(s)}.
$$

Then reference tracking and measurement-noise transmission both involve $T(s)$. A design that tracks high-frequency reference changes strongly may also transmit high-frequency measurement noise strongly.

The two functions satisfy

$$
S(s)+T(s)=1.
$$

This identity captures an important tradeoff. Feedback cannot make both functions small at the same frequency.

## Feedback and parameter sensitivity

Suppose the forward path $G(s)$ changes slightly because a physical parameter changes. The closed-loop transfer function

$$
T(s)=\frac{G(s)}{1+G(s)H(s)}
$$

is less sensitive to that change when the loop gain $|G(s)H(s)|$ is large.

For a small fractional change,

$$
\frac{\Delta T/T}{\Delta G/G}
\approx\frac{1}{1+G(s)H(s)}.
$$

This reduced sensitivity is one reason feedback systems can perform consistently even when component values vary.

## What feedback does not guarantee

Negative feedback at the summing junction does not guarantee a stable closed loop. Dynamics and phase shift can place closed-loop poles in the right half-plane.

Before claiming an improvement:

1. derive the closed-loop transfer function;
2. simplify it and find the closed-loop poles;
3. check stability;
4. then interpret tracking, transient response, and disturbance rejection.

## Scope for a Systems and Signals course

The essential skills are:

- deriving $G/(1+GH)$;
- finding the characteristic equation;
- relating closed-loop poles to stability and transient response;
- understanding tracking and disturbance paths;
- recognizing gain tradeoffs.

Root locus, Nyquist stability, gain margin, phase margin, and controller synthesis are valuable topics, but they fit more naturally in a dedicated controls course.

## Common mistakes

- Calling $K$ a feedback-path gain when it appears in the forward path $G(s)$.
- Using the poles of $G(s)$ as the closed-loop poles.
- Forgetting the sign at the summing junction.
- Applying the final-value theorem before checking closed-loop poles.
- Assuming larger gain always produces a better transient response.
- Claiming that negative feedback always stabilizes a system.
- Treating disturbance rejection as independent of frequency.

## Practice

1. For $G(s)=6/[s(s+3)]$ with unity feedback, find $T(s)$ and its poles.
2. For $G(s)=K/[s(s+4)]$, determine the value of $K$ that gives a repeated closed-loop pole.
3. A unity-feedback system has $G(s)=20/(s+2)$. Find the DC closed-loop gain and the final output for a unit-step reference.
4. In a unity-feedback system, which transfer function maps an output disturbance to the output?
5. Explain why increasing gain can improve steady-state tracking while worsening overshoot.

<details><summary>Answers</summary>

1. $T(s)=6/(s^2+3s+6)$, with poles $[-3\pm j\sqrt{15}]/2$. The system is stable and underdamped.
2. The denominator is $s^2+4s+K$. A repeated pole occurs when $16-4K=0$, so $K=4$ and the repeated pole is $-2$.
3. $T(s)=20/(s+22)$, so $T(0)=10/11$. The final output is $10/11$ if the closed loop starts from rest.
4. $S(s)=1/[1+G(s)]$ for an output disturbance in a unity-feedback system.
5. Larger low-frequency loop gain reduces tracking error, but the changed closed-loop pole locations can reduce damping and increase overshoot.

</details>

