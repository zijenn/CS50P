def main():
    file = input("File name: ").strip().lower()

    if file.rpartition(".")[2] == "pdf":
            print("application/pdf")
    elif file.rpartition(".")[2] == "jpg":
            print("image/jpeg")
    elif file.rpartition(".")[2] == "jpeg":
            print("image/jpeg")
    elif file.rpartition(".")[2] == "png":
            print("image/png")
    elif file.rpartition(".")[2] == "txt":
            print("text/plain")
    elif file.rpartition(".")[2] == "zip":
            print("application/zip")
    elif file.rpartition(".")[2] == "gif":
            print("image/gif")

    else:
          print("application/octet-stream")
main()