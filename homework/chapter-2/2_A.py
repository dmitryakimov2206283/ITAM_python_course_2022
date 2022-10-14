print("Enter blocks count: ", end="")
blocks_count = int(input())

level_count = 0
blocks_taken = 1
while blocks_count > 0:
    level_count += 1
    blocks_count -= blocks_taken

    if blocks_taken + 1 <= blocks_count:
        blocks_taken += 1
    else:
        blocks_count = 0

print("Levels: ", level_count)