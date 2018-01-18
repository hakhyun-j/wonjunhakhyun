input_id=input("아이디를 입력해주세요.\n")
input_pw=input("비밀번호를 입력해주세요.\n")
def login(_id,_pw):
    members=["wonchung5461","kimrafa4441","brianshin7022","hakhyunj6340"]
    for member in members:
        if member==_id+_pw:
            return True
    return False

if login(input_id,input_pw):
    print('Hello, '+input_id)
else:
    print('Who are you?')
x=input()
