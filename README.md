# EEL 3135 — Systems and Signals

This repository is a student learning guide for the core concepts in a first course on continuous-time systems and signals. It emphasizes three habits:

1. predict the form of an answer before calculating coefficients;
2. connect mathematical operations to physical system behavior;
3. check every result in both the time and transform domains.

The notes use the unilateral Laplace transform for causal system analysis. Region of convergence is not required in the main sequence.

## Learning roadmap

| Module | Topic | Central question |
|---|---|---|
| 1 | [Signals and operations](docs/01_signals.md) | How do shifts, scaling, and elementary signals describe an input? |
| 2 | [Systems and LTI properties](docs/02_lti_systems.md) | What can we predict from linearity, time invariance, causality, and stability? |
| 3 | [Impulse response and convolution](docs/03_convolution.md) | How does an LTI system combine delayed copies of its impulse response? |
| 4 | [Laplace transform](docs/04_laplace_transform.md) | How does the transform convert differential equations and convolution into algebra? |
| 5 | [Poles and time-domain responses](docs/05_poles_and_responses.md) | How do pole patterns determine decay, growth, and oscillation? |
| 6 | [Zero-input, zero-state, and total response](docs/06_response_decomposition.md) | Which part comes from stored energy, and which part comes from the applied input? |
| 7 | [Frequency response and Bode plots](docs/07_frequency_response.md) | How do poles and zeros determine which sinusoidal frequencies pass through a system? |
| 8 | [Fourier series and Fourier transform](docs/08_fourier_analysis.md) | How do we describe signals by their frequency content? |
| 9 | [Sampling](docs/09_sampling.md) | When can samples represent a continuous-time signal without ambiguity? |
| 10 | [Cumulative problem-solving guide](docs/10_problem_solving_guide.md) | How do I decide which representation and method to use? |

## Lecture slides

- [Frequency Response and Bode Plots](<slides/EEL 3135 Frequency Response and Bode Plots.pptx>) introduces Bode plots through sinusoidal behavior, first-order building blocks, prediction activities, and one complete pole-zero example.

## How to use each module

For each topic:

1. Read the **prediction** section before doing algebra.
2. Work through the example without hiding intermediate steps.
3. Answer the concept checks without looking at the answers.
4. Explain the result in words: decay rate, oscillation frequency, source of each term, and any stability condition.

Each module now contains:

- a conceptual explanation of why the mathematics works;
- one or more fully worked examples;
- interpretation of the result, not only algebra;
- common mistakes and diagnostic checks;
- practice questions with collapsible solutions.

## Recommended study sequence

Use the notes actively. A productive 45–60 minute session is:

1. **Preview (5 minutes):** read the learning goals and the prediction prompt.
2. **Learn (15 minutes):** follow the explanation and reproduce each derivation on paper.
3. **Practice (20 minutes):** solve the worked example again without looking, then attempt the concept checks.
4. **Explain (5 minutes):** state what the answer means in words or sketch the expected waveform.
5. **Check (5 minutes):** compare units, initial value, final behavior, poles, and signs.

If you can perform the algebra but cannot predict whether a response grows, decays, or oscillates, return to Modules 5 and 6. If you can describe the behavior but cannot calculate it, return to Modules 3 and 4.

## Four representations of the same system

A central goal of the course is learning to move among four complementary views:

| Representation | Best for answering |
|---|---|
| Differential equation | What physical law relates input and output? |
| Impulse response and convolution | How does the system combine delayed input values? |
| Transfer function and poles | What modes and stability properties does the system have? |
| Frequency response and Bode plots | How does the system alter each sinusoidal frequency, and how can we see that behavior at a glance? |

None of these is “the system” by itself. They are different descriptions of the same LTI behavior under the assumptions stated in each module.

## Core concept map

```text
signal operations
      ↓
LTI system properties
      ↓
impulse response and convolution
      ↓
Laplace transform ──→ poles and system modes
      ↓                         ↓
zero-state response       zero-input response
      └──────────── total response ────────────┘
                              ↓
frequency response and Fourier analysis
                              ↓
                           sampling
```

## Notation

- `x(t)`: input signal
- `y(t)`: output signal
- `h(t)`: impulse response
- `X(s)`, `Y(s)`, `H(s)`: Laplace transforms
- `H(jω)`: frequency response, when it exists
- `u(t)`: unit step
- `δ(t)`: unit impulse
- `y_zi(t)`: zero-input response
- `y_zs(t)`: zero-state response

## Suggested software

The reading modules require no software. Optional examples can be checked with Python, NumPy, SciPy, and Matplotlib. Software should verify reasoning rather than replace it.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for corrections and proposed examples.

