flowers = ("Rose", "Lily", "Lotus")
print(flowers)
print(flowers[0])
print(flowers[1:])
# flowers[0] = "Red" # TypeError: 'tuple' object does not support item assignment
print(len(flowers))
more_flowers = ("water lily", "Red Rose")
all_flowers = more_flowers + flowers
print(all_flowers)

(rose, lily, lotus) = flowers
print(rose)
print(lily)
print(lotus)s

