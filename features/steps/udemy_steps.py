from behave import given, when, then
from features.pages.udemy_page import UdemyPage
import time

# region Teste Mudança De Idioma
@given(u'que o usuário está na tela inicial')
def step_impl(context):
    context.driver.get("https://www.udemy.com")
    context.udemy_page = UdemyPage(context.driver)
    time.sleep(20)

@when(u'ele clicar no botão do globo')
def step_impl(context):
    context.udemy_page.clicar_botao_globo()
    time.sleep(2)


@when(u'clicar no botão de lingua espanhola')
def step_impl(context):
    context.udemy_page.clicar_botao_espanhol()
    time.sleep(5)

@then(u'a tela inicial deve atualizar em espanhol')
def step_impl(context):
    texto_obtido = context.udemy_page.recuperar_texto_botao_registro()
    assert texto_obtido == 'Regístrate', f"O texto obtido '{texto_obtido}' foi diferente do texto esperado 'Regístrate'"

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