#https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python
def is_prime(n):
    if n <= 0 or n == 1:
        return False
    i = 2
    while (i <= n ** 0.5):
        if n % i == 0:
            return False
        i += 1
    return True

#https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python
def order(sentence):
    sent_list = sentence.split()
    result = ''
    count = 1
    for i in range(0, len(sent_list)):
        for j in range(0 ,len(sent_list)):
            if str(count) in sent_list[j]:
                result+=sent_list[j]+' '
        count+=1
    return result[:-1]
