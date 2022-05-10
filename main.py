from netmiko import ConnectHandler
from getpass import getpass
import time

def exc_comand(ip_add:list,user:str,passw:str):

    for ip in ip_add:
        #Conexion SSH
        ssh = ConnectHandler(device_type="cisco_ios",host=ip, port=22,username=user,password=passw)

        #Comando único
        out = ssh.send_command("sh cdp neighbors")
        print(ssh.find_prompt())
        print("sh cdp neighbors:\n" + out)
        time.sleep(5)
        ssh.disconnect()

    return '¡Configuración realizada con éxito!'

def run():
    #Autenticación
    ip =  list(input("Introduzca las IPs, separados por comas: ").split(','))
    user = input("Introduzca el usuario: ")
    passw = getpass("Introduzca contraseña: ")
    print(exc_comand(ip,user,passw))

if __name__ == '__main__':
    run()
