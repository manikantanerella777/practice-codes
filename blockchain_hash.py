import hashlib
def hashGenerator(data):
    res=hashlib.sha256(data.encode())
    return res.hexdigest()
class Block:
    def __init__(self,data,hash,prev_hash):
        self.data=data
        self.hash=hash
        self.prev_hash=prev_hash
class MyBlockchain:
    def __init__(self):
        hashlast=hashGenerator('last_gen')
        hashfirst=hashGenerator('first_gen')
        genesis=Block('gen_data',hashfirst,hashlast)
        self.chain=[genesis]
        
    def add_block(self,data):
        prev_hash=self.chain[-1].hash
        hash=hashGenerator(data+prev_hash)
        block=Block(data,hash,prev_hash)
        self.chain.append(block)

#blch=Block()
blch=MyBlockchain()
blch.add_block('A')
blch.add_block('B')
blch.add_block('C')

for block in blch.chain:
    print(block.__dict__)