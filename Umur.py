umur = int(input('Masukan umur:'))

if umur >= 65:
    print('Usia Pensiun')
elif umur>= 25:
    print('Usia Produktif')
elif umur>= 15:
    print('Usia Remaja')
elif umur>= 1:
    print('Usia Anak Anak')
else:
    print('Kondisi Salah')