from behave import given, when, then
from features.pages.sessao_pessoas_page import SessaoPessoasPage
import time

# region Testar a mudança do idioma
@given(u'que o usuário está na sessão Pessoas')
def step_impl(context):
    context.driver.get("https://br.linkedin.com")
    context.linkedin_page = SessaoPessoasPage(context.driver)
    time.sleep(50)

@when(u'clicar no dropdown idioma')
def step_impl(context):
    context.linkedin_page.clicar_botao_idioma()
    time.sleep(20)

@when(u'clicar na opção de ingles')
#def step_impl(context):
#    context.linkedin_page.clicar_opcao_english()
#    time.sleep(10)

@then(u'a página mudará para o idioma selecionado')
def step_impl(context):
    texto_obtido = context.linkedin_page.retornar_texto_botao_english()
    assert texto_obtido == 'Sign in', f"O texto obtido '{texto_obtido}' foi diferente do texto esperado 'Sign in'"
    time.sleep(10)
    
# endregion