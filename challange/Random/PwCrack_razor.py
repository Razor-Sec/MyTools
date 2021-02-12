import hashlib
print("Password Cracker By Razor")

found = 0
in_hash = input("enter your hash password : ")
wordlist = input("path of your wordlist :")

try :
    pw_file = open(wordlist, 'r')
except :
    print("error, File not found")
    print(wordlist, "Not found")
    quit()

for cracking in pw_file:
    enc_word = cracking.encode('utf-8')
    hash_word = hashlib.md5(enc_word.strip())
    digest = hash_word.hexdigest()

    if digest == in_hash:
        print("Password found.\nThe password is", cracking)
        found = 1
        break
if not found:
    print("password not found in",pw_file ," file")
    print("\n")

print("Thanks for using my program")