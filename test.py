if name in counts:
    x = counts[name]
else:
    x = 0

# using get method
x = counts.get(name, 0)

