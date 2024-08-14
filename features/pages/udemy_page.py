from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class UdemyPage(BasePage):
    BOTAO_GLOBO = (By.CSS_SELECTOR, '.ud-btn.ud-btn-medium')
    BOTAO_INGLES = (By.CSS_SELECTOR, '.ud-btn.ud-btn-medium.ud-btn-ghost.ud-text-md')
    BOTAO_REGISTRO = (By.CSS_SELECTOR, '#div:nth-child(9) > a > span')
    BOTAO_BUSINESS = (By.CSS_SELECTOR, '#u34-popper-trigger--8')

    def clicar_botao_globo(self):
        botao_globo = self.find_element(*self.BOTAO_GLOBO)
        botao_globo.click()

    def clicar_botao_ingles(self):
        botao_ingles = self.find_element(*self.BOTAO_INGLES)
        botao_ingles.click()
    
    def recuperar_texto_botao_registro(self):
        self.find_element(*self.BOTAO_REGISTRO)
        return self.get_element_text(self.find_element(*self.BOTAO_REGISTRO))
    
    def clicar_botao_business(self):
        botao_business = self.find_element(*self.BOTAO_BUSINESS)
        botao_business.click()
    


