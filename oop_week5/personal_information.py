value=int(input("จำนานคนที่จะป้อน"))
sum={}
for i in range(value):
    print(f'กรุณากรอกคนที่: {i+1}')
    sum['name']=str(input('กรุณากรอกชื่อ: '))
    sum['nickname']=str(input('กรุณากรอกชื่อเล่น: '))
    sum['id']=str(input('กรุณากรอกรหัสนศ: '))
    sum['hobby']=str(input('กรุณากรอกงานอดิเรก: '))
    sum['color']=str(input('กรุณากรอกสีที่ชอบ: '))
    print(f'ข้อมูลคนที่{i+1}')
    print(f'{sum}')
