p = 2
while p <= 100:
    is_prime = True
    for i in range(2, p):
        if p % i == 0:
            is_prime = False
            break # หยุดทำงานในลูป for เมื่อพบว่า p ไม่ใช่จำนวนเฉพาะ
    if is_prime:
        print(p)
    p += 1