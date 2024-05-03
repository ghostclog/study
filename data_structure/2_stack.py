class stack:
    def __init__(self): # 생성 함수
        self.items= []

    def push(self,data):
        self.items.append(data)
    
    def pop(self):
        try:
            return self.items.pop()
        except:
            return "stack is empty"
        
    def top(self):
        try:
            return self.items[-1]
        except:
            return "stack is empty"
        
    def len(self):
        return len(self.items)
    
#####

def ex1(txt):   # 괄호 짝 맞추기
    temp = stack()
    for i in txt:
        if(i == "("):
            temp.push("(")
        elif(i==")"):
            if(temp.pop() == "stack is empty"):
                print("error. text is wrong")
                break
            
    if(temp.len() != 0):
        print("error. text is wrong")
    else:
        print("text is perfect")

###

def ex2(nums_and_ops): # 스택을 이용한 계산기
    n_a_o = nums_and_ops.split()
    ops_list = ["+","-","/","*"] # 사칙 연산 리스트
    temp_stack = stack()    # 전위를 후위로 변경하기 위한 스택
    temp_list = []

    for i in n_a_o:
        if(i in ops_list):
            for j in temp_stack.items:
                if((i == "+" or i == "-") and (j == "*" or j == "/")):  # 만약에 i가 +-이고, 스택에 들어있는 연산자가 */일때.
                    temp_list.append(temp_stack.pop())                  # 연산자 우선 순위에 의해 스택의 내용물을 빼 줌.
                else:
                    break                                               # 그렇지 않은 경우에는 무시
            temp_stack.push(i)
        else:
            temp_list.append(i)

    for i in temp_stack.items:
        temp_list.append(temp_stack.pop())

    num_stack = stack() # 결과를 도출시키기 위한 스택

    for i in temp_list:
        if(i == "+"):
            a = int(num_stack.pop())
            b = int(num_stack.pop())
            num_stack.push(a+b)
        elif(i == "-"):
            a = int(num_stack.pop())
            b = int(num_stack.pop())
            num_stack.push(a-b)
        elif(i == "*"):
            a = int(num_stack.pop())
            b = int(num_stack.pop())
            num_stack.push(a*b)
        elif(i == "/"):
            a = int(num_stack.pop())
            b = int(num_stack.pop())
            try:
                num_stack.push(a//b)
            except:
                return "wrong ops and nums"
        else:
            num_stack.push(i)

    return int(num_stack.pop())
