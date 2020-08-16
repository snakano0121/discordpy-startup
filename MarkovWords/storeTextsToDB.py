from MarkovWords.PrepareChain import *
import pandas as pd
from tqdm import tqdm
import sys

def storeTextsToDB():

    df = pd.read_csv('data/ChatLog.csv')
    df = df[df["chatlog"]==df["chatlog"]]
    texts = df['chatlog']

    print(len(texts))

    chain = PrepareChain(texts[0])
    triplet_freqs = chain.make_triplet_freqs()
    chain.save(triplet_freqs, True)

    for i in tqdm(texts[1:]):
        chain = PrepareChain(i)
        triplet_freqs = chain.make_triplet_freqs()
        chain.save(triplet_freqs, False)


if __name__ == '__main__':
    storeTextsToDB()