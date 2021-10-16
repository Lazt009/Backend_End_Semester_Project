from nltk.stem import PorterStemmer
# import nltk
from nltk import WordNetLemmatizer
from nltk import word_tokenize , pos_tag
from nltk.corpus import wordnet,stopwords
from nltk.tokenize.sonority_sequencing import SyllableTokenizer
from nltk.util import pr


def process_text(original_sent):
    print("\n----------- Text Processing -----------\n")
    lemmatizer = WordNetLemmatizer()
    original_sent = original_sent.lower()
    print("\n\nOriginal Sentence :  ",original_sent)


    # Tokenization
    # print("\n\n------ Tokens ------ ")
    tokens = word_tokenize(original_sent)
    print("\n\nTokens :  ",tokens)


    # POS TAG
    # print("\n\n------ Parts of Speech Tagging ------ ")
    tagg = pos_tag(tokens, tagset='universal')
    print("\n\nPOS TAG :  ",tagg)


    # Reordering by grammer rules
    # print("\n\n------ Reordering Sentences ------\n       by Grammer Rules")
    ps = PorterStemmer()
    verb_string = ""
    reordered_sent = ""
    for tag in tagg:
        if(tag[1] == 'VERB'):
            verb_string +=(lemmatizer.lemmatize(tag[0]) + " ")
        else:
            reordered_sent+=(tag[0] + " ")

    reordered_sent += verb_string
    print("\n\nReordered by Grammer Rules :  ",reordered_sent)


    # Removing Stopwords
    stop_words = set(stopwords.words('english'))
    processed_sent = ""
    for word in reordered_sent.split():
        if word not in stop_words:
            processed_sent+=(word + " ")
    print("\n\nRemoved Stop Words :  ",processed_sent)
    print("\n\n\n---------------------------------------\n")
    return processed_sent

if __name__ == '__main__':
    original_sent = "A man is singing a song in the hospital"
    processed_text = process_text(original_sent)
    print("\n\n------- Final Processed Test -------", processed_text)

    