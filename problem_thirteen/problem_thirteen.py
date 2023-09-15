import numpy as np
import random

class VitaminBottle():
    def __init__(self, tot_num_gummies, draw, variance, red_likelihood):
        assert not tot_num_gummies % 2, "Total number of gummies must be even"
        
        self.red = int(tot_num_gummies / 2)
        self.blue = int(tot_num_gummies / 2)
        
        self.draw = draw
        self.variance = variance
        self.red_likelihood = red_likelihood
        
    def pick_one_vitamin(self):
        distribution = np.random.normal(self.draw, self.variance, 1)
        in_hand = int(distribution[0])
        if in_hand <= 0:
            in_hand = 1
        random_sample = random.sample(range(0, self.red + self.blue + 1), min(in_hand, self.red + self.blue))
        reds_i = sum([i <= self.red for i in random_sample])
        if reds_i > 0: 
            seed_i = random.random()
            if len(random_sample) == reds_i:
                self.red -= 1
            elif seed_i <= self.red_likelihood:
                self.red -= 1
            else:
                self.blue -= 1 
        else: 
            self.blue -= 1
            
    def exhaust_reds(self):
        i = 0
        while self.red > 0:
            self.pick_one_vitamin()
            i += 1
        return i
        

def main():
    tot = 0
    for i in range(1000):
        vitamin_c = VitaminBottle(500, 8, 2, 0.9)
        days = vitamin_c.exhaust_reds()
        tot += days
    print(tot / 1000)
    
if __name__ == "__main__":
    main()