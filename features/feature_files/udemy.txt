Feature: Funcionalidades da pagina inicial

### Udemy bloqueia pedindo verificação de pessoa
#        @CampoDePesquisa
#          Scenario: Teste do campo de pesquisa
 #           Given que o usuário está na tela inicial
 #            When ele pesquisar gherkin
 #            Then deve ser encaminhado para a página de resultados da pesquisa

        @TesteModalIdiomas
        Scenario: Verificar modal de idiomas
            Given que o usuário deve estar na tela inicial do site
             When ele clicar no botão de idioma da página
             Then surgirá o modal de idiomas
             