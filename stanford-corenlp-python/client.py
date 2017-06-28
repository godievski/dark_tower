import json
import nltk
#from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import pprint
#from nltk.stem import SnowballStemmer
from corenlp import *

# class StanfordNLP:
#     def __init__(self):
#         self.server = ServerProxy(JsonRpc20(),
#                                   TransportTcpIp(addr=("127.0.0.1", 8085)))
    
#     def parse(self, text):
#         return json.loads(self.server.parse(text))

#stemmer = SnowballStemmer('english')

nlp = StanfordCoreNLP()
#text="The man in black fled across the desert, and the gunslinger followed. The desert was the apotheosis of all deserts, huge, standing to the sky for what looked like eternity in all directions. It was white and blinding and waterless and without feature save for the faint, cloudy haze of the mountains which sketched themselves on the horizon and the devil-grass which brought sweet dreams, nightmares, death. An occasional tombstone sign pointed the way, for once the drifted track that cut its way through the thick crust of alkali had been a highway. Coaches and buckas had followed it. The world had moved on since then. The world had emptied."
text="Barack Obama was born in Hawaii.  He is the president. Obama was elected in 2008."
result = json.loads(nlp.parse(text))

tokenized_sentences = nltk.sent_tokenize(text)
tokenized_in_words=[nltk.word_tokenize(sentence) for sentence in tokenized_sentences]



for block_to_replace in result["coref"]:
	sentence_index=block_to_replace[0][1][1]
	word_index=block_to_replace[0][1][2]
	replace_sent=block_to_replace[0][1][0]
	word_to_replace=tokenized_in_words[sentence_index][word_index]

	if not word_to_replace.istitle():
		continue


	print 'word_to_replace: ',word_to_replace


	for i,lines_to_replace in enumerate(block_to_replace):
		#getting the important word to
		#index of the sentence
		ix_sent=lines_to_replace[0][1]
		sent_to_replace=lines_to_replace[0][0]
		tokenized_sentences[ix_sent]=tokenized_sentences[ix_sent].replace(sent_to_replace,word_to_replace)
		
		#print i,' ',lines_to_replace
	#replace the replacer lol
	tokenized_sentences[sentence_index]=tokenized_sentences[sentence_index].replace(replace_sent,word_to_replace)
	print

final_text=' '.join(tokenized_sentences)
print final_text

sents_token=[nltk.word_tokenize(sentence) for sentence in tokenized_sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in sents_token]   
print tagged_sentences