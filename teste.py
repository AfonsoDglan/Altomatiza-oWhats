import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import urllib
from random import randint



contatos = pd.read_csv("teste.csv", encoding="UTF-8");
print(contatos);
navegador = webdriver.Chrome(ChromeDriverManager().install());
navegador.get("https://web.whatsapp.com/");
sleep(30);
def buscar_contato(contato):
    pesquisa = navegador.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]');
    sleep(3);
    pesquisa.click();
    pesquisa.send_keys(contato);
    pesquisa.send_keys(Keys.ENTER);
    sleep(3);

def enviar_mensagem(mensagem):
    campo_msg = navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]');
    campo_msg.click();
    sleep(3);
    campo_msg.send_keys(mensagem);
    campo_msg.send_keys(Keys.ENTER);
for i,nome in enumerate(contatos["First Name"]):
    msg = f"""fala {nome}. Um Teste ai https://web.whatsapp.com/""";
    print(nome )
    buscar_contato(nome);
    sleep(3);
    enviar_mensagem(msg);
    sleep(3);