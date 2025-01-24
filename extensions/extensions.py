def main():
    file_name = input("File name: ").lower().strip()
    parts = file_name.split(".")
    if len(parts) == 1:
        print("application/octet-stream")
    else:
        extension = file_name.split(".")[len(parts) - 1]
        match extension:
            case "gif":
                print("image/gif")
            case "jpeg" | "jpg":
                print("image/jpeg")
            case "png":
                print("image/png")
            case "pdf":
                print("application/pdf")
            case "txt":
                print("text/plain")
            case "zip":
                print("application/zip")
            case _:
                print("application/octet-stream")

main()
