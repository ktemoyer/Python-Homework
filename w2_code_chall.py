#Task 1
user_num=(input("Type integers separated by a space: "))
user_list=user_num.split()
for i in range(len(user_list)):
    user_list[i]=int(user_list[i])
total=sum(user_list)
print(f'These numbers add to {total}.')

#Task 2
fav_books=("ACOTAR", "Sapiens", "simplicity", "Fourth Wing", "The Body Keeps the Score")
for i in fav_books:
    print(i)

#Task 3
user_dict={'Name':"K", 'Age':23, 'Color':"Blue", 'School':"Bachelor"}
user_dict['Name']=input("What is your name? ")
user_dict['Age']=int(input("How old are you? "))
user_dict['Color']=input("What is your favorite color? ")
user_dict['School']=input("What is your highest education level? ")
print(user_dict)

#Task 4
set1={}
set2={}
set1=set(input("Enter elements of the first set separated by spaces: "))
set2=set(input("Enter elements of the second set separated by spaces: "))

print(set1&set2)

#Task 5
def get_word_list():
    words = input("Enter a list of words separated by spaces: ").split()
    return words
word_list = get_word_list()
odd_length_words = [word for word in word_list if len(word) % 2 != 0]
print("Words with odd number of characters:", odd_length_words)


