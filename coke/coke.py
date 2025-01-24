def main():
    coin_sum = 0

    while coin_sum < 50:
        coin = int(input("Insert Coin: ").strip())
        if coin == 5 or coin == 10 or coin == 25:
            coin_sum += coin
            if coin_sum < 50:
                print("Amount Due: " + str(50 - coin_sum))
            else:
                print("Change Owed: " + str(coin_sum - 50))
        else:
            print("Amount Due: " + str(50 - coin_sum))

main()
