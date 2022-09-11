def value(chr):
    return ord(chr) - ord('a')

def reverse_value(chr):
    return ord('z') - ord(chr)

def move(chr, prev_chr):
    import math
    return int(math.fabs(value(chr) - value(prev_chr)))

def reverse_move(chr, prev_chr):
    import math
    return min(value(chr) + reverse_value(prev_chr), value(prev_chr) + reverse_value(chr)) + 1

str = input()
length = len(str)
mn_move = 0
prev_chr = 'a'

for chr in str:
    mv = move(chr, prev_chr)
    rev_mv = reverse_move(chr, prev_chr)
    move_needed = min(mv, rev_mv)
    # print(f'chr = {chr} mv = {mv}  rev_mv = {rev_mv}  move_needed = {move_needed}')
    mn_move += move_needed
    prev_chr = chr

print(mn_move)

