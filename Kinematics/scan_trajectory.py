import numpy as np

def generate_scan_path(
    angle_start,
    angle_end,
    linear_start,
    linear_end,
    steps
):
    angles = np.linspace(angle_start, angle_end, steps)
    linear_positions = np.linspace(linear_start, linear_end, steps)

    trajectory = []

    for theta, d in zip(angles, linear_positions):
        trajectory.append({
            "linear_displacement": d,
            "rotation_angle": theta,
            "tilt_angle": 0.0
        })

    return trajectory

if __name__ == "__main__":
    scan = generate_scan_path(
        angle_start=np.deg2rad(-90),
        angle_end=np.deg2rad(90),
        linear_start=0.15,
        linear_end=0.35,
        steps=60
    )

    print(f"Generated {len(scan)} scan points")
