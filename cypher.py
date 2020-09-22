def encode(message, shift):
    encoded_message = ""
    rest = shift % 26
    for i in range(0, len(message)):
        nt_enc = ord(message[i])
        if rest == 0 or nt_enc < 65 or (90 < nt_enc < 97) or nt_enc > 122:
            encoded_message += chr(nt_enc)
        elif 65 <= nt_enc <= 90:  # suured tahed
            difference = 90 - nt_enc
            if difference >= rest:
                encoded_message += chr(nt_enc + rest)
            else:
                remain = rest - difference
                encoded_message += chr(64 + remain)
        elif 97 <= nt_enc <= 122:  # vaikesed tahed
            difference = 122 - nt_enc
            if difference >= rest:
                encoded_message += chr(nt_enc + rest)
            else:
                remain = rest - difference
                encoded_message += chr(96 + remain)
    return encoded_message


def crack(encoded_message, phrase):
    cracked = ""
    if phrase == encoded_message or phrase in encoded_message or phrase == "":
        cracked = encoded_message
    elif len(encoded_message) < len(phrase) or len(encoded_message) <= 0:
        cracked = None
    elif len(phrase) <= 0 or phrase.isspace() or encoded_message.isspace():
        cracked = None
    else:
        answers = []
        for a in range(0, 26):  # AscII tahestikus on 26 tahti
            coded = encode(encoded_message, a)
            if phrase in coded:
                answers.append(coded)
                cracked = answers[len(answers) - 1]
            elif len(answers) <= 0:
                cracked = None
    return cracked


if __name__ == '__main__':
    print(encode("i like turtles", 6))