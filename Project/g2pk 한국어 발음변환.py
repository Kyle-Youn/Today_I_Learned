'''
pip install g2pk
'''

from g2pk import G2p

g2p = G2p()
text = "어디선가 뭔가 많이 다가와 미지에 세상 그곳에 나를 데려가줘"
phonemes = g2p(text)
print(phonemes)