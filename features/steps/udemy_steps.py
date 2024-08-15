from behave import given, when, then
from features.pages.udemy_page import UdemyPage
import time

# region Verificar modal de idiomas
@given(u'que o usuário deve estar na tela inicial do site')
def step_impl(context):
    context.driver.get("https://www.udemy.com")
    context.udemy_page = UdemyPage(context.driver)
    time.sleep(20)

@when(u'ele clicar no botão de idioma da página')
def step_impl(context):
    context.udemy_page.clicar_botao_idioma()
    time.sleep(10)

@then(u'surgirá o modal de idiomas')
def step_impl(context):
    texto_obtido = context.udemy_page.retornar_botao_english()
    assert texto_obtido == 'English', f"O texto obtido '{texto_obtido}' foi diferente do texto esperado 'English'"
    time.sleep(10)
    
# endregion