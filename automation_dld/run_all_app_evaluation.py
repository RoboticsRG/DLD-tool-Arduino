import os
import subprocess
import time

def listar_projetos(dir):
    lista_projeto = []
    for nome in os.listdir(dir):
        file_name = os.path.join(dir, nome)
        lista_projeto.append(file_name)
    return lista_projeto


dir = "/home/davi/projetos_git/apks"
list = listar_projetos(dir)

# cont = 0
# for l in list:
#     cont +=1
#     print(l)
# print(cont)
    # list_test = []
    # list_test.append("/home/davi/projetos_git/apks/Conversations_v1.14.0.apk")
    # list_test.append("/home/davi/projetos_git/apks/Amaze_File_Manager_v3.1.0-beta.1.apk")
    # list_test.append("/home/davi/projetos_git/apks/BeeCount_v2.4.7.apk")
    # 3 horas 2250 .json
for l2 in list:
    inicio = time.time()

    dir_out = "/home/davi/projetos_git/out_teste"
    nome = l2.split("/")[5].split(".apk")[0]
    nome = nome.replace(" ", "\ ")
    l2=l2.replace(" ","\ ")

    # print nome
    comando = "dld -a {} -o {}/{} -grant_perm -is_emulator -count 5 -robot".format(l2, dir_out, nome)
    print(comando)

    # os.popen(comando).read()
    time.sleep(10)
    process = subprocess.Popen(comando, shell=True)
    # process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # process.
    output, error = process.communicate()

    fim = time.time()

    print("Tempo em horas {}".format((fim-inicio)/3600))
