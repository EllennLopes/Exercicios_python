def fazer_quiz():
    questions = [
        {
            "question": "O que é um algoritmo?",
            "options": [
                "a) Uma linguagem de programação", 
                "b) Uma sequência de instruções para resolver um problema", 
                "c) Um erro de sintaxe no código",
                "d) Um tipo de variável"
            ],
            "answer": "b"
        },
        {
            "question": "O que é uma variável na programação?",
            "options": [
                "a) Uma função que repete comandos", 
                "b) Um valor fixo no programa", 
                "c) Um espaço de memória para armazenar dados",
                "d) Um comando de saída de dados"
            ],
            "answer": "c"
        },
        {
            "question": "Qual estrutura usamos para repetir comandos?",
            "options": [
                "a) if",
                "b) else",
                "c) while/for",
                "d) def"
            ],
            "answer": "c"
        },
        {
            "question": "Qual é a função de um condicional if em um algoritmo?",
            "options": [
                "a) Repetir ações",
                "b) Definir uma função",
                "c) Armazenar dados",
                "d) Fazer comparações e tomar decisões"
            ],
            "answer": "d"
        }
    ]
    score = 0
    
    for question in questions: 
        print("\n" + question["question"])
        for option in question["options"]:
            print(option)
        
        user_answer = input("Enter the letter corresponding to your answer: ").lower()
        if user_answer == question["answer"]:
            print("Correct answer!")
            score += 1 
        else:
            print("Wrong answer!")
    
    print(f"\nYou got {score} out of {len(questions)} questions right.")

fazer_quiz()


   
               
              