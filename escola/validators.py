import re # importa o regex
from validate_docbr import CPF

def cpf_invalido(numero_cpf):
    cpf = CPF()
    cpf_valido = cpf.validate(numero_cpf)
    return not cpf_valido

def nome_invalido(nome):
        return not nome.isalpha()

def celular_invalido(celular):
       # 86 99999-9999
        modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}' #[0-9] define o intervalo e {numero} quantos digitos 
        resposta = re.findall(modelo,celular)
        #print(resposta)
        return not resposta


       
       
        ''' return len (celular) != 13 #and not celular.isdigit() 
       # return len (celular) != 13'''

'''if len(dados['cpf']) != 11:
            raise serializers.ValidationError({'cpf':'O CPF deve possuir 11 digitos'})
        if not dados['nome'].isalpha():
            raise serializers.ValidationError({'nome':'O nome deve conter apenas letras.'})
        if not dados['celular'].isdigit():
            raise serializers.ValidationError({'celular':'O celular deve conter apenas números.'})
        if len(dados['celular']) != 13:
            raise serializers.ValidationError({'celular':'O celular deve ter 13 dígitos.'})'''