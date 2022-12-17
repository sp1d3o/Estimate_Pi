import random

def estimate_pi(n):
    num_pts_circle = 0
    num_pts_square = 0

    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance < 1:
            num_pts_circle += 1
        num_pts_square += 1

    return 4 * num_pts_circle / num_pts_square

print(estimate_pi(100000000))