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
| 7 | [Frequency response](docs/07_frequency_response.md) | Why does a sinusoid emerge with the same frequency but a different amplitude and phase? |
| 8 | [Fourier series and Fourier transform](docs/08_fourier_analysis.md) | How do we describe signals by their frequency content? |
| 9 | [Sampling](docs/09_sampling.md) | When can samples represent a continuous-time signal without ambiguity? |

## How to use each module

For each topic:

1. Read the **prediction** section before doing algebra.
2. Work through the example without hiding intermediate steps.
3. Answer the concept checks without looking at the answers.
4. Explain the result in words: decay rate, oscillation frequency, source of each term, and any stability condition.

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

