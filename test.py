import RandomChar as randchar

# 密码生成器模块
def generate_password(length):
    if length < 4:
        raise ValueError("密码至少4位")
    random_char = randchar.RandomChar()
    password = random_char.uppercase()
    password += random_char.lowercase()
    password += random_char.digit()
    password += random_char.special()
    count = 5
    while count <= length:
        password += random_char.anyone()
        count += 1
    return password

if __name__ == "__main__":
    password_length = int(input("请输入密码长度(8-20)"))
    if password_length < 8 or password_length > 20:
        raise ValueError("密码长度不符合!")
    pwd = generate_password(password_length)
    print(pwd)
