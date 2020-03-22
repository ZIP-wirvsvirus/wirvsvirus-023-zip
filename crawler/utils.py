#!/usr/bin/env python3
import re
from germalemma import GermaLemma
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import nltk

nltk.download('stopwords')


class Keywordgeneration:
    def __init__(self):
        self.lemmatizer = GermaLemma()

        ##Creating a list of stop words and adding custom stopwords
        self.own_stopwords = ["sollen", "können", "würde"]
        self.stop_words = set(stopwords.words("german"))
        self.stop_words = self.stop_words.union(self.own_stopwords)

        self.corona_keywords = ['corona', 'coronavirus', 'covid19', 'covid', 'hamsterkauf', 'impfstoff', 'medikamente',
                                'medikament', 'impfung', 'ausgangssperre']

    def sort_coo(self, coo_matrix):
        tuples = zip(coo_matrix.col, coo_matrix.data)
        return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)

    def extract_topn_from_vector(self, feature_names, sorted_items, topn=10):
        """get the feature names and tf-idf score of top n items"""

        # use only topn items from vector
        sorted_items = sorted_items[:topn]

        score_vals = []
        feature_vals = []

        # word index and corresponding tf-idf score
        for idx, score in sorted_items:
            # keep track of feature name and its corresponding score
            score_vals.append(round(score, 3))
            feature_vals.append(feature_names[idx])

        # create a tuples of feature,score
        # results = zip(feature_vals,score_vals)
        results = {}
        for idx in range(len(feature_vals)):
            results[feature_vals[idx]] = score_vals[idx]

        return results

    def normalizeText(self, text):

        # Remove punctuations
        text = re.sub('[^a-zA-ZäöüßÄÖÜ]', ' ', text)

        # Convert to lowercase
        text = text.lower()

        # remove tags
        text = re.sub("&lt;/?.*?&gt;", " &lt;&gt; ", text)

        # remove special characters and digits
        text = re.sub("(\\d|\\W)+", " ", text)

        ##Convert to list from string
        text = text.split()

        # Lemmatisation
        text = [self.lemmatize(word) for word in text if not word in self.stop_words]
        text = " ".join(text)

        text = text.lower()

        return text

    def lemmatize(self, word):
        return self.lemmatizer.find_lemma(word, 'N')

    def generateKeyWords(self, strs):
        keywordList = []
        corpus = []

        for i in range(0, len(strs)):
            corpus.append(self.normalizeText(strs[i]))

        cv = CountVectorizer(stop_words=self.stop_words, max_features=10000, ngram_range=(1, 3))
        X = cv.fit_transform(corpus)

        tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
        tfidf_transformer.fit(X)

        # get feature names
        feature_names = cv.get_feature_names()

        for i in range(0, len(strs)):
            # fetch document for which keywords needs to be extracted
            doc = corpus[i]
            # generate tf-idf for the given document
            tf_idf_vector = tfidf_transformer.transform(cv.transform([doc]))
            # sort the tf-idf vectors by descending order of scores
            sorted_items = self.sort_coo(tf_idf_vector.tocoo())
            # extract only the top n; n here is 10
            keywords = self.extract_topn_from_vector(feature_names, sorted_items, 5)

            # check if important corona keyword is used in text
            for t in self.corona_keywords:
                if t in doc:
                    keywords[t] = 1

            keywordList.append(keywords)

        return keywordList
