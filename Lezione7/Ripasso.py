def find_div_7() -> list:

    nums: list = [number for number in range(2000, 3201) if ((number % 7) == 0) and ((number % 5) != 0)]
    
    return nums

#print(find_div_7())

def fact_num(number: int) -> int:

    fact: int = number
    max: int = number
    counter: int = 1
    m_number: int = number
    while (counter < max):

        m_number *= (fact - counter)
        counter += 1 

    return m_number

#print(fact_num(8))

def fact_list_nums(numbers: list) -> list:
    
    list_fact: list = []
    for number in numbers:

        fact: int = number
        max: int = number
        counter: int = 1
        m_number: int = number
        while (counter < max):

            m_number *= (fact - counter)
            counter += 1

        list_fact.append(m_number)

    return list_fact

#print(fact_list_nums([8, 4]))

