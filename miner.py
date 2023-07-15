import string, random, time
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
while True:
    chance = random.randint(0, 9)
    time.sleep(0.07)
    if chance == 0:
        money = random.randint(1, 5)
        prGreen(''.join(random.choice(string.ascii_letters + string.digits) for i in range(32))+'   0.00'+str(money)+'ETH')
    else:
        print(' '+''.join(random.choice(string.ascii_letters + string.digits) for i in range(32))+'   0.000ETH')