def main():
	path_to_book = "books/frankenstein.txt"
	book_name = "frankenstein"
	text = get_book(path_to_book)
	print(f"There are {count_words(text)} words in {book_name}")
	print('\n'+'\n'.join(f'There are {i[1]} instance(s) of the letter: {i[0]}' for i in count_chars(text)))

def get_book(book):	
	with open(book, "r") as fronk:
		return fronk.read()

def count_words(text_inp):
	words = text_inp.split()
	return len(words)

def count_chars(text_inp):
	Counter = __import__("collections", fromlist=["Counter"]).Counter
	#characters = dict(Counter(i for i in text_inp.lower() if i.isalpha()))
	return Counter(i for i in text_inp.lower() if i.isalpha()).most_common()

if __name__ == "__main__":
	main()
