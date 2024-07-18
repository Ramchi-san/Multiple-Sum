#Sum of all multiples of 3 and 5 from 0 till a certain number
from typing import List
class MultiplesSum:    

    def main():
        factor_count = input("How many multiples are we trying to find? ").replace(" ", "")
        factors = MultiplesSum.acquiring_factors(factor_count)
        lower_limit = int(input("Enter the lower limit of the range: ").replace(" ", ""))
        upper_limit = int(input("Enter the upper limit of the range: ").replace(" ", ""))
        factor_multiples = MultiplesSum.factor_multiples(factors, lower_limit, upper_limit)
        multiple_sum = MultiplesSum.multiple_adder(factor_multiples)
        MultiplesSum.result_displayer(lower_limit, upper_limit, factor_multiples, multiple_sum)

        
    """
    The acquiring_factors function is about acquiring all the factors that the user
    is considering.
    """
    def acquiring_factors(count : int) -> List[int]:
        result = []
        for i in range(int(count)):
            result.append(int(input(f"Multiple no. {i+1}: ")))
        return result
    
    """
    The factor_multiples function is about finding the multiples of certain list of factors
    storing them in a dictionary with the factors as the key and the list of multiples as the 
    value
    """ 
    def factor_multiples(factors: List[int], lower_limit : int, upper_limit : int):
        multiples = {}
        for number in factors:
            multiples[number] = MultiplesSum.multiple_finder(number, lower_limit, upper_limit)
        return multiples
    

    """
    The multiple_finder function is a utility function of factor_multiples
    which determines the multiples of a number within a certain range.
    """
    def multiple_finder(factor: int, lower_limit : int, upper_limit: int) -> List[int]:
        counter = 1
        result = []
        temp_result = 0
        while int(temp_result) < upper_limit:
            temp_result = factor * counter
            if temp_result >= lower_limit and temp_result <= upper_limit:
                result.append(temp_result)
            counter+=1
        return result
     
    """
    The multiple_adder function is about adding all the multiples within a list
    that is stored in a dictionary except those that are repeating.
    """
    def multiple_adder(multiples):
        temp_copy = multiples.popitem()
        popped_set = set(temp_copy[1])
        for multiple_list in multiples.values():
            popped_set = popped_set.union(set(multiple_list))
        multiples[temp_copy[0]] = temp_copy[1]
        return sum(popped_set)
    
    
    """
    The result_displayer showcases the multiples of certain factors within the range
    and the overall sum of these multiples except duplicates
    """
    def result_displayer(lower_limit, upper_limit, multiples, sum):
        for a_key, a_value in multiples.items():
            print(f"The multiples of {a_key} in the range of {lower_limit} - {upper_limit} are: {a_value}")
        
        print(f"The sum of all these multiples are: {sum}")


MultiplesSum.main()