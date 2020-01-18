def raise_to_power(base_num, power): 
        Result = 1 
        for index in range(power): 
              Result = base_num * Result  

        return Result 


## raise_to_power(3,4)
    
## Breaking it down in simpler terms: 
## Since pow_num is 4, it's looping 4 times
## 3 * 1  = 3          Loop 1
## 3 * 3  = 9          Loop 2 
## 3 * 9  = 27         Loop 3
## 3 * 27 = 81         Loop 3


## Another function that will return the same result

def r_t_power(base_num,power):
        return base_num ** power
