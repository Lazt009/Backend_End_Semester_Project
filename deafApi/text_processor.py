# import nltk
# nltk.download('universal_tagset')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
# nltk.download('stopwords')
# nltk.download('punkt')

from nltk.stem import PorterStemmer
from nltk import WordNetLemmatizer
from nltk import word_tokenize , pos_tag
from nltk.corpus import stopwords
# from nltk.tokenize.sonority_sequencing import SyllableTokenizer
# from nltk.util import pr

from googletrans import Translator


def translate_to_english(input_sent):
    translator = Translator()
    trans_sent = translator.translate(input_sent).text
    return trans_sent


def process_text(original_sent):

    print("\n----------- Text Processing -----------\n")
    print("\n\nOriginal Raw Sentence :  ",original_sent)



    # Any language to English Only
    english_trans_sent = translate_to_english(original_sent)
    english_trans_sent = english_trans_sent.lower()
    print("\n\nEnglish Translated Sentence :  ",english_trans_sent)    


        
    # Tokenization
    # print("\n\n------ Tokens ------ ")
    tokens = word_tokenize(english_trans_sent)
    print("\n\nTokens :  ",tokens)



    # POS TAG
    # print("\n\n------ Parts of Speech Tagging ------ ")
    tagg = pos_tag(tokens, tagset='universal')
    print("\n\nPOS TAG :  ",tagg)



    # Reordering by grammer rules
    # print("\n\n------ Reordering Sentences ------\n       by Grammer Rules")
    ps = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

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
    original_sent = "हम शनिवार को अध्ययन करने जा रहे हैं"
    processed_text = process_text(original_sent)
    print("\n\n  Final Processed Text :  ", processed_text,"\n\n\n")

