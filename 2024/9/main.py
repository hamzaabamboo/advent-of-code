from itertools import combinations

raw = open("./input.txt").read()
# raw = open("./test.txt").read()

size = sum([int(n) for n in raw])

cursor = 0
idx = 0
disk = [None for _ in range(size)]

for index in range(len(raw)):
    n = int(raw[index])
    if index % 2 == 0:
        for i in range(n):
            disk[cursor + i] = idx
        idx += 1
    cursor += n

# def frag():
#     write_cursor = len(disk) - 1
#     for index in range(len(disk)):
#         if write_cursor <= index:
#             return
#         if disk[index] is None:
#             print(cursor, write_cursor)
#             disk[index] = disk[write_cursor]
#             disk[write_cursor] = None
#             write_cursor -= 1
#             while disk[write_cursor] == None and write_cursor > index:
#                 write_cursor -= 1

# frag()


def defrag():
    cursor = 0
    write_cursor = len(disk) - 1
    cur_id = disk[len(disk) - 1]
    min_id = size
    while write_cursor > 0:
        cursor = 0
        while (disk[write_cursor] is None) and write_cursor > cursor:
            write_cursor -= 1
        current_block_id = disk[write_cursor]
        current_block_size = 1
        while (
            disk[write_cursor - current_block_size] is current_block_id
            and write_cursor > cursor
        ):
            current_block_size += 1

        min_id = min(current_block_id, min_id)

        while current_block_id > min_id:
            write_cursor -= 1
            while (disk[write_cursor] is None) and write_cursor > cursor:
                write_cursor -= 1
            current_block_id = disk[write_cursor]
            current_block_size = 1
            while (
                disk[write_cursor - current_block_size] is current_block_id
                and write_cursor > cursor
            ):
                current_block_size += 1

        # print("BLOCK ID", write_cursor, current_block_id, current_block_size)

        cursor = 0
        while cursor < len(disk) and cursor < write_cursor and disk[cursor] is not None:
            cursor += 1

        current_space_size = 0
        while (cursor + current_space_size) < len(disk) and disk[
            cursor + current_space_size
        ] is None:
            current_space_size += 1

        while (
            current_block_size > current_space_size
            and cursor < len(disk)
            and cursor < write_cursor
        ):
            cursor += current_space_size
            while cursor < len(disk) and disk[cursor] is not None:
                cursor += 1

            current_space_size = 0
            while (
                (cursor + current_space_size) < len(disk)
                and cursor < write_cursor
                and disk[cursor + current_space_size] is None
            ):
                current_space_size += 1

        if current_block_size <= current_space_size:
            # print(cursor, current_space_size, write_cursor, current_block_size)
            for i in range(current_block_size):
                disk[cursor + i] = current_block_id
                disk[write_cursor - i] = None
        write_cursor -= current_block_size
        # print("".join([str(n) if n is not None else "." for n in disk]))


# print("".join([str(n) if n is not None else "." for n in disk]))
defrag()
# print("".join([str(n) if n is not None else "." for n in disk]))
print(sum([i * disk[i] if disk[i] is not None else 0 for i in range(len(disk))]))
print(size)
print(len(raw))
