def int32_to_ip(int32):
    parts = [bin(int32)[2:].zfill(32)[i:i+8] for i in range(0, 32, 8)]
    return ".".join([str(int(parts, 2)) for parts in parts])