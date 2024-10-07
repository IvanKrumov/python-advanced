text = input()
text_dict = {}

# unique_symbols = sorted(set(text))   BETTER WAY
# print(unique_symbols)
# [print(f"{ch}: {text.count(ch)} times/s" for ch in sorted(set(text)))]   MUCH BETTER

for letter in text:
    if letter not in text_dict:
        text_dict[letter] = 1
    else:
        text_dict[letter] += 1

for key, value in sorted(text_dict.items()):
    print(f"{key}: {value} time/s")