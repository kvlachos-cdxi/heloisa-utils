def insert_decimal_after_second_digit(num):
    num_str = str(num)
    if len(num_str) <= 2:
        # If the number has 2 or fewer digits, just prefix with '0.'
        return f"0.{num_str}"
    return num_str[:2] + '.' + num_str[2:]

if __name__ == "__main__":
    
    # Examples
    print(insert_decimal_after_second_digit(342342342))  # 34.2342342
    print(insert_decimal_after_second_digit(3243))       # 32.43
    print(insert_decimal_after_second_digit(99))         # 0.99