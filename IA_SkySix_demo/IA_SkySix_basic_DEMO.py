# IA_SkySix_basic.py
# Versão demo simplificada - apenas comandos básicos, sem integração online, sem IA avançada.

def saudacao():
    print("Olá! Eu sou a IA_SkySix versão demo.")
    print("Para mais funcionalidades, adquira a versão completa no GitHub.")

def comando_simples():
    comando = input("Diga algo simples (ex: 'hora', 'data', 'sair'): ").lower()

    if comando == 'hora':
        from datetime import datetime
        print(f"Hora atual: {datetime.now().strftime('%H:%M:%S')}")
    elif comando == 'data':
        from datetime import datetime
        print(f"Data de hoje: {datetime.now().strftime('%d/%m/%Y')}")
    elif comando == 'sair':
        print("Encerrando demo. Obrigado!")
        return False
    else:
        print("Comando não reconhecido na versão demo.")
    return True

def main():
    saudacao()
    ativo = True
    while ativo:
        ativo = comando_simples()

if __name__ == "__main__":
    main()
