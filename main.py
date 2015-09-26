#imports
from multiprocessing.pool import ThreadPool
import difflib
import english
import threading

symbols = "!$%&/()=?|@#'\\\",[]{-_;.:}1234567890<>"

class englishThread (threading.Thread):
    def __init__(self, sentence):
        threading.Thread.__init__(self)
        self.sentence= sentence
        self.words_in_language = 0.0
        self.words = sentence.split()
        self.word_count = len(self.words)
    def run(self):
        words = self.sentence.split()
        for word in words:
            for i in range(0, len(symbols)):
              word = word.replace(symbols[i], "")
            res = difflib.get_close_matches(word, english.words)
            if len(res) > 0 and word in res:
               self.words_in_language += 1.0
        probability = (self.words_in_language / self.word_count) * 100
        print "It is " + str(probability) + "% English"

class spanishThread (threading.Thread):
    def __init__(self, sentence):
        threading.Thread.__init__(self)
        self.sentence= sentence
    def run(self):
        print "TODO Spanish"

# Get sentence
sentence = raw_input("Enter your text\n")

# Create new threads
thread1 = englishThread(sentence.lower())
thread2 = spanishThread(sentence.lower())

# Start new Threads
thread1.start()
thread2.start()

