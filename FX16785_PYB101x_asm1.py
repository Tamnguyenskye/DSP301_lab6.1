#Nhập tọa độ [Ax, Ay, Bx, By, Cx, Cy]
print('Nhập tọa độ [Ax, Ay, Bx, By, Cx, Cy]:')
Ax, Ay, Bx, By, Cx, Cy = map(float, input().split())
lst = [Ax, Ay, Bx, By, Cx, Cy]
#Tính các góc, cạnh, trọng tâm tam giác ABC
import math
canhAB = math.sqrt((Bx-Ax)**2+(By-Ay)**2)
canhBC = math.sqrt((Bx-Cx)**2+(By-Cy)**2)
canhCA = math.sqrt((Cx-Ax)**2+(Cy-Ay)**2)
a = canhBC
b = canhCA
c = canhAB
AB,BC,CA = [round(elem, 2) for elem in [canhAB,canhBC,canhCA]] #Độ dài cạnh làm tròn để so sánh
gocACB = math.acos((a**2+b**2-c**2)/(2*a*b))
gocABC = math.acos((a**2+c**2-b**2)/(2*a*c))
gocBAC = math.pi - gocACB - gocABC
gocA,gocB,gocC = [round(math.degrees(elem),2) for elem in [gocBAC,gocABC,gocACB]] #Góc làm tròn đơn vị độ
#Goi G(Gx, Gy) la trong tam tam giac ABC
Gx = (Ax + Bx + Cx) / 3
Gy = (Ay + By + Cy) / 3
AG = math.sqrt((Gx - Ax) ** 2 + (Gy - Ay) ** 2)
BG = math.sqrt((Gx - Bx) ** 2 + (Gy - By) ** 2)
CG = math.sqrt((Gx - Cx) ** 2 + (Gy - Cy) ** 2)
#Viết hàm kiểm tra 3 điểm A, B, C có đủ điều kiện hợp thành tam giác ABC hay không
def kiemtra_tamgiac(lst):
  if (AB + BC > CA) and (AB + CA > BC) and (BC + CA > AB):
    return True
  else:
    return False
# Viết hàm tính góc cạnh tam giác
def goccanh_tamgiac(lst):
  goccanh = [AB, BC, CA,gocA, gocB, gocC]
  return goccanh
#Xét xem tam giác ABC thuộc loại tam giác nào
def xet_tamgiac(lst):
  if AB==BC==CA:                            #Xet tam giac deu
    return "ABC là tam giac deu"
  elif AB == CA:                            #Xet tam giac can va vuong/tu tai A
    if gocA == 90.0:
      return "ABC là tam giac vuong can tai dinh A"
    elif gocA > 90.0:
      return "ABC là tam giac tu va can tai dinh A"
    else:
      return "ABC là tam giac can tai A"
  elif AB==BC:                              #Xet tam giac can va vuong/tu tai B
    if gocB == 90.0:
      return "ABC là tam giac vuong can tai dinh B"
    elif gocB > 90.0:
      return "ABC là tam giac tu va can tai dinh B"
    else:
      return "ABC là tam giac can tai B"
  elif BC==CA:                  #Xet tam giac can va vuong/tu tai C
    if gocC == 90.0:
      return "ABC là tam giac vuong can tai dinh C"
    elif gocC > 90.0:
      return "ABC là tam giac tu va can tai dinh C"
    else:
      return "ABC là tam giac can tai C"
  elif gocA == 90.0:               #Xet tam giac vuong, tu tai A
    return "ABC là tam giac vuong tai dinh A"
  elif gocA > 90.0:
    return "ABC là tam giac tu tai dinh A"
  elif gocB == 90.0:               #Xet tai B
    return "ABC là tam giac vuong tai dinh B"
  elif gocB > 90.0:
    return "ABC là tam giac tu tai dinh B"
  elif gocC == 90.0:               #Xet tai C
    return "ABC là tam giac vuong tai dinh C"
  elif gocC > 90.0:
    return "ABC là tam giac tu tai dinh C"
  else:
    return "ABC là tam giac binh thuong"
