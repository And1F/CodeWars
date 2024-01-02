def is_right_angle(a, b, c):
    vector_ab = [b[0] - a[0], b[1] - a[1]]
    vector_bc = [c[0] - b[0], c[1] - b[1]]    
    return vector_ab[0] * vector_bc[0] + vector_ab[1] * vector_bc[1] == 0

def count_rect_triang(points):
    points = list(set(tuple(point) for point in points))
    count = 0
    n = len(points)
    
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if is_right_angle(points[i], points[j], points[k]):
                    count += 1
                elif is_right_angle(points[i], points[k], points[j]):
                    count += 1
                elif is_right_angle(points[j], points[i], points[k]):
                    count += 1
    return count