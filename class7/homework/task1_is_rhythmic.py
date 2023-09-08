def is_rhythmic(bars: str) -> bool:
    phrases = bars.split()
    checked_vowels_amount = 0
    for letter in phrases[0]:
        if letter.lower() in ["а", "е", "ё", "и", "о", "у", "ы", "ю", "я"]:
            checked_vowels_amount += 1
                
    for i in range(1, len(phrases)):
        current_vowels_amount = 0
        for letter in phrases[i]:
            if letter.lower() in ["а", "е", "ё", "и", "о", "у", "ы", "ю", "я"]:
                current_vowels_amount += 1
        if current_vowels_amount != checked_vowels_amount:
            return False
    return True


def main():
    lines = input("Enter your bars to check if their rhythm is good: ")
    answer = is_rhythmic(lines)
    if answer:
        print("Парам пам-пам")
    else:
        print("Пам парам")
        
main()