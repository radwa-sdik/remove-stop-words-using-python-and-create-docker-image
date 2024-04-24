
#import libraries
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')

#read data
data = pd.read_table(".//paragraphs.txt")

data.head()

#dataframe to list
data.columns = ["string"]
data = data['string'].tolist()

#dunction to remove step words in one sentance
def remove_stop_words(s):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(s)
    data_without_sw = ""
     
    for w in word_tokens:
        if w not in stop_words:
            data_without_sw = data_without_sw + ' ' + w
    
    return data_without_sw.strip()

#remove stepwords from all the data
for i in range(len(data)):
    data[i] = remove_stop_words(data[i])

#function that count every unique word in one string
def count(s):
    word_tokens = word_tokenize(s)
    unique_words = pd.Series(word_tokens).drop_duplicates().tolist()
    for w in unique_words:
        print(f"    {w} : {s.count(w)}")


#example for the first 3 sentances in data and count for their unique words
for i in range(3):
    print(f"\nsentance {i+1}:")
    count(data[i])

