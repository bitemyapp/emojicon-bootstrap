from BeautifulSoup import BeautifulSoup
import re
import os

emojipath = "e/"
emojicon = []
dumppath = "dump_e.txt"

for emojifile in os.listdir(emojipath):
    emojistring = ''.join(open(emojipath + emojifile, 'r').readlines())
    bs = BeautifulSoup(emojistring)
    # [x + 1 for x in [1, 2, 3, 4, 5]] == [2, 3, 4, 5, 6]
    # [1, 2, 3].extend([4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    emojicon.extend([(emoji.text, emoji.parent.parent.parent.a.text) for emoji in bs('textarea')])
    unique = set(emojicon)

dump = open(dumppath, "w")

for emoji in unique:
    outstring = "Emoji: %s \t Name: %s\n" % (emoji[0], emoji[1])
    print outstring
    # encode returns, does not mutate. Defaults to "ascii"
    # which will make .write() insanely cranky if it gets unicode.
    dump.write(outstring.encode("utf-8"))

dump.close()
