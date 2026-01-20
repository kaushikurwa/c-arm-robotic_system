# Denavit-Hartenberg Parameters 3-DOF C-Arm Robot

This C-Arm robot is designed with three degrees of freedom to perform
controlled scanning motion around a stationary object. The configuration
matches the mechanical structure described in the project report.

## Joint Configuration

| Joint | Type        | Function |
|-----|------------|----------|
| J1  | Prismatic  | Linear positioning of the C-Arm structure |
| J2  | Revolute   | Tilting / angular alignment |
| J3  | Revolute   | Rotational sweep around the object |

This joint selection provides sufficient workspace coverage while
maintaining mechanical simplicity.

## Coordinate Frame Assignment

Each joint frame is assigned following the standard DH convention.
The Z-axis of each frame corresponds to the joint motion axis.

## DH Parameter Table (Standard DH Convention)

| Link | θ (theta)        | d (offset) | a (length) | α (alpha) |
|-----|------------------|------------|------------|-----------|
| 1   | 0                | d₁ (var)   | 0          | +90°      |
| 2   | θ₂ (var)         | d₂ (const) | 0          | −90°      |
| 3   | θ₃ + 90° (var)   | 0          | a₃         | 0°        |

Where:
- d₁ represents the linear displacement of the C-Arm
- θ₂ controls angular alignment
- θ₃ performs rotational scanning around the object

## Notes
- Joint limits are enforced in software to prevent over-travel
- Parameters are derived from the physical prototype dimensions
- The model supports repeatable and predictable scanning motion
