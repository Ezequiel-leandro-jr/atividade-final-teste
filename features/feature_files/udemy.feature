Feature: Funcionalidades da pagina inicial


        @TesteSimples
        Scenario: Teste do campo de pesquisa
            Given que o usuário está na tela inicial
             When ele escrever gherkin no campo
             When pressionar a primeira sugestão surgida abaixo
             Then deve ser encaminhado para a página de resultados da pesquisa

        #@TesteSimples2
        #Scenario: verificar acesso a página de inscrição do Udemy Business
            #Given que o usuário deve estar na tela inicial do site
             #When ele clicar no botão da Udemy Business
             #Then deve ser encaminhado para a tela de inscrição do Udemy Business