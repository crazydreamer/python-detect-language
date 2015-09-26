#imports
from multiprocessing.pool import ThreadPool
import difflib
import threading
import time

english = [line.rstrip('\n').lower() for line in open('english.txt')]
spanish = [line.rstrip('\n').lower() for line in open('spanish.txt')]
german = [line.rstrip('\n').lower() for line in open('german.txt')]
french = [line.rstrip('\n').lower() for line in open('french.txt')]
start_time = time.time()
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
            if word in english:
               self.words_in_language += 1.0
        probability = (self.words_in_language / self.word_count) * 100
        print "It is " + str(probability) + "% English\n"
        print("--- %s seconds ---" % (time.time() - start_time))

class spanishThread (threading.Thread):
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
            if word in spanish:
               self.words_in_language += 1.0
        probability = (self.words_in_language / self.word_count) * 100
        print "It is " + str(probability) + "% Spanish\n"
        print("--- %s seconds ---" % (time.time() - start_time))

class germanThread (threading.Thread):
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
            if word in german:
               self.words_in_language += 1.0
        probability = (self.words_in_language / self.word_count) * 100
        print "It is " + str(probability) + "% German\n"
        print("--- %s seconds ---" % (time.time() - start_time))

class frenchThread (threading.Thread):
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
            if word in french:
               self.words_in_language += 1.0
        probability = (self.words_in_language / self.word_count) * 100
        print "It is " + str(probability) + "% French\n"
        print("--- %s seconds ---" % (time.time() - start_time))

# Get sentence
sentence = "Hello world"

# Create new threads
thread1 = englishThread(sentence.lower())
thread2 = spanishThread(sentence.lower())
thread3 = germanThread(sentence.lower())
thread4 = frenchThread(sentence.lower())

# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()


