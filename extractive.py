import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
    
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords

def remove_punctuation(text):
    punctuation_pattern = r'[^\w\s]'
    text_without_punctuation = re.sub(punctuation_pattern, '', text)
    return text_without_punctuation

def summarize(text,size,style):
    newText=remove_punctuation(text)
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(newText)
    k=0
    if(size=="Small"):
        k=1.8
    if(size=="Medium"):
        k=1.68
    if(size=="Large"):
        k=1.52
    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    sentences = sent_tokenize(text)
    sentenceValue = dict()

    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq

    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    average = int(sumValues / len(sentenceValue))

    summary = ""
    ct=0
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (k * average)):
            sentence = ' '.join(re.sub(r'\s+', ' ', sentence).splitlines())
            
            if(style=="keyPoints"):
                summary += "\u2022 " + sentence + "\n\n"
            elif (style == "paragraph"):

                ct+=1
                summary+=" "+sentence
                if(ct==5):
                    summary+=" \n "
                    summary+="\n"
                    ct=0
    return summary

