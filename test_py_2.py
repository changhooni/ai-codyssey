from flask import Flask

app = Flask(__name__)    

def is_float_try(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def is_int_try(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def power_result(a, b):
    kk = 1

    if b == 0:
        kk = "Error: Division by zero."
        return kk

    if b > 0:
        for _ in range(b):
            kk *= a
        
        if kk == 0:
            kk = "Zero division error"        
        elif is_float_try(kk):
            kk = kk
        return kk    
    else:
        for _ in range(abs(b)):
            kk /= a
        
        if kk == 0:
            kk = "Zero division error"        
        elif is_float_try(kk):
            kk = kk
        return kk 
        

def main():
    try:
        input_num = float(input("Enter Number : "))
        power_num = input("Enter exponent : ")     

        if is_int_try(power_num):
            reslut = 0
            reslut = power_result(input_num, int(power_num))
        else:
            reslut = "Invalid exponent input."
        
    except ValueError:
        reslut = "Invalid number input"
    
    print(f"{reslut}")

    
if __name__ == "__main__":
    main()