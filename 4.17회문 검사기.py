def is_palindrome(s):
 
    def preprocess_string(s):
        return ''.join(char.lower() for char in s if char.isalnum())

 
    def check_palindrome(processed_str):
        stack = []
        for char in processed_str:
            stack.append(char)

        reversed_str = ''
        while stack:
            reversed_str += stack.pop()

        return processed_str == reversed_str

    processed_string = preprocess_string(s)

    return check_palindrome(processed_string)


input_string = input("문자열 입력: ")

result = is_palindrome(input_string)

if result:
    print(f'입력하신 문자열 : "{input_string}" 회문입니다.')
else:
    print(f'입력하신 문자열 : "{input_string}" 회문이 아닙니다.')
