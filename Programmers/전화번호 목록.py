def solution(phone_book):
    book=dict()
    for number in sorted(phone_book):
        for num in range(1,len(number)+1):
            if number[:num] in book:
                return False
        book[number]=number
    return True
