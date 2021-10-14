def luas_persegi(panjang,lebar):
    print("luas persegi")
    luaspsg = panjang*lebar
    print(panjang,'*',lebar,'=',luaspsg)
    
def luas_lingkaran(jarijari):
    print("luas lingkaran")
    phi = 3.14
    luaslgk = phi*jarijari*jarijari
    luaslgk_irisan = luaslgk*0.5
    #print(phi,"*",jarijari,"*",jarijari,"=",luaslgk)
    
    print("apakah irisan?")
    print("tidak")
    print("ya")
    kondisi_lgk = input()

    if kondisi_lgk == "tidak":
        print(phi,"*",jarijari,"*",jarijari,"=",luaslgk)
    else:
        print(phi,"*",jarijari,"*",jarijari,"=",luaslgk_irisan)
