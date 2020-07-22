# 좋은 패스워드를 만드는것은 어려운 일이다. 대부분의 사용자들은 buddy처럼 발음하기 좋고 기억하기 쉬운 패스워드를 원하나,
# 이런 패스워드들은 보안의 문제가 발생한다. 어떤 사이트들은 xvtpzyo 같은 비밀번호를 무작위로 부여해 주기도 하지만,
# 사용자들은 이를 외우는데 어려움을 느끼고 심지어는 포스트잇에 적어 컴퓨터에 붙여놓는다.
# 가장 이상적인 해결법은 '발음이 가능한' 패스워드를 만드는 것으로 적당히 외우기 쉬우면서도 안전하게 계정을 지킬 수 있다. 

# 회사 FnordCom은 그런 패스워드 생성기를 만들려고 계획중이다.
# 당신은 그 회사 품질 관리 부서의 직원으로 생성기를 테스트해보고 생성되는 패스워드의 품질을 평가하여야 한다.
# 높은 품질을 가진 비밀번호의 조건은 다음과 같다.

# 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
# 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
# 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
# 이 규칙은 완벽하지 않다;우리에게 친숙하거나 발음이 쉬운 단어 중에서도 품질이 낮게 평가되는 경우가 많이 있다.

# 입력
# 입력은 여러개의 테스트 케이스로 이루어져 있다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 테스트할 패스워드가 주어진다.

# 마지막 테스트 케이스는 end이며, 패스워드는 한글자 이상 20글자 이하의 문자열이다.
# 또한 패스워드는 대문자를 포함하지 않는다.

# 출력
# 각 테스트 케이스를 '예제 출력'의 형태에 기반하여 품질을 평가하여라.

# 예제 입력 1           예제 출력 1
# a                     <a> is acceptable.
# tv                    <tv> is not acceptable.
# ptoui                 <ptoui> is not acceptable.
# bontres               <bontres> is not acceptable.
# zoggax                <zoggax> is not acceptable.
# wiinq                 <wiinq> is not acceptable.
# eep                   <eep> is acceptable.
# houctuh               <houctuh> is acceptable.
# end

def is_vowel(pw, ls):
    vowel_cnt = 0
    for i in pw:
        if i in ls:
            vowel_cnt += 1
    if vowel_cnt == 0:
        return False
    return True

def three_in_a_row(pw, ls):
    vow = 0
    cons = 0
    i = 0
    while i < len(pw):
        if pw[i] in ls:
            cons = 0
            vow += 1
        else:
            vow = 0
            cons += 1
        if vow >= 3 or cons >= 3:
            return False
        i += 1
    return True

def two_in_a_row(pw, ls):
    cnt = 0
    i = 1
    while i < len(pw):
        if pw[i] != 'e' and pw[i] != 'o':
            if pw[i] == pw[i - 1]:
                cnt += 1
            else:
                cnt = 0    
        if cnt >= 1:
            return False
        i += 1
    return True
            
vowel = ['a','e','i','o','u']

while 1:
    pw = input()
    if pw == 'end':
        break
    if not is_vowel(pw, vowel) or not three_in_a_row(pw, vowel) or not two_in_a_row(pw, vowel):
        print('<'+pw+'> is not acceptable.')
        continue
    else:
        print('<'+pw+'> is acceptable.')