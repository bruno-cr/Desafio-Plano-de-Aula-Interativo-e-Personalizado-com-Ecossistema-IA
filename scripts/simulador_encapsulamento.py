from scapy.all import IP, TCP, Ether, Raw

def simular_jornada_do_pacote():
    print("--- Iniciando Simulação de Encapsulamento (Modelo OSI) ---")

    # 1. Camada de Aplicação (Dados brutos)
    dados = "Mensagem: Ola, esta e uma aula de Redes de Computadores!"
    payload = Raw(load=dados)
    print(f"\n[Camada 7 - Aplicacao] Dados gerados: {dados}")

    # 2. Camada de Transporte (TCP)
    # Definindo portas de origem e destino
    segmento_tcp = TCP(sport=443, dport=80) / payload
    print(f"[Camada 4 - Transporte] Header TCP adicionado (Portas 443 -> 80)")

    # 3. Camada de Rede (IP)
    # Definindo IPs de origem e destino
    pacote_ip = IP(src="192.168.1.10", dst="8.8.8.8") / segmento_tcp
    print(f"[Camada 3 - Rede] Header IP adicionado (IP Origem: 192.168.1.10)")

    # 4. Camada de Enlace (Ethernet)
    # Definindo endereços MAC
    quadro_ethernet = Ether(src="aa:bb:cc:dd:ee:ff", dst="00:11:22:33:44:55") / pacote_ip
    print(f"[Camada 2 - Enlace] Header Ethernet adicionado (MAC Destino: 00:11:22:33:44:55)")

    print("\n--- Pacote Finalizado para Envio (Binario) ---")
    print(quadro_ethernet.summary())
    
    # Exibe a estrutura detalhada de camadas
    print("\n--- Visualizacao Detalhada (Encapsulamento) ---")
    quadro_ethernet.show()

if __name__ == "__main__":
    simular_jornada_do_pacote()
