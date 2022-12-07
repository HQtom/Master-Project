import json
import time
import hashlib
import _json
from transaction import transaction

class Block():
    def __init__(self, p_hash,lastID, trans):
        self.t_stamp = time.asctime(time.localtime(time.time()))
        self.p_hash = p_hash
        self.ID = lastID+1
        self.trans = trans
        self.pow = 0
        self.hash = 0
        self.nonce = 0

    def getHash(self):
       # data = self.t_stamp + self.ID + self.p_hash+self.trans+self.pow

        dc = self.__dict__.copy()
        dc.pop('hash')
        data = json.dumps(dc, sort_keys=True)
        hash = hashlib.sha256()
        hash.update(data.encode("ascii"))
        return hash.hexdigest()


#block = Block(0,0,["rwerwerew"])
#hash1 = block.getHash()
#hash2 = block.getHash()
#print (hash1)
#print (hash2)
#block.trans = {}
#hash2 = block.getHash()
#print (hash2)
