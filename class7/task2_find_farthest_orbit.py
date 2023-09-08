def find_farthest_orbit(orbits: list[tuple]) -> tuple:
    max_orbit_area = orbits[0][0] * orbits[0][1]
    max_orbit = orbits[0]
    for orbit in orbits:
        curr_orbit_area = 1
        for i in range(2):
            curr_orbit_area *= orbit[i]
        if curr_orbit_area > max_orbit_area:
            max_orbit_area = curr_orbit_area
            max_orbit = orbit
    return max_orbit

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
            