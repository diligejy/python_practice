import datetime 
from dataclasses import dataclass 

@dataclass
class User:
    first_name: str
    last_name: str
    
def main():
    number = 800
    print(f"The Number is {number:06}.")
    print(f"{100.233048031:.2f}")
    print(f"{4400000000000:,.2f}")
    print(f"{0.234567:%}")
    greet = "Hi"
    print(f"{greet:_>10}")
    print(f"{greet:>10}")
    print(f"{greet:^10}")
    print(f"{greet:<10}")
    today = datetime.datetime.now()
    print(f"simple date printing: {today}")
    s = f"{today:%H:%M}"
    print(s)
    print(f"Today is {today:%A, %B %d, %Y}")
    print(f"Today is {today:%x}")
    print(f"Today is {today:%X}")
    
    
if __name__ == '__main__':
    main()