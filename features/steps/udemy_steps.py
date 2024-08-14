from behave import given, when, then
from features.pages.udemy_page import UdemyPage
import time

# region Teste do campo de pesquisa
@given(u'que o usuário está na tela inicial')
def step_impl(context):
    context.driver.get("https://www.udemy.com")
    context.udemy_page = UdemyPage(context.driver)
    time.sleep(20)

@when(u'ele escrever gherkin no campo')
def step_impl(context):
    context.udemy_page.escrever_texto_campo_pesquisa()
    time.sleep(10)


@when(u'pressionar a primeira sugestão surgida abaixo')
def step_impl(context):
    context.udemy_page.clicar_autocomplete()
    time.sleep(15)

@then(u'deve ser encaminhado para a página de resultados da pesquisa')
def step_impl(context):
    texto_obtido = context.udemy_page.recuperar_texto_resultado()
    assert texto_obtido == '112 resultados para “gherkin”', f"O texto obtido '{texto_obtido}' foi diferente do texto esperado '112 resultados para “gherkin”'"

# endregion

# region Teste verificar acesso a página de inscrição do “Udemy Business”
#@when(u'ele clicar no botão “Udemy Business”')
#def step_impl(context):
    #context.udemy_page.clicar_botao_business()
    #time.sleep(2)

#@then(u'deve ser encaminhado para a tela de inscrição do “Udemy Business”')
#def step_impl(context):
    #context.udemy_page.clicar_botao_globo()
    #time.sleep(2)

# endregion