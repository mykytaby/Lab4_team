def ruslankonoz():
    from config import TEXT
    # lowercase the sentence
    text = TEXT.lower()

    # replace a letter "а" with @
    text = text.replace("а", "@")

    # split the TEXT by separator @
    text = text.split("@")

    var = "{There was a}"

    # join the string with "{0}" as joiner"
    text = "{0}".join(text)

    # format the TEXT substituting the "var" into the sentence
    text = text.format(var)

    # make all first letters capital
    text = text.title()

    print(text)


def mykytabychenok():
    from config import TEXT

    # Count occurrences of the word "програмування"
    programming_count = TEXT.count("програмування")
    print(f"Occurrences of 'програмування': {programming_count}")

    # Find the index of the word "програмування"
    programming_index = TEXT.find("програмування")
    print(f"First occurrence of 'програмування': {programming_index}")

    # Strip whitespaces from text elements
    text_parts = TEXT.split(".")  # Split sentences for demonstration
    stripped_parts = [part.strip() for part in text_parts]
    print(f"Text after stripping: {stripped_parts}")


if __name__ == '__main__':
    ruslankonoz()
    mykytabychenok()
