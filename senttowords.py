#Program for extracting sentences,words and noun phrases from a paragraph
paragraph='Your social networks and your location within them shape the kinds and amount of information that you have access to. Information is distinct from data, in that makes some kind of generalization about a person, thing, or population. Defensible generalizations about society can be either probabilities (i.e., statistics) or patterns (often from qualitative analysis). Such probabilities and patterns can be temporal, spatial, or simultaneous.'
from textblob import TextBlob
tbsentence=TextBlob(paragraph)
sents=tbsentence.sentences
print("\n**SENTENCES**")
for sentindex,sent in enumerate(sents):
    print(f"Sentence {sentindex}:: {sent}")

print("\n**WORDS*")
parawords=tbsentence.words
for wordindex,word in enumerate(parawords):
    print(f"Word {wordindex}:: {word}")

nouns=tbsentence.noun_phrases
print("\n**NOUNS**")
for nounindex,noun in enumerate(nouns):
    print(f"Noun {nounindex}:: {noun}")
print(type(parawords))
print(type(tbsentence))
print(type(sents))
print(type(wordindex))
print(type(nouns))
