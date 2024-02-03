import os
import threading

os.system('cls')


print(" Hash generator")
print(" Choose your Hash algorithm :")
print()
n = input(" 1 - MD5\n 2 - SHA-256\n 3 - SHA-384\n 4 - SHA-512\n\n Please enter a number : ")


def main():
	for i in range(10000):

		print(f" Hash {i} calculation in progress...")

		hash_i = []

		temp0 = open("temp0", "w")
		temp0.write(str(i))	
		temp0.close()

		if n == '1':
			os.system("certUtil -hashfile temp0 MD5 > temp1")
		if n == '2':
			os.system("certUtil -hashfile temp0 SHA256 > temp1")
		if n == '3':
			os.system("certUtil -hashfile temp0 SHA384 > temp1")
		if n == '4':
			os.system("certUtil -hashfile temp0 SHA512 > temp1")

		temp1 = open("temp1","r")
		content = temp1.read()
		temp1.close()


		if n == '1':
			hash_file = open("MD5.txt","a")
			for j in range(23,55,1):
				hash_i.append(content[j])

			hash_file.write(f"The hash MD5 of {i} is : ")

			for j in range(32):
				hash_file.write(hash_i[j])

		if n == '2':
			hash_file = open("SHA-256.txt","a")
			for j in range(26,90,1):
				hash_i.append(content[j])

			hash_file.write(f"The hash SHA-256 of {i} is : ")

			for j in range(64):
				hash_file.write(hash_i[j])

		if n == '3':
			hash_file = open("SHA-384.txt","a")
			for j in range(26,122,1):
				hash_i.append(content[j])

			hash_file.write(f"The hash SHA-384 of {i} is : ")

			for j in range(96):
				hash_file.write(hash_i[j])

		if n == '4':
			hash_file = open("SHA-512.txt","a")
			for j in range(26,154,1):
					hash_i.append(content[j])

			hash_file.write(f"The hash SHA-512 of {i} is : ")

			for j in range(128):
				hash_file.write(hash_i[j])

		hash_file.write("\n")
		hash_file.close()

	os.system("del temp0, temp1")

	print("Calcul de Hash terminé.")



def test():

	i = 0
	while(i<10000):
		t0 = threading.Thread(target = Calcul_Tempx(i,0))
		i += 1
		t1 = threading.Thread(target = Calcul_Tempx(i,1))
		i += 1
		t2 = threading.Thread(target = Calcul_Tempx(i,2))
		i += 1
		t3 = threading.Thread(target = Calcul_Tempx(i,3))
		i += 1
		t4 = threading.Thread(target = Calcul_Tempx(i,4))
		i += 1
		t5 = threading.Thread(target = Calcul_Tempx(i,5))
		i += 1
		t6 = threading.Thread(target = Calcul_Tempx(i,6))
		i += 1
		t7 = threading.Thread(target = Calcul_Tempx(i,7))
		i+= 1
		t8 = threading.Thread(target = Calcul_Tempx(i,8))
		i += 1
		t9 = threading.Thread(target = Calcul_Tempx(i,9))
		i += 1
		t10 = threading.Thread(target = Calcul_Tempx(i,10))
		i += 1
		t11 = threading.Thread(target = Calcul_Tempx(i,11))
		i += 1
		t12 = threading.Thread(target = Calcul_Tempx(i,12))
		i += 1
		t13 = threading.Thread(target = Calcul_Tempx(i,13))
		i += 1
		t14 = threading.Thread(target = Calcul_Tempx(i,14))
		i += 1
		t15 = threading.Thread(target = Calcul_Tempx(i,15))
		i += 1

		t0.start()
		t1.start()
		t2.start()
		t3.start()
		t4.start()
		t5.start()
		t6.start()
		t7.start()
		t8.start()
		t9.start()
		t10.start()
		t11.start()
		t12.start()
		t13.start()
		t14.start()
		t15.start()


		t0.join()
		t1.join()
		t2.join()
		t3.join()
		t4.join()
		t5.join()
		t6.join()
		t7.join()
		t8.join()
		t9.join()
		t10.join()
		t11.join()
		t12.join()
		t13.join()
		t14.join()
		t15.join()

	print("Calcul de Hash terminé.")

def Calcul_Tempx(x,y):
	hash_i = []
	temp0 = open(f"temp{y}", "w")
	temp0.write(str(x))	
	temp0.close()
	os.system(f"certUtil -hashfile temp{y} SHA512 > temp{y+100}")
	temp1 = open(f"temp{y+100}","r")
	content = temp1.read()
	temp1.close()
	hash_file = open("SHA-512.txt","a")
	for j in range(26,155,1):
		hash_i.append(content[j])

	hash_file.write(f"The hash SHA-512 of {x} is : ")

	for j in range(129):
		hash_file.write(hash_i[j])

	hash_file.write("\n")
	hash_file.close()



if __name__ == "__main__":
	main()
	#test()