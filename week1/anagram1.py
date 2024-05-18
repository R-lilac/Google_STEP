def better_solution(random_word, dictionary):
    # random_wordがアルファベットかどうかを判別
    # 英単語なら小文字にそろえる
    if random_word.isalpha():
        random_word = random_word.lower()
        # print(random_word)
    else:
        return "pls enter English Word (not include hyphen)"

    # 入力されたrandom_wordをアルファベット順にする
    list_random_word = sorted(random_word)
    sorted_random_word = ''.join(str(x) for x in list_random_word)
    # print(list_random_word)
    # print(sorted_random_word)

    new_dictionary = []
    for word in dictionary:
        list_word = sorted(word)
        sorted_word = ''.join(str(x) for x in list_word)
        new_dictionary.append((sorted_word, word))
        # print(sorted_word, word)
    # リストを一番目の要素でソート(new_dictionary)
    new_dictionary = sorted(new_dictionary)

    # anagram = 二部探索して元の単語を返す(sorted_random_word, new_dictionary)
    left = 0
    right = len(new_dictionary) - 1
    lower_bound = 0
    list_anagram = []
    while left < right:
        mid = (left + right) // 2
        mid_tuple = new_dictionary[mid]
        mid_sorted_word = mid_tuple[0]
        mid_word = mid_tuple[1]
        # print(mid,mid_tuple,mid_sorted_word,mid_word)
        # print(mid)
        # print(mid_tuple)
        # print(mid_sorted_word)
        # print(mid_word)
        if mid_sorted_word == sorted_random_word:
            right = mid -1
            # print("=",left,right)
        elif mid_sorted_word < sorted_random_word:
            left = mid + 1
            # print("小さい")
        else:
            right = mid - 1
            # print("大きい")

    if left >= right:
        # print(1)
        right = mid + 1
        left = mid - 1
        mid = (left + right) // 2
        mid_tuple = new_dictionary[mid]
        mid_sorted_word = mid_tuple[0]
        mid_word = mid_tuple[1]
        print(mid_sorted_word,sorted_random_word)
        if mid_sorted_word == sorted_random_word:
            lower_bound = mid
            # print(2)
        else:
            lower_bound = mid + 1
            # print(3)

    # print(lower_bound)
    # print(new_dictionary[lower_bound])
    # print(new_dictionary[lower_bound][1])

    while new_dictionary[lower_bound][0] == sorted_random_word:
        anagram_word = new_dictionary[lower_bound][1]
        list_anagram.append(anagram_word)
        lower_bound += 1
        # print(list_anagram)

    if list_anagram :
        return list_anagram
    else :
        return "can't find anagram"

# words.txtをlist型で読み込み
with open("words.txt") as f:
    dictionary = [s.rstrip() for s in f.readlines()]

# 実行用
random_word = input()
print(better_solution(random_word,dictionary))
