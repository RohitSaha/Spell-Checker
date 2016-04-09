import pypyodbc

def checking(passed_word, word_entered):
    operations = 0
    k = 0
    j = 0
    similar = 0
    while (k< len(passed_word)):
        while(j< len(word_entered)):
            if(passed_word[k] == word_entered[j]):
                k = k+1
                j = j+1
                similar = similar + 1
            else:
                if(len(word_entered) < len(passed_word)):
                    word_entered = word_entered[0:j] + passed_word[k] + word_entered[j:]
                    k = k+1
                    j = j+1
                elif(len(word_entered) > len(passed_word)):
                    word_entered = word_entered[0:j] + word_entered[(j+1):]
                else:
                    word_entered = word_entered[0:j] + passed_word[k] + word_entered[(j+1):]
                    k = k+1
                    j = j+1
                print word_entered
                operations = operations + 1
    probability = (float)(operations) / ((float)(length) * (float)(similar))
    print (probability)
    probability_of_words.append(probability)


conn = pypyodbc.win_connect_mdb('F:\\Dictionary')
cur1 = conn.cursor()

print("Words available in the dictionary")

SQL = 'SELECT * FROM WORDS ORDER BY STRINGS'
cur1.execute(SQL)

for row in cur1.fetchall():
    for field in row:
        print field

word = raw_input("Enter word")
word = word.upper()
temp = ""
temp = word[0]
length = len(word)

words = []
probability_of_words = []

SQL = 'SELECT * FROM WORDS WHERE STRINGS LIKE \''+ temp + '%\' '
cur1.execute(SQL)

for row in cur1.fetchall():
    for field in row:
        print field
        words.append(field)


cur1.close()
conn.close()

for i in words:
    checking(i, word)

min_probability = probability_of_words[0]
store = 0

for i in range(0, len(probability_of_words)):
    if(probability_of_words[i] < min_probability):
        min_probability = probability_of_words[i];
        store = i

print("Least Percentage of operations done : " , min_probability)
print("Predicted word : " , words[store])


