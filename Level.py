#!/usr/bin/python3

# Class
class Level:

	# Attributes
	__lineCount = 0

	# Level loading method
	def loadLevel(self, filename):
		with open(filename, "r") as myfile:
#			array = []
			for line in myfile:
				self.__lineCount += 1
#				array.append(line)
				words = line.split("\t")
				if len(words[0]) > 0 and words[0][0] == '#':
					continue
					print("#COMMENT")
				elif words[0] == "thing" and len(words) == 6:
					print(words[1])
				elif words[0] == "poly" and len(words) == 20:
					print(words[1])
				else:
					print("INVALID LINE IGNORED AT {}".format(self.__lineCount))

	# Constructor
	def __init__(self, filename):
		self.loadLevel(filename)

	# Method
	def displayCount(self):
		print("Total lines {}".format(self.__lineCount))


lvl = Level("file.txt")
#lvl.displayCount()

