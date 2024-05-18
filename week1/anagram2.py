def anagram2(input_word, dictionary):
    # random_wordがアルファベットかどうかを判別
    # 英単語なら小文字にそろえる
    if input_word.isalpha():
        input_word = input_word.lower()
    else:
        return ("pls enter English Word (not include hyphen)")

    # 入力された英単語に対してアルファベットごとにカウント
    input_count = {}
    input_count = dict.fromkeys(list("abcdefghijklmnopqrstuvwxyz"), 0)
    # print(input_count)

    # small_word = 'rlsneeesufmrsqyo'
    for letter in input_word:
        if letter in input_count.keys(): #alphabet_code が持つキーの一覧を参照
            input_count[letter] += 1
    # print(input_count)
    # print(input_count["e"])

    # 辞書内の単語に対してアルファベットごとにカウント
    word_count = {}
    word_count = dict.fromkeys(list("abcdefghijklmnopqrstuvwxyz"), 0)
    # print(word_count)

    max_score = 0
    no1_word = ""
    no1s = []
    for word in dictionary:
        # print(word)
        for letter in word:
            if letter in word_count.keys(): #alphabet_code が持つキーの一覧を参照
                word_count[letter] += 1
        # print(word_count)
        # print(word_count["e"])
        flag = 0
        for i in range(97,123):
            if word_count[chr(i)] > input_count[chr(i)]:
                flag += 1
            else:
                flag += 0
        if flag == 0:
            score = ((word_count["a"]+word_count["e"]+word_count["h"]+word_count["i"]+word_count["n"]+word_count["o"]+word_count["r"]+word_count["s"]+word_count["t"])*1
                    +(word_count["c"]+word_count["d"]+word_count["l"]+word_count["m"]+word_count["u"])*2
                    +(word_count["b"]+word_count["f"]+word_count["g"]+word_count["p"]+word_count["v"]+word_count["w"]+word_count["y"])*3
                    +(word_count["j"]+word_count["k"]+word_count["q"]+word_count["x"]+word_count["z"])*4)
            # print(word,score)
            if score > max_score:
                max_score = score
                no1s.clear()
                no1s.append(word)
            elif score == max_score:
                no1s.append(word)
        word_count = dict.fromkeys(list("abcdefghijklmnopqrstuvwxyz"), 0)
    no1_word = no1s[0]
    # print(no1s)
    # print(max_score)
    return no1_word

# words.txtをlist型で読み込み
with open("words.txt") as f:
    dictionary = [s.rstrip() for s in f.readlines()]

# small
with open("small.txt") as f:
    words = [s.rstrip() for s in f.readlines()]
# print(words)

output = []
for word in words:
    no1_word = anagram2(word, dictionary)
    output.append(no1_word)
# print(output)

with open('small_output.txt', 'w') as f:
    for no1_word in output:
        f.write("%s\n" % no1_word)

# medium
with open("medium.txt") as f:
    words = [s.rstrip() for s in f.readlines()]
# print(words)

output = []
for word in words:
    no1_word = anagram2(word, dictionary)
    output.append(no1_word)
# print(output)

with open('medium_output.txt', 'w') as f:
    for no1_word in output:
        f.write("%s\n" % no1_word)

# large
with open("large.txt") as f:
    words = [s.rstrip() for s in f.readlines()]
# print(words)

output = []
for word in words:
    no1_word = anagram2(word, dictionary)
    print(no1_word)
    output.append(no1_word)
# print(output)

with open('large_output.txt', 'w') as f:
    for no1_word in output:
        f.write("%s\n" % no1_word)
