global cnt; cnt=0
global wname; wname=[] #단어장이름 저장 리스트
global name; name=[] #단어장 저장 리스트

while(1):
    print("\n\n"+"-"*15+"  항목  "+"-"*15)
    print("1.단어장 관리")
    print("2.단어 시험")

    menu=int(input("\n항목 선택(숫자만 입력) : ")) #항목 선택

    if menu==1: #단어장 관리

        while(1):
            print("\n\n"+"-"*15+"  단어장 관리  "+"-"*15)
            print("1.단어장 생성")
            print("2.단어장 수정")
            print("3.단어장 삭제")
            print("4.항목으로 돌아가기")

            me=int(input("\n번호 선택(숫자만 입력) : "))

            if me==1: #단어장 생성
                print("\n\n"+"-"*15+"  단어장 생성  "+"-"*15)
                print("1. 직접 입력하기")
                print("2. 엑셀에 있는 데이터 옮겨오기")
                print("3. 항목으로 돌아가기")

                m=int(input("\n번호 선택(숫자만 입력) : "))

                if m==1: #단어장생성-직접 입력

                    print("새로운 단어장의 이름 : ",end='')
                    wname.append(input(""))
                    print("\n- 입력할 영어 단어의 수를 먼저 입력합니다.")
                    print("- 영어를 먼저 일괄입력 합니다.")
                    print("- 영어단어를 그만 입력하고싶으면 기호 #을 입력합니다.")
                    print("- 영어 일괄입력 후에는 입력한 영어 단어에 맞는 한글 뜻을 일괄입력 합니다.")
                    print("- 잘못입력된 내용은 중간에 수정이 불가능하며, \n 후에 단어장 수정 탭을 선택하여 수정이 가능합니다.\n\n")
                    
                    num=int(input("입력할 단어의 수 : ")) #입력된것이 숫자가 아닐 경우 재입력 추가
                    print("단어입력을 시작합니다.")

                    t=[]
                    for i in range(0,num,1): #영어단어 입력                        
                        t.append(input(""))
                        # #을 입력하면 단어입력을 그만두는 기능 구현하기
                    name.insert(cnt,t) #cnt번째 단어장에 단어 저장
                    print()

                    t=[]
                    for i in range(0,num,1): #한글 뜻 입력
                        print(name[cnt][i],end='\t')                   
                        t.append(input(""))
                    name.insert(cnt+1,t) #cnt번째 단어장에 단어 저장

                    cnt+=2
                    break #항목으로 돌아간다

                elif m==2: #단어장생성-엑셀
                    pass
                elif m==3: #돌아가기
                    break
                else:
                    print("다시 입력해 주세요")
                    continue

            elif me==2: #단어장 수정
                print("생성된 단어장")
                print(*wname)

                while(1):
                    print("\n\n1. 영어 수정")
                    print("2. 한글 수정")
                    print("3. 항목으로 돌아가기")

                    m=int(input("\n번호 선택(숫자만 입력) : "))

                    if m==1: #영어 수정
                        pass
                    elif m==2: #한글 수정
                        pass
                    elif m==3: #항목으로 돌아가기
                        break
                    else:
                        print("다시 입력해 주세요")
                        continue

            elif me==3: #단어장 삭제
                pass
            elif me==4: #돌아가기
                break
            else:
                print("다시 입력해 주세요")
                continue

    elif menu==2: #단어 시험

        while(1):
            print("\n\n"+"-"*15+"  단어 시험  "+"-"*15)
            print("1.영어 시험")
            print("2.한글(뜻) 시험")
            print("3.항목으로 돌아가기")

            me=int(input("\n번호 선택(숫자만 입력) : "))

            if me==1: #영어 시험
                pass
            elif me==2: #한글(뜻) 시험
                pass
            elif me==3: #돌아가기
                break
            else:
                print("다시 입력해 주세요")
                continue

    else: #정해진 번호 외의 것이 입력된 경우, 재입력
        print("다시 입력해 주세요")
        continue 
