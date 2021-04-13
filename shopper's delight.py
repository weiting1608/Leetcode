# Shopper's delight - IBM
# A shopaholic has buy a pair of jeans, a pair of shoes, a skirt, and a top with budgeted dollars.
# Given a list of prices for each kind of product, determine how many different combinations can be bought.
# If required, all budgeted dollars can be spent.

# input: jeans, shoes, skirts, tops: list of integer, budget

jeansAndShoes = []
for jean in jeans:
    for shoe in shoes:
        jeansAndShoes.append(jean+shoe)

skirtsAndTops = []
for skirt in skirts:
    for top in tops:
        skirtsAndTops.append(skirt+top)

jeansAndShoes.sort()
skirtsAndTops.sort(reverse=True)

res = 0
limit = 0

for cost in jeansAndShoes:
    remaining = budget - cost
    while limit < len(skirtsAndTops) and skirtsAndTops[limit] > remaining:
        limit += 1

    if limit == len(skirtsAndTops):
        break

    res += len(skirtsAndTops) - limit

return res
