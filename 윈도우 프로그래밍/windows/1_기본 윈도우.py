# 처음 만드는 윈도우
from tkinter import *  #'*'-모든 클래스, 함수

"""
def click():
  print("안녕~ 파이썬!")
  lbl_result.config(text="안녕~ 파이썬!")

root = Tk() #Tk 클래스의 인스턴스 생성
root.title("첫 윈도우")
#너비-100pixel, 높이-50p + 뒷숫자는 박스생성 좌표 위치 조정
root.geometry("250x80+500+500")  

# 라벨 생성
# pack() - 가운데 배치(한 줄을 차지함)
Label(root, text="Hello~ Python!!").pack()

# 버튼 생성
# command - 함수에 명령을 내림
Button(root, text="확인", command=click).pack()

# 레이블 생성
lbl_result = Label(root)
lbl_result.pack()

root.mainloop()
"""

#레이아웃(배치) - gird() 함수 
window = Tk()
window.title('배치-grid')
window.geometry("300x300")

Label(window, text="오늘도 좋은하루 되세요!", font=("고딕", 13)).grid(row=0, column=0)
# Label(window, text="오늘도 좋은하루 되세요!").grid(row=1, column=0)
Button(window, text="동", width=5, height=2).grid(row=2, column=0, sticky=E) 
#그리드 쓰면 그 행열의 가운데 정렬 #sticky=E 몇 우측정렬, =W면 좌측 정렬
Button(window, text="서", width=5, height=2).grid(row=2, column=0, sticky=W)
Button(window, text="북", width=5, height=2).grid(row=1, column=0, sticky=N)
Button(window, text="남", width=5, height=2).grid(row=3, column=0, sticky=S)

window.mainloop()