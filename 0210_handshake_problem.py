import math

def get_participants(handshakes):
    if handshakes == 0: return 0
    return int(math.ceil((math.sqrt(1 + 8 * handshakes) - 1) / 2)) + 1