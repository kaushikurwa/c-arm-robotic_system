# Scan Execution Algorithm (Pseudocode)

INITIALIZE SYSTEM
  Load scan parameters
  Calibrate linear and rotational axes
  Move system to home position

FOR each scan step:
  Move linear joint to next position
  Rotate C-Arm to next angle
  Maintain alignment of detector
  Record sensor data

END FOR

STORE collected scan data
RETURN system to home position
