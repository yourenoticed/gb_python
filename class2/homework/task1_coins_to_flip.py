def coins_to_flip(coins: list) -> int:
    heads = 0
    tails = 0
    for coin in coins:
        if coin == 0:
            tails += 1
        elif coin == 1:
            heads += 1
            
    return min(heads, tails)

coins = [1, 0, 1, 1, 0]
print(coins_to_flip(coins))