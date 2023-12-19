def name_file(fmt, nbr, start):
    if not isinstance(nbr, int) or nbr <= 0 or nbr != int(nbr):return []
    if not isinstance(start, int):return []

    if '<index_no>' not in fmt:
        return [fmt] * nbr
    return [fmt.replace('<index_no>', str(start + i)) for i in range(nbr)]