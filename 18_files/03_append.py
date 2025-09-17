# Append to an existing file called abhi bauhre.txt
# It should add data about abhi bauhre hometown

f = open("abhi bauhre.txt","a")

string = '''
John Doe initially lived in Phoenix, Arizona. He is a very nice guy
'''
f.write(string)

f.close()

