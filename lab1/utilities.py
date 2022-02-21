from statistics import median


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
    counter_sentences = 0
    total_words = 0

    for key in text_dict:
        counter_sentences += 1
        total_words += len(text_dict[key])

    return (total_words / counter_sentences)


def median_num(text_dict):
    med_num = []

    for key in text_dict:
        med_num.append(len(text_dict[key]))

    return (median(med_num))
    print(f"Median number of words in sentences:{median(med_num)}")
    return


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

    return (dict(sorted(nGrams_dic.items(), key=lambda item: item[1], reverse=True)))
