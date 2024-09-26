def safe_root(a, b):
    #Your Answer
        answer = a**(1/ b)
    #Your Answer
        #Your Answer
            answer = "Result is an imaginary number"
        #Your Answer
            answer = -(-a)**(1/ b)
    return answer

print(safe_root(5,6))