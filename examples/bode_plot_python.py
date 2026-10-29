"""Plot the exact Bode response of the worked pole-zero example."""

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


def main() -> None:
    # H(s) = 100(s + 10) / [(s + 1)(s + 100)]
    system = signal.TransferFunction(
        [100, 1000],
        [1, 101, 100],
    )

    # Angular frequency in rad/s.
    requested_w = np.logspace(-1, 3, 1000)
    w, magnitude_db, phase_deg = signal.bode(system, w=requested_w)

    fig, (ax_mag, ax_phase) = plt.subplots(
        2,
        1,
        figsize=(8, 6),
        sharex=True,
    )

    ax_mag.semilogx(w, magnitude_db, color="#7030A0", linewidth=2)
    ax_mag.set_ylabel("Magnitude (dB)")
    ax_mag.grid(True, which="both", alpha=0.35)

    ax_phase.semilogx(w, phase_deg, color="#E68A00", linewidth=2)
    ax_phase.set_xlabel("Angular frequency (rad/s)")
    ax_phase.set_ylabel("Phase (deg)")
    ax_phase.grid(True, which="both", alpha=0.35)

    for corner in (1, 10, 100):
        ax_mag.axvline(corner, color="0.5", linestyle="--", linewidth=1)
        ax_phase.axvline(corner, color="0.5", linestyle="--", linewidth=1)

    fig.suptitle("Bode plot of 10(1 + s/10)/[(1 + s)(1 + s/100)]")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