#Viết hàm dientich_tamgiac(input) để tính diện tích của tam giác ABC
def dientich_tamgiac(lst):
  S = round((c*a*math.sin(gocABC))/2, 2)
  return S
#Viết hàm duongcao_tamgiac(input) để tính độ dài của các đường cao của tam giác ABC
def duongcao_tamgiac(lst):
  p = (a+b+c)/2
  tuso = math.sqrt(p*(p-a)*(p-b)*(p-c))
  dcA = round(2*tuso/a,2)
  dcB = round(2*tuso/b,2)
  dcC = round(2*tuso/c,2)
  return [dcA, dcB, dcC]
#h.Viết hàm tam_tamgiac(input) trả về tọa độ của trọng tâm và trực tâm
#Goi H(Hx, Hy) la truc tam tam giac ABC
def tam_tamgiac(lst):
  mauso = math.tan(gocBAC)+math.tan(gocABC)+math.tan(gocACB)
  Hx = round((Ax*math.tan(gocBAC)+Bx*math.tan(gocABC)+Cx*math.tan(gocACB))/mauso,2)
  Hy = round((Ay*math.tan(gocBAC)+By*math.tan(gocABC)+Cy*math.tan(gocACB))/mauso,2)
  return [round(Gx,2),round(Gy,2),Hx,Hy]
#g.Viết hàm trungtuyen_tamgiac(input) để tính độ dài đường trung tuyến tương ứng của các đỉnh A, B, C
def trungtuyen_tamgiac(lst):
  ttA = round(AG*3/2,2)
  ttB = round(BG*3/2,2)
  ttC = round(CG*3/2,2)
  trungtuyen = [ttA,ttB,ttC]
  return trungtuyen
#f.Viết hàm giaima_tamgiac(lst)
def giaima_tamgiac(lst):
  s1 = "A, B, C hop thanh mot tam giac"
  s2 = "1.So do co ban cua tam giac:"
  s3 = "Chieu dai canh AB: "+ str(AB)
  s4 = "Chieu dai canh BC: "+ str(BC)
  s5 = "Chieu dai canh CA: "+ str(CA)
  s6 = "Goc A:" + str(gocA)
  s7 = "Goc B:" + str(gocB)
  s8 = "Goc C:" + str(gocC)
  s9 = xet_tamgiac(lst)
  s10= "2. Dien tich cua tam giac ABC: " + str(dientich_tamgiac(lst))
  s11= "3. So do nang cao tam giac ABC:"
  s12= "Do dai duong cao tu dinh A: "+ str(duongcao_tamgiac(lst)[0])
  s13= "Do dai duong cao tu dinh B: "+ str(duongcao_tamgiac(lst)[1])
  s14= "Do dai duong cao tu dinh C: "+ str(duongcao_tamgiac(lst)[2])
  s15= "Khoang cach den trong tam tu dinh A:"+ str(round(AG, 2))
  s16= "Khoang cach den trong tam tu dinh B:"+ str(round(BG, 2))
  s17= "Khoang cach den trong tam tu dinh C:"+ str(round(CG, 2))
  s18= "4. Toa do mot so diem dac biet cua tam giac ABC:"
  s19= "Toa do trong tam: ("+str(round(Gx, 2))+","+str(round(Gy, 2))+")"
  s20= "Toa do truc tam: ("+str(tam_tamgiac(lst)[2])+","+str(tam_tamgiac(lst)[3])+")"
  ketqua = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20]
  kq = "\n".join(ketqua)
  if not kiemtra_tamgiac(lst):
    return "A, B, C khong hop thanh mot tam giac"
  else:
    return kq

#Testinhketqua
print(giaima_tamgiac(lst))

