import numpy as np

def dh_transform(theta, d, a, alpha):
    ct, st = np.cos(theta), np.sin(theta)
    ca, sa = np.cos(alpha), np.sin(alpha)

    return np.array([
        [ct, -st*ca,  st*sa, a*ct],
        [st,  ct*ca, -ct*sa, a*st],
        [0,      sa,     ca,    d],
        [0,       0,      0,    1]
    ])

def forward_kinematics(d1, theta2, theta3):
    a3 = 0.4     
    d2 = 0.2     

    T1 = dh_transform(0, d1, 0, np.deg2rad(90))
    T2 = dh_transform(theta2, d2, 0, np.deg2rad(-90))
    T3 = dh_transform(theta3 + np.deg2rad(90), 0, a3, 0)

    T = T1 @ T2 @ T3
    position = T[:3, 3]

    return position, T

if __name__ == "__main__":
    pos, T = forward_kinematics(
        d1=0.25,
        theta2=np.deg2rad(20),
        theta3=np.deg2rad(60)
    )

    print("End-effector position:")
    print(pos)
