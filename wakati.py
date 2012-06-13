import MeCab
import sys,random

line=sys.stdin.readline()
m=MeCab.Tagger("-Owakati")
print m.parse(line)
