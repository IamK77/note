class Father():

    character = 'irascible'     # 父亲性格暴躁

    def __init__(self):
        self.iq = 100

    def printf(self):
        print('i am a typist')  # 父亲是个打字员


class Mother():
    
    character = 'gentle'        # 母亲性格温柔

    def __init__(self):
        self.iq = 120

    def printf(self):
        print('i am a singer')   # 母亲是个歌手


class Son(Mother, Father):
    
        def __init__(self):
            self.iq = 50
    
        def fire(self):
            print('i am a soldier')  # 儿子是个士兵


f = Father()
m = Mother()
s = Son()

print(f.character)
print(m.character)
print(s.character)

f.printf()
m.printf()
s.printf()