import sys, random
import MeCab

MAXGEN = 1000
nonword = "\n"
w1 = w2 = nonword
statetab = {}
m=MeCab.Tagger("-Owakati")
while 1:
    wakatiline = sys.stdin.readline()
    line = m.parse(wakatiline)
    if line == "":
        break
    
    for word in line.split():
        if not statetab.has_key((w1, w2)):
            statetab[(w1, w2)] = []
        statetab[(w1, w2)].append(word)
        w1, w2 = w2, word

if not statetab.has_key((w1, w2)):
    statetab[(w1, w2)] = []
statetab[(w1, w2)].append(nonword)

w1 = w2 = nonword
for i in range(MAXGEN):
    suf = statetab[(w1, w2)]
    r = random.randint(0, len(suf) - 1)
    t = suf[r]
    if t == nonword:
        break
    print t,
    w1, w2 = w2, t
