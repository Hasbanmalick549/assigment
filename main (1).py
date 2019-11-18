# name
n1 = "babar azam"
n2 = "fakhar zaman"
n3 = "haris sohail"
print("   welcome to the cricket match")
print("  player performense")
# status
print("")
print( n1)
sn1 = input(" status : ");
#run
rn1 = int(input(" run : "));
#ball
b1  = int(input(" ball :"));
st1 = (rn1 * 100) / b1
stt1 = round(st1, 2)
print(" strike rate : " ,stt1)
print("")
print( n2)
sn2 = input(" status : ");
#run
rn2 = int(input(" run : "));
#ball
b2  = int(input(" ball : "));
st2 = (rn2 * 100) /b2
stt2 = round(st2, 2)
print(" strike rate : " ,stt2)
print("")
print( n3)
sn3 = input(" status : ");
#run
rn3 = int(input(" run : "));
#ball
b3  = int(input(" ball : "));
st3 = (rn3 * 100) /b3
stt3 = round(st3, 2)
print(" strike rate : " ,stt3)
print("")
print("")

#     Team performese
print(" Team  performensr")
# total run
trn = (rn1 + rn2 + rn3)
# total over
tb = (b1 + b2 + b3)
tb1 = tb % 6
tb2 = tb1/10
tb3 = tb // 6
tbo = tb3 + tb2

rr = (trn / tb) * 6
trr = round(rr, 2)
# print total run
print("")
print(" total run : ",trn)

# wicket
print("")
if sn1 == "not out" and sn2 == "not out" and sn3 == "not out" :
    print(" wicket 0")
elif sn1 == "out" and sn2 == "not out" and sn3 == "not out" :
    print(" wicket 1")
elif sn1 == "not out" and sn2 == "out" and sn3 == "not out" :
    print(" wicket 1")
elif sn1 == "not out" and sn2 == "not out" and sn3 == "out" :
    print(" wicket 1")
elif sn1 == "out" and sn2 == "out" and sn3 == "not out" :
    print(" wicket 2")
elif sn1 == "not out" and sn2 == "out" and sn3 == "out" :
    print(" wicket 2")
elif sn1 == "out" and sn2 == "not out" and sn3 == "out" :
    print(" wicker 2")
elif sn1 == "out" and sn2 == "out" and sn3 == "out" :
    print(" wicket 3")
#print over
print(" over : ",tbo)
#print run rate
print(" run rate : ",trr)   






