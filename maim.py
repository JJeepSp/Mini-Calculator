def add(a,b) :
  ans=a+b
  print("คำตอบของ",str(a),"+",str(b),"=",ans)
  print("----------------------------")

def sub(a,b) :
  ans=a-b
  print("คำตอบของ",str(a),"-",str(b),"=",ans)
  print("----------------------------")

def mul(a,b) :
  ans=a*b
  print("คำตอบของ",str(a),"*",str(b),"=",ans)
  print("----------------------------")

def div(a,b) :
  ans=a/b
  print("คำตอบของ",str(a),"/",str(b),"=",ans)
  print("----------------------------")

while True :
  print("ตัวดำเนินการ")
  print("1 = บวก")
  print("2 = ลบ")
  print("3 = คูณ")
  print("4 = หาร")
  sym=int(input("เลือกตัวดำเนินการ : "))

  if sym==1 :
    a=float(input("ใส่เลขตัวแรก : "))
    print("ตัวดำเนินการ : +")
    b=float(input("ใส่เลขตัวที่สอง : "))
    add(a,b)

  elif sym==2 :
    a=float(input("ใส่เลขตัวแรก : "))
    print("ตัวดำเนินการ : -")
    b=float(input("ใส่เลขตัวที่สอง : "))
    sub(a,b)

  elif sym==3 :
    a=float(input("ใส่เลขตัวแรก : "))
    print("ตัวดำเนินการ : *")
    b=float(input("ใส่เลขตัวที่สอง : "))
    mul(a,b)

  elif sym==4 :
    a=float(input("ใส่เลขตัวแรก : "))
    print("ตัวดำเนินการ : /")
    b=float(input("ใส่เลขตัวที่สอง : "))
    div(a,b)

  else :
    print("กรุณาตรวจสอบข้อมูลให้ถูกต้อง")
    print("----------------------------")
    quit()