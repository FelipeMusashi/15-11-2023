import re

def extrair_informacoes(texto):
    padrao_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails_encontrados = re.findall(padrao_email, texto)

    return {
        'emails': emails_encontrados
    }
texto_exemplo = """
Ola meu e-mail e usuario@example.com.
"""
informacoes = extrair_informacoes(texto_exemplo)
print("E-mails encontrados:")
print(informacoes['emails'])
