
path = "books/"
filename =""

def main():
    #add userinput filename?
    while True:
        filename = input("enter filename of book in /books directory\ndefaults to frankenstein.txt\nctrl+c to quit\n\n")
        if filename == "":
            filename= "frankenstein.txt"
        with open(path+filename) as file:
            file_contents = file.read()
            report(word_count(file_contents), char_count(file_contents))

def dict_sort_on_val(dict):
    sorted_list = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_list


def word_count(string):
    return len(string.split())

def char_count(string):
    string=string.lower()
    chars={}
    for char in string:
        if char.isalpha():
            if char in chars:
                chars[char]+=1
            else:
                chars[char]=1
    return chars

def report(word_count, chars_count):
    print(f"--- Begin report of {path}{filename} ---")
    print(f"{word_count} words in document")
    sorted_list_of_tups = dict_sort_on_val(chars_count)
    for tup in sorted_list_of_tups:
        print(f"The char '{tup[0]}' appears {tup[1]} times")
    print("-----complete-----\n\n")

main()
