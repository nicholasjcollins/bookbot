def main():
    filepath = "books/frankenstein.txt"
    contents = ""
    with open(filepath) as f:
        contents = f.read()
    print(f"--- Begin report of {filepath} ---")
    print()
    print(f"{word_count(contents)} words found in the document")
    for dict in character_count(contents):
        print(f"The '{dict["character"]}' was found {dict["count"]} times")

def word_count(str):
    return len(str.split())

def character_count(str):
    normalized = str.lower()
    dict = {}
    for char in normalized:
        if char in dict:
            dict[char] += 1
        elif char.isalpha():
            dict[char] = 1
    lis = []
    for key in dict:
        new_dict = {}
        new_dict["character"]= key
        new_dict["count"] = dict[key]
        lis.append(new_dict)
        lis.sort(reverse=True, key=sort_on)
    return lis

def sort_on(dict):
    return dict["count"]
        


main()

