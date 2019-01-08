#logic:
import time


# ATTEMPT 1

def checkHand(nums, suits):
    #royal flush
    isFlush = max(suits.values()) == 5
    isStraight = checkStraight(nums)
    hc = highCard(nums)

    # in this hand, the high card is always highest element of hand
    if isStraight and isFlush:
        if hc == 13: return (10,) #royal flush
        else: return (9, hc) #straight flush

    # returns 13 for 4 aces by reversing list (finds first case of a 4)
    if max(nums) == 4:
        return (8,  nums.index(4) + 2) #four of a kind, card num

    # full house
    if nums.count(3) * nums.count(2) != 0: return (7, nums.index(3) + 2, nums.index(2) + 2)

    if isFlush: return (6, hc) #flush
    if isStraight: return (5, hc) #straight


    if max(nums) == 3: return (4, len(nums) - nums[::-1].index(3) , hc) # 3 of a kind

    if nums.count(2) == 2: return (3,len(nums) - nums[::-1].index(2), nums.index(2) + 2, hc) # two pair

    if nums.count(2) == 1: return (2, nums.index(2) + 2, hc) # a pair

    return (1,hc) # high card


def highCard(nums):
    index = len(nums) - 1
    for numCards in nums[::-1]:
        if numCards != 0: return index + 1
        index -= 1


def checkStraight(nums):
    for i in range(4,len(nums)):
        if nums[i-4] * nums[i-3] * nums[i-2] * nums[i-1] * nums[i] != 0: return True #isStraight
    return False


def p1Wins(p1Hand, p2Hand,p1Nums, p2Nums):
    index = 0
    while index < len(p1Hand):
        if p1Hand[index] != p2Hand[index]:
            return p1Hand[index] > p2Hand[index]
        index += 1
    # if we reach this point, both hands are identical besides high card;
    # simply traverse list backwards and find first difference
    for x,y in zip(p1Nums[::-1], p2Nums[::-1]):
        if x != y: return x > y


p1win_count = 0

with(open("input_files/p054_poker.txt")) as inputFile:
    for hand in inputFile:
        hand = hand.replace("\n", "")
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
                p1Nums[12] += 1
            elif num == "K": p1Nums[11] += 1
            elif num == "Q": p1Nums[10] += 1
            elif num == "J": p1Nums[9] += 1
            elif num == "T": p1Nums[8] += 1
            else: p1Nums[int(num) - 2] += 1
            p1Suits[suit] += 1

        for card in p2:
            num = card[0]
            suit = card[1]
            if num == "A":
                p2Nums[12] += 1
            elif num == "K": p2Nums[11] += 1
            elif num == "Q": p2Nums[10] += 1
            elif num == "J": p2Nums[9] += 1
            elif num == "T": p2Nums[8] += 1
            else: p2Nums[int(num) - 2] += 1
            p2Suits[suit] += 1

#        print("cards: ", cards)
#        print ("p1 cards: ", p1)
#        print ("p1nums: ", p1Nums)
#        print ("p1suits: ", p1Suits)
        p1Hand = checkHand(p1Nums, p1Suits)
#        print ("p1hand", p1Hand)
#        print ("p2 cards: ", p2)
#        print ("p2 nums: ", p2Nums)
#        print ("p2suits: ", p2Suits)
        p2Hand = checkHand(p2Nums, p2Suits)
#        print ("p2 hand: ", p2Hand)

 #       print ("p1 wins: ", p1Wins(p1Hand,p2Hand,p1Nums,p2Nums))
#        print("-*" * 40)
#        time.sleep(1)
        if p1Wins(p1Hand, p2Hand, p1Nums, p2Nums):
            p1win_count += 1

print(p1win_count)

    
    
