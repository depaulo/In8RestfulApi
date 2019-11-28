# In8RestfulApi
    Bom dia a quem estiver lendo.
Como pedido eu criei um arquivo bem simples, acredito que mais que isso não seria necessario ou iria me demandar muito tempo.

    Os requerimentos para o projeto estão no arquivo.

1-Executar o arquivo.
2-Eu fiz cinco comandos para o Api, dois no endereço '/' methods=['GET', 'POST'], e tres no endereço '/biblioteca' methods=['GET', 'PUT', 'DELETE'].

    1) Endereço = '/' , method = 'GET', sem parametros. 
    Resultado: A lista de livros.
    
    2) Endereço = /' , method = 'POST'. Parametros numero, titulo, autor, edicao. 
    Resultado: Cadastrar livros.
    
    3) Endereço = /biblioteca' , method = 'GET', Parametros numero. 
    Resultado: Se o livro esta na bibioteca ou não.
    
    4) Endereço = /biblioteca' , method = 'PUT'. Parametros numero, titulo, autor, edicao. 
    Resultado: Atualizar as informações do livro.
    
    5) Endereço = /biblioteca' , method = 'DELETE'. Parametros numero. Resultado: Apagar o livro.
