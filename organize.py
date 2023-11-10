#importe os módulos os e shutil
import os
import shutil


#crie duas variáveis, from_dir e to_dir para receberem os respectivos caminhos
from_dir = "./assets"
to_dir = "./"


#crie uma variável list_of_files que receberá um lista de todos os arquivos do diretório de origem (from_dir)
#imprima o que tem na lista de arquivos
list_of_files = os.listdir(from_dir)
print(list_of_files)
#faça um loop for para percorrer a lista de arquivos 
for file in list_of_files:

    #crie duas variáveis para receber o caminho e extensão dos arquivos respectivamente
    name, ext = os.path.splitext(file)
    
    
    #verifique se a extensão está vazia, se estiver, ignore
    if ext == "" :
        continue
    #Verifique se a extensão é uma imagem
    if ext in [".jpg", ".jpeg", ".png", ".gif",".jfif"]:
    
        #se a extensão for uma imagem, crie 3 variáveis de pasta path1... 
        path1 = from_dir + "/" + file
        path2 = to_dir + "/" + "images" 
        path3 = to_dir + "/"  + "images" + "/" + file

        
        #se path2 existir, mova o arquivo para path3
        if os.path.exists(path2):
            print(f"movendo {file}...")
            shutil.move(path1,path3)
             
            

        #caso contrário, crie a path2 e mova o arquivo para path3
        else:
            os.makedirs(path2)
            print(f"movendo {file}...")
            shutil.move(path1,path3)
        
        
#Fim
        
        