class Base:
    num_base_call = 0
    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_call+=1

class Left(Base):
    num_left_call = 0
    def call_me(self):
        Base.call_me(self)
        print("Calling method on Left Class")
        self.num_left_call+=1

class Right(Base):
    num_right_call = 0
    def call_me(self):
        Base.call_me(self)
        print("Calling method on Right Class")
        self.num_right_call+=1

class Derived(Left, Right):
    num_sub_calls = 0
    def call_me(self):
        Left.call_me(self)
        Right.call_me(self)
        print("Calling method on Derived class")
        self.num_sub_calls += 1

if __name__ == '__main__':
    d = Derived()
    d.call_me()