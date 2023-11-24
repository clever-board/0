from Crypto.Cipher import AES
import sys
from getpass import getpass

i = getpass().encode()

while len(i) < 32:
	i += b'0'

key = i[:16]
iv = i[16:]

def encrypt(buffer):
	try:
		cipher = AES.new(key, AES.MODE_GCM, iv)
		return cipher.encrypt(buffer)
	except Exception as e:
		print(e)
		return b''

def decrypt(buffer):
	try:
		cipher = AES.new(key, AES.MODE_GCM, iv)
		return cipher.decrypt(buffer)
	except Exception as e:
		print(e)
		return b''

if __name__ == '__main__':
	option = int(sys.argv[1])
	input_filename = sys.argv[2]
	if option == 0:
		output_filename = input_filename + '.crypt47'
		with open(input_filename, 'rb') as _in:
			data = _in.read()
		c = encrypt(data).hex()
		with open(output_filename, 'w') as _out:
			_out.write(c)
	else:
		output_filename = input_filename.split('.crypt47')[0]
		with open(input_filename, 'r') as _in:
			data = _in.read()
		data = bytes.fromhex(data)
		d = decrypt(data)
		with open(output_filename, 'wb') as _out:
			_out.write(d)