def string_match(string1, string2):
	string1_words = string1.split(' ')
	string2_words = string2.split(' ')
	for i in range(min(len(string1_words), len(string2_words))):
		if string1_words[i] != string2_words[i]:
			print(string1_words[i],string2_words[i],end = '\n')

if __name__ == '__main_':
	string_match(input(),input())
