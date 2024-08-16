Feature: Funcionalidades do menu superior

        @TesteMenuPessoas
        Scenario: Testando a pesquisa do menu Pessoas
            Given que o usuário está na página inicial
             When clicar no menu Pessoas
             When digitar o nome
             When digitar o sobrenome e clicar ENTER
             When clicar no resultado da busca
             Then o modal de login/cadastro para ver o perfil completo aparece
        
        @TesteMenuLearning
        Scenario: Testando a pesquisa do menu Learning
            Given que o usuário está na página inicial
             When clicar no menu Learning
             When digitar Power Bi e clicar ENTER
             When clicar no resultado da busca
             When clicar no botão PLAY
             Then o vídeo é reproduzido
    