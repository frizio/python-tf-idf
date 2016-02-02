The simplest TF-IDF library imaginable.

Modified by Maurizio Frizio


Add your documents as two-element lists `[doc_name, [list_of_words_in_the_document]]` with `addDocument(doc_name, list_of_words)`.

```python
table.addDocument("foo", ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel"])
```

Get a list of all the `[doc_name, similarity_score]` pairs relative to a list of words by calling `similarities([list_of_words])`. Resulting similarities will always be between `0.0` and `1.0`, inclusive.

```python
table.similarities(["alpha", "bravo", "charlie"])
```

So, for example see tfidf_test.py


*Disclaimer:* This library is a pretty clean example of how TF-IDF operates. However, it's totally unconcerned with efficiency (it's really just an exercise to brush up my Python skills), so you probably don't want to be using it in production. If you're looking for a more heavy-duty Python library to do information retrieval and topic modelling, I'd suggest taking a look at [Gensim](http://radimrehurek.com/gensim/).
