#logic:
import time
def checkHand(nums, suits):
    #royal flush
    isFlush = max(suits.values()) == 5
    isStraight = checkStraight(nums)
    hc = highCard(nums)


    if isStraight and isFlush:
        if hc == 14: return (10,) #royal flush
        else: return (9, hc) #straight flush

    #watch out; will return card num 1 for 4 aces
    if max(nums) == 4:
        return (8, nums.index(4) + 1, hc) #four of a kind, card num

    # full house
    if nums.count(3) * nums.count(2) != 0: return (7, nums.index(3) + 1, nums.index(2) + 1)

    if isFlush: return (6, hc) #flush
    if isStraight: return (5, hc) #straight

    # watch out; will return card num 1 for 4 aces
    if max(nums) == 3: return (4,nums.index(3) + 1, hc) # 3 of a kind

    if nums.count(2) == 2: return (3,nums.index(2) + 1, hc) # two pair

    if nums.count(2) == 1: return (2, nums.index(2) + 1, hc) # a pair

    return (1, hc) # high card


def highCard(nums):
    index = len(nums) - 1
    for numCards in nums[::-1]:
        if numCards != 0: return index + 1
        index -= 1


def checkStraight(nums):
    for i in range(4,len(nums)):
        if nums[i-4] * nums[i-3] * nums[i-2] * nums[i-1] * nums[i] != 0: return True #isStraight
    return False


with(open("input_files/p054_poker.txt")) as inputFile:
    for hand in inputFile:
        cards = hand.split(" ")
        p1 = cards[:5]
        p2 = cards[5:]

        p1Nums = list([0]*14)
        p1Suits = dict(zip(["D","S","H","C"], [0]*4)) # [Diamonds Hearts Spades Clubs]
        p2Nums = list([0]*14)
        p2Suits = dict(zip(["D","S","H","C"], [0]*4)) # [Diamonds Hearts Spades Clubs]

        for card in p1:
            num = card[0]
            suit = card[1]
            if num == "A":
                p1Nums[0] += 1
                p1Nums[13] += 1
            if num == "K": p1Nums[12] += 1
            elif num == "Q": p1Nums[11] += 1
            elif num == "J": p1Nums[10] += 1
            elif num == "T": p1Nums[9] += 1
            else: p1Nums[int(num) - 1] += 1
            p1Suits[suit] += 1

        for card in p2:
            num = card[0]
            suit = card[1]
            if num == "A":
                p2Nums[0] += 1
                p2Nums[13] += 1
            if num == "K": p2Nums[12] += 1
            elif num == "Q": p2Nums[11] += 1
            elif num == "J": p2Nums[10] += 1
            elif num == "T": p2Nums[9] += 1
            else: p2Nums[int(num) - 1] += 1
            p2Suits[suit] += 1

            print cards
            print p1
            print p1Nums
            print p1Suits
            p1Hand = checkHand(p1Nums, p1Suits)
            print p1Hand
            print p2
            print p2Nums
            print p2Suits
            p2Hand = checkHand(p2Nums, p2Suits)
            print p2Hand
            time.sleep(100)

def p1Wins(p1Hand, p2Hand):
    index = 0
    while True:
        if p1Hand[index] != p2Hand[index]:
            return p1Hand[index] > p2Hand[index]
        index += 1