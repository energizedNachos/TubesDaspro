#Penulis Modul: Moch. Sofyan Firdaus - 16521144, Nicholas Liem - 16521108, Darren - 16521063
#Judul Modul: Operasi Array
#Tanggal: 9 April 2022

def panjang_baris(array_data):
    panjangBaris = 0
    for baris in array_data:
        panjangBaris +=1
    return panjangBaris

def panjang_kolom(array):
    panjangKolom = 0
    for kolom in array[0]:
        panjangKolom+=1
    return panjangKolom

def fungsi_append(array,s):
    temp = ['' for i in range(panjang_baris(array)+1)]
    for i in range (panjang_baris(array)+1):
        if i < panjang_baris (array):
            temp[i]=array[i]
        else:
            temp[i]=s   
    return temp

def copy(array):
    temp = ['' for _ in range(panjang_baris(array))]
    for i in range(panjang_baris(array)):
        temp[i] = array[i]
    return temp

def join(s, array_string):
    out = ''
    panjang = panjang_baris(array_string)
    for i in range(panjang-1):
        out += array_string[i] + s
    out += array_string[panjang-1]
    return out

#SEARCHING
def found_in_kolom(array,kolom_id,validator):
    for i in range(panjang_baris(array)):
        if array[i][kolom_id] == validator:
            return True
    return False

def all_valid_row(array,csvID,validator):
    data_baris = []
    for baris in array:
        if baris[csvID] == validator:
            data_baris = fungsi_append(data_baris, baris)
    return data_baris

def find_row_id(array, csvID, validator):
    #Asumsikan bahwa data pasti ada di barisnya
    panjang_baris_data = panjang_baris(array)
    for i in range(1,panjang_baris_data):
        if array[i][csvID] == validator:
            baris_id = i
    return baris_id

def delete_column(array, columnCSVId):
    panjang_kolom_data = panjang_kolom(array)
    array_without_column = []
    for item in array:
        baris_temp = []
        for i in range(panjang_kolom_data):
            if i != columnCSVId:
                baris_temp = fungsi_append(baris_temp,item[i])
        array_without_column = fungsi_append(array_without_column, baris_temp)
    return array_without_column

def max_in_row(matrix, index, context):
    maks = matrix[index][0]
    for i in range(panjang_kolom(matrix)):
        if context(maks) < context(matrix[index][i]):
            maks = matrix[index][i]
    return maks

def max_in_column(matrix, index, context):
    maks = matrix[0][index]
    for i in range(panjang_baris(matrix)):
        if context(maks) < context(matrix[i][index]):
            maks = matrix[i][index]
    return maks

def cetak_tabel(matrix):
    kolom = panjang_kolom(matrix)
    baris = panjang_baris(matrix)
    max_width = [0 for x in range(kolom)]
    pemisah = '+'
    for i in range(kolom):
        max_width[i] = panjang_baris(max_in_column(matrix, i, panjang_baris))
        pemisah += '-' * max_width[i] + '+'
    for i in range(baris):
        print(pemisah)
        for j in range(kolom):
            print("|{0:<{width}}".format(matrix[i][j], width=max_width[j]), end='')
        print('|')
    print(pemisah)

def cekinteger(variabel):
    for c in variabel:
        if not(48 <= ord(c) <= 57):
            return False
    return True

def operasi_dua_array(array1, array2, operator):
    array_sama = []
    found = False
    if operator == "CHECK_IF_CONSISTS":
        for item1 in array1:
            for item2 in array2:
                if item1 == item2:
                    found = True
        return found

    elif operator == "RETURN_SAME":
        for item1 in array1:
            for item2 in array2:
                if item1 == item2:
                    array_sama = fungsi_append(array_sama,item1)
        return array_sama

def sorting_ascd(array,id):
    for i in range(2, panjang_baris(array)):
        Temp_Baris = array[i]
        Temp_Id = int(array[i][id])
        Tag = i-1
        while (Temp_Id < int(array[Tag][id])) and (Tag > 1):
            array[Tag+1] = array[Tag]
            Tag -= 1
        if (Temp_Id >= int(array[Tag][id])):
            array[Tag+1] = Temp_Baris
        else:
            array[Tag+1] = array[Tag]
            array[Tag] = Temp_Baris
    return array

def sorting_dscd(array,id):
    for i in range(2, panjang_baris(array)):
        Temp_Baris = array[i]
        Temp_Id = int(array[i][id])
        Tag = i-1
        while (Temp_Id > int(array[Tag][id])) and (Tag > 1):
            array[Tag+1] = array[Tag]
            Tag -= 1
        if (Temp_Id <= int(array[Tag][id])):
            array[Tag+1] = Temp_Baris
        else:
            array[Tag+1] = array[Tag]
            array[Tag] = Temp_Baris
    return array