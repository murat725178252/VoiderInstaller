import os
import datetime
import colorama
os.system("cls")
os.system("cls")
os.system("cls")
os.system("cls")
os.system("cls")
svrtoollist = ["gamertool"]


gamertoolindex = """
import PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import Qt

while True:
    line = input("$V >")
    if line != "":
        print("G$ : ")
    if line == "clicker":
        alwaysontop = input("always on top [0/1]: ")
        print("Clicker Program Starting ...")

        class ClickerGame(QMainWindow):
            def __init__(self):
                super().__init__()
                self.initUI()

            def initUI(self):
                self.setGeometry(100, 100, 300, 300)
                self.setWindowTitle('Clicker Game')

                self.score = 0

                self.click_button = QPushButton('Click Here!', self)
                self.click_button.setGeometry(50, 100, 200, 50)
                self.click_button.clicked.connect(self.on_click)

                self.score_label = QLabel(f'Score: {self.score}', self)
                self.score_label.setGeometry(50, 150, 200, 50)

            def on_click(self):
                self.score += 1
                self.score_label.setText(f'Score: {self.score}')

        if __name__ == '__main__':
            app = QApplication(sys.argv)
            game = ClickerGame()
            if alwaysontop == "1":
                game.setWindowFlags(Qt.WindowStaysOnTopHint)  # Pencere her zaman en �stte
            game.show()
"""
zipfileindex = """PK  """
htmlsamplewebsite = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Website</title>
</head>
<body>
    <link rel="stylesheet" href="/css/style.css">
    <script src="/js/script.js"></script>
    <h2>Title</h2>
    <a>Hello World!</a>
    <a>1 line</a>
</body>
</html>
"""

csssamplewebsite = """"
* body {
    background-color: aqua;
}"""
AllCreateCommands = """"
|=============================================================================|
|                           CREATE ALL COMMANDS HELP                          |
|    create file                                                              |
|    ╚ Extention                                                              |
|    create folder                                                            |
|    create project                                                           |
|=============================================================================|

"""
history = []
ConvertingLanguageTR = "Dile Dönüştürülüyor : Türkçe"
ConvertingLanguageEN = "Dile Dönüştürülüyor : English"
datenow = datetime.datetime.now()
datenowHistory = ("Saat", datenow.hour,"Gün", datenow.day,f"Ay", datenow.month)
Language = "TR / Türkçe"
history.append(("Opened  :  ", datenowHistory))
# HelpCommand = 'Komut Yardım ; \n [help {isteğe bağlı}] \n      | help c - Komut Yardımı \n      | help - Konsol Yardımı \n \n [create file {uzantı} | NOT:Burada "Yazılmayan create file" kodları var örn: r, s, js, clj] \n      | create file text - Yazı Dosyası \n      | create file html - Web Dosyası \n      | create file asm - Assembly Dosyası \n      | create file py - Python Dosyası \n      | create file pp - Puppet Dosyası \n      | create file java - Java Dosyası \n      | create file php - PHP Intelephense Dosyası \n      | create file powershell - Windows PowerShell Dosyası \n \n [clear] \n      | cls - konsolu temizle \n \n [L] \n      | L EN - konsolu İngilizce*ye Çevir \n      | L TR - konsolu Türkçe*ye Çevir \n \n [history] \n | history  - Geçmişi Yazdır'
HelpCommand = '''
Komut Yardım ; 
    [help] 
      ╠ help c - Komut Yardımı 
      ╚ help - Konsol Yardımı 
 
    [create] 
      ╠ create file  { Dil Adı / Uzantı } - Yazı Dosyası 
      ╠ create project - proje oluştur
      ╠ create zip - zip dosyası : zip dosyası bozuk çikbilir hata için üzgünüz
      ╠ create folder - 
      ╚ create ? - Tüm Create komutlarını göster
 
    [clear] 
      ╠ cls - konsolu temizle 
      ╚ clear - konsolu temizle 
 
    [L] 
      ╠ L EN - konsolu İngilizce*ye Çevir 
      ╚ L TR - konsolu Türkçe*ye Çevir 
 
    [history] 
      ╚ history  - Geçmişi Yazdır
    
    [pc]
      ╠ pc shutdown - bilgisayarı kapat
      ╚ pc restart - bilgisayarı yeniden başlat
 '''
ErrorCommandNotFound = "Hata : Komut Bulunamadı"
Help = f"""Yardım ; 
 Gerekir ise türkçe harf kullanma 
    ╠ ı = i
    ╚ ö = o 
 Komut Yardımı için : help c 
 Konsol Dilini Türkçe Yapmak için : L TR 
 Konsol Dilini İngilizce Yapmak için : L EN
 Mevcut Dilin : {Language}
