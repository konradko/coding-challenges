def get_asteroid_collision(asteroids: list[int]) -> list[int]:
    remaining_asteroids = []

    for asteroid in asteroids:
        while remaining_asteroids and asteroid < 0 and remaining_asteroids[-1] > 0:
            # Collision with top asteroid happens
            collision_result = remaining_asteroids[-1] + asteroid

            if collision_result <= 0:
                # Top asteroid is destroyed
                remaining_asteroids.pop()

            if collision_result >= 0:
                # Current astroid is destroyed
                break
        else:
            remaining_asteroids.append(asteroid)

    return remaining_asteroids
