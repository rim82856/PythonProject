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

                if m==1:
                    pass
                elif m==2:
                    pass
                elif m==3:
                    pass
                else:
                    pass
            elif me==2: #단어장 수정
                pass
            elif me==3: #단어장 삭제
                pass
            elif me==4: #돌아가기
                break
            else:
                print("다시 입력해 주세요")
                continue

    elif menu==2: #단어 시험
        print("\n\n"+"-"*15+"  단어 시험  "+"-"*15)
        print("1.영어 시험")
        print("2.한글(뜻) 시험")
        print("3.항목으로 돌아가기")

        while(1):
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
