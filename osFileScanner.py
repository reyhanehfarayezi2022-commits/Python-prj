import os
class FileScanner :
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_size = 0
        self.file_name = ""

    def extract_file_info(self):
        if os.path.exists(self.file_path):
            self.file_name = os.path.basename(self.file_path)
            self.file_size = os.path.getsize(self.file_path)

            if os.path.isdir(self.file_path):
                self.list_of_dirfiles = os.listdir(self.file_path)
                print(f"\n\n\t\t ***name : {self.file_name}\n\t\t***size : {self.file_size}\t\t ***list of directories : {self.list_of_dirfiles}\n\n")
                return self.save_info()
            else:
                print(f"\n\n\t\t ***name : {self.file_name}\n\t\t***size : {self.file_size}\n\n")
                return self.save_info()
        else:
            return(f"\t\t\t*** There is no file with path : {self.file_path} ***\n\n")
        
    def save_info(self):
        z = "info.txt"
        if os.path.exists(z):
            with open(z , "a") as file:
                file.write(f"\n\n\t\t ***name : {self.file_name}\n\t\t***size : {self.file_size}\t\t ***list of directories : {self.list_of_dirfiles}\n\n")
        else :
            with open(z , "w") as file:
                file.write(f"\n\n\t\t ***name : {self.file_name}\n\t\t***size : {self.file_size}\t\t ***list of directories : {self.list_of_dirfiles}\n\n")
        return self.get_file_extention()

    def get_file_extention(self):
        z = "extention.txt"
        if os.path.exists(z):
            with open(z , "a") as file:
                file.write(f"{os.path.splitext(self.file_name)}")

                for item in self.list_of_dirfiles:
                    file.write(f"\n{os.path.splitext(item)[1]}")
        else:
            with open(z , "w") as file:
                file.write(f"{os.path.splitext(self.file_name)}")
                for item in self.list_of_dirfiles:
                    file.write(f"\n{os.path.splitext(item)[1]}")


x = str(input("\tEnter File Path :\t"))
example1 = FileScanner(x)
print(example1.extract_file_info())