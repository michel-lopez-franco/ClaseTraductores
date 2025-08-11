entrada = "hola 9 9,8 10 mundo"


def siguiente_token(entrada):
    edo = 0
    token = ""
    for c in entrada:
        match edo:
            case 0:
                if c >= "a" and c <= "z":
                    edo = 1
                    token += c
                if c >= "0" and c <= "9":
                    edo = 2
                    token += c

            case 1:
                if c >= "a" and c <= "z":
                    token += c
                else:
                    break
            case 2:
                if c >= "0" and c <= "9":
                    token += c
                else:
                    break

    match edo:
        case 1:
            return "str", token
        case 2:
            return "int", token
        case _:
            return "EOF", None


print(siguiente_token(entrada))
print(siguiente_token(entrada))
