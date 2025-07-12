from sys import stdin
from heapq import heappush, heappop

ask, bid = [], []
sask, sbid, sprice = "-", "-", "-"

class Stock:
    def __init__(self, p, c, t): self.p = p; self.c = c; self.t = t
    def string(self): return f"{self.p}"
    def __gt__(self, o): return self.p > o.p if self.t == "sell" else self.p < o.p

def manejar(p, c, t):
    global sask, sbid, sprice
    heappush(bid if t == "buy" else ask, Stock(p, c, t))
    while ask and bid and bid[0].p >= ask[0].p:
        cb, ca = bid[0].c, ask[0].c
        sprice = ask[0].string()
        bid[0].c -= ca
        ask[0].c -= cb
        if ask[0].c <= 0: heappop(ask)
        if bid[0].c <= 0: heappop(bid)
    sask = ask[0].string() if ask else "-"
    sbid = bid[0].string() if bid else "-"
    print(sask+ " " + sbid + " " + sprice)

def main():
    global ask, bid, sask, sbid, sprice
    while (linea := stdin.readline()):
        t = int(linea)
        for _ in range(t):
            ask.clear(); bid.clear()
            sask = sbid = sprice = "-"
            n = int(stdin.readline())
            for _ in range(n):
                arr = stdin.readline().split()
                manejar(int(arr[4]), int(arr[1]), arr[0])

main()
