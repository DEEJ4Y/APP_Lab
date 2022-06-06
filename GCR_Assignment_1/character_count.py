def character_count(text: str):
    text_length = len(text)
    character_count_set = list()

    for i in range(0, text_length):
        curr = text[i]
        found = False
        for j in range(0, len(character_count_set)):
            character_data = character_count_set[j]
            if character_data["character"] == curr:
                character_data["count"] += 1
                found = True

        if not found:
            character_count_set.append({"character": curr, "count": 1})

    return character_count_set


if __name__ == "__main__":
    sentence = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam assumenda atque quidem dignissimos id harum aliquid tenetur corrupti, iste rerum libero expedita? Dicta, sit temporibus esse ab nisi quaerat aliquid!'
    print(sentence)
    print(character_count(sentence))
