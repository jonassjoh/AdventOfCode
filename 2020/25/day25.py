
def solve(door_key, card_key):
    loop_size, key, loop = None, 1, 0

    while loop_size is None:
        loop += 1
        key = (key * 7) % 20201227

        if key == door_key:
            loop_size = loop

    key = 1
    for loop in range(loop_size):
        key = (key * card_key) % 20201227

    return key

input = (11349501, 5107328)
input0 = (17807724, 5764801)

key = solve(*input)

print(f"The handshake is trying to establish {key} as the key.")
