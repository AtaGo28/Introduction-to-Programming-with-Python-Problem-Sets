def main():
    file_name = input("File name: ").strip().lower()
    print(check_file(file_name))


def check_file(filename):
    if filename.endswith((".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip")):
        return (
            "image/gif"
            if filename.endswith(".gif")
            else "image/jpeg"
            if filename.endswith((".jpg", ".jpeg"))
            else "image/png"
            if filename.endswith(".png")
            else "application/pdf"
            if filename.endswith(".pdf")
            else "text/plain"
            if filename.endswith(".txt")
            else "application/zip"
            if filename.endswith(".zip")
            else None
        )
    else:
        return "application/octet-stream"


main()
