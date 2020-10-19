def solution(phone_number):
    return ''.join(['*']*(len(phone_number)-4))+phone_number[-4:]
