Feature: Funcionalidades da pagina inicial

    @TesteSimples
    Scenario: teste de mudança de idioma do site
        Given que o usuário está na tela inicial
        When ele clicar no botão do globo
        When clicar no botão “Español”
        Then a tela inicial deve atualizar em espanhol

    @TesteSimples
    Scenario: verificar acesso a página de inscrição do “Udemy Business”
        Given que o usuário deve estar na tela inicial do site
        When ele clicar no botão “Udemy Business”
        Then deve ser encaminhado para a tela de inscrição do “Udemy Business”