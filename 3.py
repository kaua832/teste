tarefas = []

while True:
    
    print("\n--- GERENCIADOR DE TAREFAS ---")
    print("1. Adicionar | 2. Listar | 3. Concluir | 4. Remover | 5. Sair")
    opcao = input("Escolha: ")

    match opcao:
        case "1":
            nova_tarefa = input("Nova tarefa: ")
            if nova_tarefa:
                tarefas.append(f"não concluida {nova_tarefa}")
                #adicionar a tarefa na lista tarefas[]
        case "2":
            print("\n--- TAREFAS ---")
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}")
                #o for le a lista de tarefas
                #i guarda o numero da linha da tarefa
                #o enumerate enumera as tarefas começando do 1

        case "3":
            num = int(input("Número da tarefa concluída: "))
            tarefas[num - 1] = tarefas[num - 1].replace("não concluida", "concluida")
            #-1 para selecionar a opçao real da tarefa
            #.replace pra trocar a string nao concluida pela string concluida

        case "4":
            num = int(input("Número da tarefa a remover: "))
            tarefas.pop(num - 1)
            #.pop pra remover um item da lista

        case "5":
            print("Até mais!")
            break

        case _:
            print("⚠️ Opção inválida!")