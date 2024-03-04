def convert(faces):
    convert_to_emoji = faces.replace(":)", "🙂").replace(":(", "🙁")
    return convert_to_emoji


def main():

    faces = input("Type anything and add happy face or sad face... ")
    print(convert(faces))


main()
