import struct
import sys

#Stable
S0 =[["01","00","11","10"],
    ["11","10","01","00"],
    ["00","10","01","11"],
    ["11","01","11","10"]]

S1 =[["00","01","10","11"],
    ["10","00","01","11"],
    ["11","00","01","10"],
    ["10","01","00","10"]]

# permutations functions
def p10(arr):
    arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7],arr[8],arr[9] = arr[2],arr[4],arr[1],arr[6],arr[3],arr[9],arr[0],arr[8],arr[7],arr[5]
    return arr

def p8(arr):
    arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7],arr[8],arr[9] = arr[5],arr[2],arr[6],arr[3],arr[7],arr[4],arr[9],arr[8],arr[0],arr[1]
    arr.pop()
    arr.pop()
    return(arr)

def P4(arr):
    arr[0],arr[1],arr[2],arr[3] = arr[1],arr[3],arr[2],arr[0]
    return(arr)

#left shift function
def ls(arr, n):
    for i in range (0,n):
        arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7],arr[8],arr[9] = arr[1],arr[2],arr[3],arr[4],arr[0],arr[6],arr[7],arr[8],arr[9],arr[5]
    return arr

#split function
def split(arr):
    half = len(arr)//2
    return arr[:half], arr[half:]

#xor function
def xor(a, b):
    y = ''.join('0' if i == j else '1' for i, j in zip(a,b))
    y = [int(x) for x in str(y)]
    return y

#subkey 1 and 2 functions
def sk1(key):
    arr = [int(x) for x in str(key)]
    #p10
    p10(arr)    
    # #ls1
    ls(arr, 1)
    #p8
    p8(arr)
    return(arr)

def sk2(key):
    arr = [int(x) for x in str(key)]
    #p10
    p10(arr)    
    # #ls1
    ls(arr, 3)
    #p8
    p8(arr)
    return(arr)

#Pi process
def IP(arr):
    arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7] = arr[1],arr[5],arr[2],arr[0],arr[3],arr[7],arr[4],arr[6]
    return(arr)

def IPinv(arr):
    arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7] = arr[3],arr[0],arr[2],arr[4],arr[6],arr[1],arr[7],arr[5]
    return(arr)

def EP(arr):
    arr[0],arr[1],arr[2],arr[3] = arr[3],arr[0],arr[1],arr[2]
    arr.append(arr[2])
    arr.append(arr[3])
    arr.append(arr[0])
    arr.append(arr[1])
    return arr

#find row and column from S0 and S1 table
def sbox(arr,s):
    row = str(arr[0])+str(arr[3])
    if row == "00":
        row = 0
    elif row == "01":
        row = 1
    elif row == "10":
        row = 2
    elif row == "11":
        row = 3
    col = str(arr[1])+str(arr[2])
    if col == "00":
        col = 0
    elif col == "01":
        col = 1
    elif col == "10":
        col = 2
    elif col == "11":
        col = 3
    return(s[row][col])

#swap left and right(theta function)
def theta(x,y):
    temp = x
    x = y
    y = temp
    return x+y

#Pi
def Pi(key, p, sk):
    arr = [int(x) for x in str(p)]
    arr = split(arr)
    end2 = arr[1].copy()
    end2 = str(end2[0])+str(end2[1])+str(end2[2])+str(end2[3])
    b2 = EP(arr[1])
    table = xor(sk(key),b2)
    sTable = split(table)
    sTable = sbox(sTable[0],S0)+sbox(sTable[1],S1)
    sTable = [int(x) for x in str(sTable)]
    sTable = P4(sTable)
    end1 = xor(sTable, arr[0])
    end1 = str(end1[0])+str(end1[1])+str(end1[2])+str(end1[3])
    return(end1, end2)

#encrypt
def enc(key,plain):
    plain = [int(x) for x in str(plain)]
    plain = IP(plain)
    plain = ''.join([str(a) for a in plain])
    x = Pi(key,plain,sk1)
    y = str(theta(x[0],x[1]))
    z = Pi(key, y, sk2)
    l = str(z[0])+str(z[1])
    l = [int(x) for x in str(l)]
    end = IPinv(l)
    end = ''.join([str(a) for a in end])
    return(end)

#decrypt
def dec(key,cipher):
    cipher = [int(x) for x in str(cipher)]
    cipher = IP(cipher)
    cipher = ''.join([str(a) for a in cipher])
    x = Pi(key, cipher, sk2)
    y = str(theta(x[0],x[1]))
    z = Pi(key, y, sk1)
    l = str(z[0])+str(z[1])
    l = [int(x) for x in str(l)]
    end = IPinv(l)
    end = ''.join([str(a) for a in end])
    return end

#read file and confert to bytes and bits functions
def get_bytes(filename):
    with open(filename, 'rb') as fileobject:
        byte=fileobject.read(1)
        while byte != b'':
            yield byte
            byte=fileobject.read(1)

def write_bytes(filename, byte_generator):
    with open(filename, 'wb') as fileobject:
        for byte in byte_generator:
            fileobject.write(byte)

def byte_to_bits(byte):
    return ord(byte)

def bits_to_byte(bits):
    return struct.pack("B", bits)

#file reading and writing
def main(x,y,z):
    for byte in get_bytes(x):
        bitstring=bin(byte_to_bits(byte))[2:].zfill(8)
        cipher_bitstring= y(z , bitstring)
        cipher_bit=int(cipher_bitstring, 2)
        yield bits_to_byte(cipher_bit)

#shell arguments functions
def shellarg():
    # -e or -d command
    a = sys.argv[1]
    #10bit key
    key = sys.argv[2]
    src = sys.argv[3]
    dest = sys.argv[4]

    if a == "-e":
        if len(key) != 10:
            print("only 10-bits key are accepted here...")
        else:
            valid = True
            for item in key:
                if item not in {'0','1'}:
                    print("only 10-bits binary are accepted here...")
                    valid = False
                    break
            if valid:
                write_bytes(dest, main(src,enc,key))
    elif a == "-d":
        if len(key) != 10:
            print("only 10-bits key are accepted here...")
        else:
            valid = True
            for item in key:
                if item not in {'0','1'}:
                    print("only 10-bits binary are accepted here...")
                    valid = False
                    break
            if valid:
                write_bytes(dest, main(src,dec,key))
        
    else:
        print("wrong syntax... pls use -e to encrypt or -d to decrypt")

shellarg()