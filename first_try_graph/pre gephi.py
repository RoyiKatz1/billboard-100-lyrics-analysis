import pandas as pd
import re
from collections import Counter
#
def simple_tokenize(text):
    # ממיר את הטקסט לאותיות קטנות ומוציא רק מילים (אותיות ומספרים)
    return re.findall(r'\b\w+\b', text.lower())

# file load
df = pd.read_excel('../data/processed/hot100_translated.xlsx')

all_bigrams = []

for lyrics in df['lyrics_en'].dropna():
    tokens = simple_tokenize(lyrics)
    bigrams_list = list(zip(tokens, tokens[1:]))
    all_bigrams.extend(bigrams_list)

# ספירת התדירות של כל צמד
bigram_freq = Counter(all_bigrams)

# המרת הנתונים ל-DataFrame
bigram_df = pd.DataFrame(bigram_freq.items(), columns=['bigram', 'weight'])

# פיצול עמודת הצמד לשתי עמודות נפרדות ל-GEPHI
bigram_df[['source', 'target']] = pd.DataFrame(bigram_df['bigram'].tolist(), index=bigram_df.index)

# הסרת עמודת הצמד המקורית
bigram_df = bigram_df.drop(columns=['bigram'])

# מיון לפי המשקל בסדר יורד
bigram_df = bigram_df.sort_values(by='weight', ascending=False)

# שמירת הקובץ CSV לייבוא ל-GEPHI
bigram_df.to_csv('bigram_edges.csv', index=False)

print("קובץ הצמדים עם המשקל נשמר בהצלחה כ-'bigram_edges.csv'")

# כל המילים (nodes) הן האיחוד של כל המילים מ-source ו-target
nodes = pd.DataFrame(pd.unique(bigram_df[['source', 'target']].values.ravel()), columns=['Id'])

# אפשר להוסיף עמודה עם התווית (Label) — לרוב פשוט שם המילה
nodes['Label'] = nodes['Id']

# שמירת קובץ ה-nodes ל-GEPHI
nodes.to_csv('bigram_nodes.csv', index=False)

print("קובץ nodes נשמר בהצלחה כ-'bigram_nodes.csv'")
