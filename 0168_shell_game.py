def find_the_ball(start, swaps):
    ball_location = start

    for swap in swaps:
        if ball_location in swap:
            ball_location = swap[0] if ball_location == swap[1] else swap[1]

    return ball_location