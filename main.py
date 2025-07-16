# Instalar o Playwright -> pip3 install playwright
# Instalar "engines" do Playwright -> playwright install

# abrir um navegador
from playwright.sync_api import sync_playwright, expect

# Cria instancia do navegador
# Para visualizar o navegador, coloque headless=False como parâmetro
with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False)
    contexto = navegador.new_context() # Permite gerenciar abas

    # Abre o navegador com uma página
    pagina = contexto.new_page()

    # Navegar para uma página
    pagina.goto('https://www.hashtagtreinamentos.com/')

    # pegar infos da página
    print(pagina.title())

    # Selecionando elementos no playwright
    # Use o gerador de códigos do playwright para selecionar elementos
    # -> playwright codegen website.com

    # 1ª forma -> xpath (não recomendado para o Playwright)
    # pagina.locator('xpath=/html/body/main/section[1]/div[2]/a').click()

    # 2ª forma -> .get_by
    # O expect_page() permite que a segunda página carregue apropriadamente
    # Permite que as informações sejam carregadas de maneira correta e armazenadas na variável pagina2_info
    botao = pagina.locator("div").filter(has_text="Torne-se uma referência no").get_by_role("link")
    with contexto.expect_page() as pagina2_info: # Útil se caso o botão for levar para outra página
        botao.click()
    pagina2 = pagina2_info.value
    pagina2.goto('https://www.hashtagtreinamentos.com/curso-python')

    # Preenchendo o formulário do curso de python
    pagina2.get_by_role("textbox", name="Seu primeiro nome").fill('Elestaodiolhoemnois')
    pagina2.get_by_role("textbox", name="Seu melhor e-mail").fill('exemplo@exemplo.com')
    pagina2.get_by_role("textbox", name="Seu WhatsApp com DDD").fill('55 55555 5555')
    pagina2.get_by_role("button", name="Quero acessar as informações").click()

    # Esperar um elemento na tela - importar função expect (Opcional)
    botao_inscricao = pagina2.get_by_role("link", name="quero garantir uma vaga")
    expect(botao_inscricao).to_be_visible()
    botao_inscricao.click()

    # Selecionar vários elementos
    # Este comando cria uma lista com todas as divs do site
    # divs = pagina.locator('div').all()

    # Fecha a página no final dos processos
    navegador.close()