"""

while True:
    line = input("$V >")
    line = line.lower()
    if line != "":
        print(colorama.Fore.YELLOW + "$", line + colorama.Fore.WHITE)
    datenow = datetime.datetime.now()
    history.append((f"{line}  :  ", datenowHistory))
    # HELP
    if line == "help" or line == "yardim" or line == "yardım":
        print(Help)
        datenow = datetime.datetime.now()
        history.append(("Help  :  ", datenowHistory))
    # LANGUAGES
    elif line == "l tr":  # Language Turkish Converter Element
            print(ConvertingLanguageTR)
            Language = "TR / Türkçe"
            HelpCommand = '''
Komut Yardım ;
    [help] 
      ╠ help c - Komut Yardımı 
      ╚ help - Konsol Yardımı 
 
    [create] 
      ╠ create file  { Dil Adı / Uzantı } - Yazı Dosyası 
      ╠ create project - proje oluştur
      ╠ create zip - zip dosyası : zip dosyası bozuk çikbilir hata için üzgünüz
      ╠ create folder - 
      ╚ create ? - Tüm Create komutlarını göster
 
    [clear] 
      ╠ cls - konsolu temizle 
      ╚ clear - konsolu temizle 
 
    [L] 
      ╠ L EN - konsolu İngilizce*ye Çevir 
      ╚ L TR - konsolu Türkçe*ye Çevir 
 
    [history] 
      ╚ history  - Geçmişi Yazdır

    [pc]
      ╠ pc shutdown - bilgisayarı kapat
      ╚ pc restart - bilgisayarı yeniden başlat'''
            datenowHistory = "Saat", datenow.hour,"Gün", datenow.day,f"Ay", datenow.month
            ConvertingLanguageTR = "Dile Dönüştürülüyor : Türkçe"
            ConvertingLanguageEN = "Dile Dönüştürülüyor : English"
            ErrorCommandNotFound = "Hata : Komut Bulunamadı"
            Help = f"Yardım ; \n Gerekir ise türkçe harf kullanma \n    ╠ ı = i\n    ╚ ö = o \n Komut Yardımı için : help c \n Konsol Dilini Türkçe Yapmak için : L TR \nKonsol Dilini İngilizce Yapmak için : L EN \n Mevcut Dilin : {Language}"
            print("Başarılı")
    elif line == "l en": # Language English Converter Element
            print(ConvertingLanguageEN)
            Language = "EN / English"
            HelpCommand = '''
Command Help ;
    [help]
      ╠ help c - Command Help
      ╚ help - Console Help
 
    [create]
      ╠ create file { Language Name / Extension } - Text File
      ╠ create project
      ╠ create zip - zip file: the zip file may be corrupt, sorry for the error
      ╠ create folder -
      ╚ create ? - Show all Create commands
 
    [clear]
      ╠ cls - clear console
      ╚ clear - clear console
 
    [L]
      ╠ L EN - Translate console to English*
      ╚ L TR - Translate console to Turkish*
 
    [history]
      ╚ history - Print History
    [pc]
      ╠ pc shutdown - shut down the computer
      ╚ pc restart - restart the computer
      '''
            datenowHistory = "Hour", datenow.hour,"Day", datenow.day,f"Month", datenow.month
            ConvertingLanguageTR = "Converting Language : Türkçe"
            ConvertingLanguageEN = "Converting Language : English"
            ErrorCommandNotFound = "Error : Command Not Found"
            Help = f"Help ; \nUse Turkish letters if necessary\n ╠ ı = i\n ╚ ö = o \n ​​For Command Help: help c \n To change the Console Language to Turkish: L TR \nTo change the Console Language to English: L EN \n Current Language: {Language}"
            print(colorama.Fore.GREEN + "Success" + colorama.Fore.WHITE)
    elif line == "help c":
        print(HelpCommand)
    elif line == "pc shutdown":
        os.system("shutdown /s /t 0")
    elif line == "pc restart":
        os.system("shutdown /r /t 0")
    elif line == "history":
        for i in range(len(history)):
            print(history[i], "\n")
    elif line == "svr install":
        installname = input("$svrdownlandSVC::")
        if installname in svrtoollist:
            try:
                try:
                    os.mkdir(f"svrmods")
                except:
                    pass
                print(f"Trying to downloand {installname}")
                if installname == "gamertool":
                    
                    print("Writing on new python file ... : svrmods/gamertool.py")

                    with open("svrmods/gamertool.py", "w", encoding="utf-8") as gamertool_file:
                        gamertool_file.write(gamertoolindex)

            except Exception as e:
                print(colorama.Fore.RED + f"Failed: {e}" + colorama.Fore.WHITE)
    # CREATE FILE
    elif line == "create ?" or line == "create help":
        print(colorama.Fore.BLUE + colorama.Back.YELLOW + AllCreateCommands + colorama.Back.RESET + colorama.Fore.RESET)
    elif line == "create file":
        Temp1 = input("File Extention > ")
        os.system(f"echo Voider File > FileReady.{Temp1}")
    elif line == "create folder":
        os.system("md FolderReady")
    elif line == "create project":
        try:
            print(colorama.Fore.CYAN + colorama.Back.BLUE +"|==================| Voider Project Wizard |==================|" + colorama.Fore.RESET + colorama.Back.RESET)
            projectname = input(colorama.Fore.LIGHTMAGENTA_EX + "Project Name: ")
            dowebsitetemplate = input("Website Template [0/1]: ")
            if dowebsitetemplate != "1":
                projecttype = input("Main File Name: ")
                projectextention = input("extension: ")
            doreadmetext = input("README.txt file [0/1]: ")
            datafolder = input("DATA Folder [0/1]: ")
            if dowebsitetemplate == "1":
                dojsfile = input(".js file [0/1]: ")
                docssfile = input(".css file [0/1]: ")
            if " " in projectname:
                print("Don't use ' ' space because it may cause issues")
                input("Press Enter To Close")
                exit()

            print(f"Creating folder: {projectname}")
            os.mkdir(projectname)

            if doreadmetext == "1":
                with open(f"{projectname}/README.txt", "w") as readme:
                    readme.write("By Voider\n")

            if datafolder == "1" and dowebsitetemplate != "1":
                print(f"Creating folder: {projectname}/Data")
                os.mkdir(f"{projectname}/Data")
            if dowebsitetemplate == "1":
                print(f"Creating Website Template: {projectname}/Website")
                os.mkdir(f"{projectname}/Website")

                print(f"Creating JS Folder: {projectname}/Website/js/")
                os.mkdir(f"{projectname}/Website/js")

                print(f"Creating CSS Folder: {projectname}/Website/css/")
                os.mkdir(f"{projectname}/Website/css")


                print(f"Creating Website File: {projectname}/Website/index.html")
                with open(f"{projectname}/Website/index.html", "w") as website:
                    website.write(htmlsamplewebsite)

                if dojsfile == "1":
                    print(f"Creating folder js: {projectname}/Website/js/")
                    with open(f"{projectname}/Website/js/script.js", "w") as jsfile:
                        jsfile.write("console.log('Hello World!')")

                if docssfile == "1":
                    print(f"Creating Website CSS: {projectname}/Website/css/style.css")
                    with open(f"{projectname}/Website/css/style.css", "w") as cssfile:
                        cssfile.write(csssamplewebsite)

            if dowebsitetemplate != "1":
                print(f"Creating file: {projectname}/{projecttype}.{projectextention}")
                filename = f"{projectname}/{projecttype}.{projectextention}"
                with open(filename, "w"):
                    pass
            print("Success" + colorama.Fore.WHITE)
        except Exception as e:
            print(colorama.Fore.RED + f"Failed: {e}" + colorama.Fore.WHITE)
    elif line == "clear" or line == "cls":
        os.system('cls')
    elif line == "create":
        print("Incorrect Usage For 'create' : \n create file \n create folder \n create project")
    elif line == "create zip":
        print("building | ZIP")
        with open(f"ReadyFile.zip", "w") as zipfile:
            zipfile.write(zipfileindex)
        print("success on building zip file ... ")
    else:
        if line != "":
            print(colorama.Fore.RED + ErrorCommandNotFound + colorama.Fore.WHITE)