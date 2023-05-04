import socket
import ipaddress
import time

start_time = time.time()

ports_str = open("ports.txt")
ports = ports_str.read().strip().split(", ")
hosts = open("hosts.txt")
results_file = open("scan_results.txt","w")

for host in hosts:
    host = host.rstrip()

    try:
        ipaddress.IPv4Address(host)

    except:
        print(f"{host}: Invalid IP address")
        results_file.write(f"{host}: Invalid IP address\n")

    else:
        print (f"Ожидай, идет сканирование портов для {host}")        
        for port in list(ports):    
            s = socket.socket()    
            s.settimeout(1)   
            try:    
                s.connect((host, int(port)))    
            except socket.error:    
                #results_file.write(f"{host}:{port} порт закрыт\n")
                pass
            else:
                results_file.write(f"{host}:{port} порт активен\n")
                print(f"{host}: {port} порт активен")    
                s.close()
        print ("Сканирование завершено!")
  

hosts.close()
results_file.close()


end_time = time.time()
print("Run time: {:.2f} seconds".format(end_time - start_time))