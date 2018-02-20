import Auth
input_id = input("아이디를 입력해주세요.\n")
if Auth.login(input_id):
    print('Hello, '+input_id)
else:
    print('who are you?')