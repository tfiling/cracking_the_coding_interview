def beautifulCoinFlips(coins):
    tails_prefix = []
    count = 0
    for c in coins:
        if c == "T":
            count += 1
        tails_prefix.append(count)
    heads_postfix = [0] * len(coins)
    count = 0
    for i in range(len(coins) -1, -1, -1):
        if coins[i] == "H":
            count += 1
        heads_postfix[i] = count
    return min(tails + heads for tails, heads in zip(tails_prefix, heads_postfix)) - 1

if __name__ == '__main__':
    # print(beautifulCoinFlips("THHHTH"))
    print(beautifulCoinFlips("HHHHH"))
