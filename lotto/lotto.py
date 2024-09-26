import random

numbers = []

def lotto():
    result = []
    for i in range(6):
        number = random.randint(0, 44-i)
        result.append(numbers[number])
        before = numbers[-1]
        numbers[-1] = numbers[number]
        numbers[number] = before
    return result
    
def addResults(result, results):
    for number in result:
        results[number] += 1
        
if __name__ == '__main__':
    results = dict()
    for i in range(45):
        numbers.append(i)
        results[i] = 0
    
    for i in range(1000):
        result = lotto()
        addResults(result, results)
    print(results)
    
    