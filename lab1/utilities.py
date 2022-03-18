


def occurences(text_dict):
    list_words = dict()

    for value in text_dict.values():
        for word in value:
            if word in list_words:
                list_words[word] += 1
            else:
                list_words[word] = 1

    return list_words


def average_num(text_dict):
    counter_sentences = len(text_dict)
    total_words = 0

    for key in text_dict:
        total_words += len(text_dict[key])

    return (total_words / counter_sentences)


def median_num(text_dict):
    counter_sentences = len(text_dict)
    total_words = []

    for key in text_dict:
        list=text_dict[key]
        total_words.append(len(list))

    total_words=sorted(total_words)

    if counter_sentences % 2 == 0:
        idx_begin = int(counter_sentences/2)
        idx_end = int(idx_begin-1)
        res = (total_words[idx_begin]+total_words[idx_end])/2
    else:

        res = total_words[int(counter_sentences/2)]

    return res


def top_ngrams(text_dict, K, N):
    tokens = []

    for value in text_dict.values():
        for el in value:
            for letter in el:
                tokens.append(letter)
            sequences = [tokens[i:] for i in range(N)]
    nGram_list = list(zip(*sequences))
    nGrams_dic = {}

    for nGram in nGram_list:
        str_nGram = ''.join(nGram)
        if nGram in nGrams_dic:
            nGrams_dic[nGram] += 1
        else:
            nGrams_dic[nGram] = 1

    print(f"Top-{K} most frequently repeated letter {N}-grams:")

    return nGrams_dic

