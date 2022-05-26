import argparse
import binascii
import hashlib


class Sum:
	
	def main():
		args = argparse.ArgumentParser()
  
		args.add_argument("-e", "--export", help = "File to hash", required = False)
		args.add_argument("-a", "--algo", help = "Algorithm to use", required = False)
		args.add_argument("-f", "--file", help = "Hash file exported", required = True)
		args.add_argument("-v", "--verify", help = "Compare two hashes", required = False)
		
		argument = args.parse_args()
		content = open(argument.file, 'rb').read()
		
		if argument.algo == "md5":
			result = hashlib.md5(content).hexdigest()
   
		elif argument.algo == "crc32":
			result = str("%08X" % binascii.crc32(content)).lower()
			
		elif argument.algo == "sha1":
			result = hashlib.sha1(content).hexdigest()
			
		elif argument.algo == "sha224":
			result = hashlib.sha224(content).hexdigest()
			
		elif argument.algo == "sha256":
			result = hashlib.sha256(content).hexdigest()
			
		elif argument.algo == "sha384":
			result = hashlib.sha384(content).hexdigest()
			
		elif argument.algo == "sha512":
			result = hashlib.sha512(content).hexdigest()
		
		elif argument.algo == "blake2b":
			result = hashlib.blake2b(content).hexdigest()

		else:
			result = hashlib.md5(content).hexdigest()
   
   
		if (argument.export):
			hash_file = open(argument.export + "." + argument.algo, 'w')
			hash_file.write("*" + argument.file + "*       " + result)
			print("Hash exported to " + argument.export + "." + argument.algo)

		if (argument.verify):
	  
			if (result == argument.verify):
				print("Hash is correct")
				print(str(result) + " == " + argument.verify)
				
			else:
				print("Hash is incorrect")
				print(str(result) + " != " + argument.verify)
				
	
		else:
			print(result)
		
		
Sum.main()