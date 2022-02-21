from statistics import median
import utilities
def main():
                    
    text = input().replace(",","").replace(":","").replace(";","").replace("?",".").replace("!",".").lower().split(".")

    text_dict = dict()

    for sentence in text:
        text_dict[text.index(sentence)+1] = sentence.split()
        
    list_words = utilities.occurences(text_dict)
    print("List of occurences of words:")

    for key in list_words:
        print(f"{key}:{list_words[key]}")
    utilities.average_num(text_dict)
    print(f"Average number of words in sentences:{utilities.average_num(text_dict)}")
    utilities.median_num(text_dict)
    print(f"Median number of words in sentences:{utilities.median_num(text_dict)}")
    K = 10

    sort_nGram = utilities.top_ngrams(text_dict, 10, 4)

    for tup in sort_nGram:
        K -= 1
        if K == -1:
            return
        for el in tup:
            print(f"{el}", end="")

        print(f":{sort_nGram[tup]}")
        
if __name__ == "__main__":
    main()