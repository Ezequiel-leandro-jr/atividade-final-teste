from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class UdemyPage(BasePage):
    BOTAO_IDIOMA = (By.CSS_SELECTOR, "button.ud-btn.ud-btn-medium.ud-btn-secondary.ud-heading-sm.ud-btn-icon.ud-btn-icon-medium")
    MODAL = (By.CSS_SELECTOR, ".modal-language-selector-module--modal--58pzd.ud-modal")
    
    def clicar_botao_idioma(self):
        botao_idioma = self.find_element(*self.BOTAO_IDIOMA)
        botao_idioma.click()
    
    def retornar_botao_english(self):
        modal = self.find_element(*self.MODAL)
        botao_english = modal.find_element(By.XPATH, "//a[span[text()='English']]")
        return botao_english.text
        
        
    #def recuperar_texto_cadastro(self):
        #botao_cadastro = self.get_element_text(self.find_element(*self.BOTAO_CADASTRO))
        #return botao_cadastro
    
    
    #def escrever_texto_campo_pesquisa(self):
     #   formulario = self.find_element(*self.FORMULARIO)
      #  campo_pesquisa = formulario.find_element(By.CSS_SELECTOR, "input.ud-text-input.ud-text-input-small.ud-text-sm.ud-search-form-autocomplete-input.js-header-search-field")
       # campo_pesquisa.send_keys('gherkin')
        #campo_pesquisa.send_keys(Keys.ENTER)


