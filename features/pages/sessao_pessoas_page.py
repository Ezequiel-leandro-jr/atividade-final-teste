from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import time

class SessaoPessoasPage(BasePage):
    BOTAO_IDIOMA = (By.CSS_SELECTOR, "button.language-selector__button[aria-expanded='false']")
    BOTAO_ENGLISH = (By.CSS_SELECTOR, "button[aria-label='Română (Romeno)']")
    BOTAO_TRADUZIDO = (By.CSS_SELECTOR, "button.btn__primary--large.from__button--floating")
    
    def clicar_botao_idioma(self):
        botao_idioma = self.find_element(*self.BOTAO_IDIOMA)
        botao_idioma.click()
    
    def clicar_opcao_english(self):
        botao_english = self.find_element(*self.BOTAO_ENGLISH)
        botao_english.click()
    
    def retornar_texto_botao_english(self):
        botao_traduzido = self.find_element(*self.BOTAO_TRADUZIDO)
        texto_botao = botao_traduzido.text
        return texto_botao
        
        
    #def recuperar_texto_cadastro(self):
        #botao_cadastro = self.get_element_text(self.find_element(*self.BOTAO_CADASTRO))
        #return botao_cadastro
    
    
    #def escrever_texto_campo_pesquisa(self):
     #   formulario = self.find_element(*self.FORMULARIO)
      #  campo_pesquisa = formulario.find_element(By.CSS_SELECTOR, "input.ud-text-input.ud-text-input-small.ud-text-sm.ud-search-form-autocomplete-input.js-header-search-field")
       # campo_pesquisa.send_keys('gherkin')
        #campo_pesquisa.send_keys(Keys.ENTER)
