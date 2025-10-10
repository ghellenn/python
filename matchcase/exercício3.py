def verificaFeriado(mes, dia):
    match mes:
        case 9:
            match dia:
                case 7:
                    print(f"Dia {dia} é idependencia do Brasil!")
                case _:
                    print("Este dia nao existe")
        case 10:
            match dia:
                case 12:
                    print(f"Dia {dia} é dia das crianças")
                case _:
                    print("Este dia nao existe")


def main():
    dia = int(input("Digite um dia do mes."))
    mes = int(input("Digite o mes."))

    verificaFeriado(mes, dia)

if __name__ == '__main__':
    main()