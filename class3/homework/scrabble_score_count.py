ENGLISH_SCORES = {
    'A' : 1, 'E' : 1, 'I' : 1,
    'O' : 1, 'U' : 1, 'L' : 1,
    'N' : 1, 'S' : 1, 'T' : 1,
    'R' : 1, 'D' : 2, 'G' : 2,
    'B' : 3, 'C' : 3, 'M' : 3,
    'P' : 3, 'F' : 4, 'H' : 4,
    'V' : 4, 'W' : 4, 'Y' : 4,
    'K' : 5, 'J' : 8, 'X' : 8,
    'Q' : 10, 'Z' :10
}

RUSSIAN_SCORES = {
    'А' : 1, 'В' : 1, 'Е' : 1,
    'И' : 1, 'Н' : 1, 'О' : 1,
    'Р' : 1, 'С' : 1, 'Т' : 1,
    'Д' : 2, 'К' : 2, 'Л' : 2,
    'М' : 2, 'П' : 2, 'У' : 2,
    'Б' : 3, 'Г' : 3, 'Ё' : 3,
    'Ь' : 3, 'Я' : 3, 'Й' : 4,
    'Ы' : 4, 'Ж' : 5, 'З' : 5,
    'Х' : 5, 'Ц' : 5, 'Ч' : 5,
    'Ш' : 8, 'Э' : 8, 'Ю' : 8,
    'Ф' : 10, 'Щ' : 10, 'Ъ' : 10
}


def count_score(word: str) -> int:
    score = 0
    word = word.upper()
    err_msg = Exception("The word contains letters from other alphabets")
    
    if word[0] in ENGLISH_SCORES:
        for letter in word:
            if letter in ENGLISH_SCORES:
                score += ENGLISH_SCORES[letter]
            else:
                raise err_msg 
    
    elif word[0] in RUSSIAN_SCORES:
        for letter in word:
            if letter in RUSSIAN_SCORES:
                score += RUSSIAN_SCORES[letter]
            else:
                raise err_msg 
            
    else:
        raise Exception("No appropriate alphabet found")
    
    return score


def main():
    word = input("Enter a word you want to count score for: ")
    print(count_score(word))
    

main()