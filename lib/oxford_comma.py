def oxford_comma(items):
    if len(items) == 1:
        return ''.join(items)
    elif len(items) ==2:
        return items[0] + " and " + items[1]
    else:
        length = len(items) - 1
        all_but_last = items[0:length]
        first_words = ", ".join(all_but_last)
        return first_words + ", and " + items[length]

