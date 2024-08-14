from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class UdemyPage(BasePage):
    CAMPO_PESQUISA = (By.CSS_SELECTOR, '#u369-search-form-autocomplete--3')
    RESULTADO_TEXTO = (By.CSS_SELECTOR, 'main-content-anchor > header > h1')
    #BOTAO_BUSINESS = (By.CSS_SELECTOR, '#u34-popper-trigger--8')

    def escrever_texto_campo_pesquisa(self):
        campo_pesquisa = self.find_element(*self.CAMPO_PESQUISA)
        campo_pesquisa.send_keys('gherkin')
        campo_pesquisa.send_keys(Keys.ENTER)
    
    def recuperar_texto_resultado(self):
        self.find_element(*self.RESULTADO_TEXTO)
        return self.get_element_text(self.find_element(*self.RESULTADO_TEXTO))
    
    def clicar_botao_business(self):
        botao_business = self.find_element(*self.BOTAO_BUSINESS)
        botao_business.click()
    


