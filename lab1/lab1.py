import utilities
import constant


def main():
    print("Enter K:")

    K = input()
    if K == '':
        K = constant.CONSTANT_K
    else:
        K = int(K)

    print("Enter N:")

    N = input()
    if N == '':
        N = constant.CONSNANT_N
    else:
        N = int(N)

    print(f"{K} {N}")

    text = input().replace(",", "").replace(":", "")\
        .replace(";", "").replace("?", ".")\
        .replace("!", ".").lower().split(".")

    print(len(text))

    text_dict = dict()

    for sentence in text:
        text_dict[text.index(sentence) + 1] = sentence.split()
        
    list_words = utilities.occurences(text_dict)
    print("List of occurences of words:")

    for key in list_words:
        print(f"{key}:{list_words[key]}")

    utilities.average_num(text_dict)
    print(f"Average number of words in sentences:{utilities.average_num(text_dict)}")
    utilities.median_num(text_dict)
    print(f"Median number of words in sentences:{utilities.median_num(text_dict)}")

    not_sort_nGram = utilities.top_ngrams(text_dict, K, N)

    sort_nGram = dict(sorted(not_sort_nGram.items(), key=lambda item: item[1], reverse=True))

    for tup in sort_nGram:
        K -= 1
        if K == -1:
            return
        for el in tup:
            print(f"{el}", end="")

        print(f":{sort_nGram[tup]}")


if __name__ == "__main__":
    main()
