# Casos de Teste - Back-End ✨

### **ID Caso de Teste**: #0
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste Geração Token de Autenticação.
<br>**Descrição:** Realizar Teste na Rota de Geração do Token de Autenticação.
<br>**Pré-Condição:** Possuir credenciais do sistema para gerar o token de autenticação.
<br>**Passo-a-Passo:** Realizar um método POST na rota http://localhost:9091/auth/realms/dfmicroservices/protocol/openid-connect/token, informando no um Form-URL encoded com os campos "grant_type":password, "username":front-end-web, "password":1329 e no header da request o campo "Authorization":Basic ZnJvbnQtZW5kLXByb2R1Y3Q6.
<br>**Resultado Esperado:** Gerar o Token de Autenticação para poder realizar chamadas nas outras rotas.
<br>**Status:** APROVADO
<br>**Report Do Bug:** Nennhum

Print do Teste #0
![Print do Teste #0](PrintsCasosDeTeste/CasoTeste00.png)

<br>

Testes - MicroServiço Produto
<br>

### **ID Caso de Teste**: #1
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste cadastro de produto.
<br>**Descrição:** Realizar teste na rota de cadastro de produto.
<br>**Pré-Condição:** Estar autenticado no sistema.
<br>**Passo-a-Passo:** Realizar um método POST na rota https://localhost:8080/dona-frost/v1/product, informando no header da requisição o campo "Authorization" com o Token de autenticação do tipo Bearer, este que foi gerado no Teste#01, também o campo "Content-Type":application/json, e um json com um body similar ao exemplo abaixo.
Ex de body:
```json
{
  "active": true,
  "description": "Lasanha",
  "discount": 2,
  "imageUri": "http://www.gishub.com/teste123",
  "name": "Lasanha",
  "plateSize": "INDIVIDUAL",
  "category": "VEGETARIAN",
  "price": 8.00
}
```
>**Resultado Esperado:** Cadastrar produto na base de dados.
<br>**Status:** APROVADO
<br>**Report Do Bug:** Nenhum

Print do Teste #1
![Print do Teste #1](PrintsCasosDeTeste/CasoTeste01.png)

---

### **ID Caso de Teste**: #2
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste atualização/update de produto.
<br>**Descrição:** Realizar teste na rota de update mudando todos os campos de um produto existente, com base em seu id.
<br>**Pré-Condição:** Estar autenticado no sistema, existir um produto na base de dados.
<br>**Passo-a-Passo:** Realizar um método PUT na rota https://localhost:8080/dona-frost/v1/product, informar no header o campo "Authorization" com o Token de autenticação do tipo Bearer, este que foi gerado no Teste#01, também no header o campo "id" com o número do produto a ser alterado e o campo "Content-Type":application/json, no body da request informar um json similar ao exemplo abaixo.
Ex de body:
```json
{
  "description": "Apenas mais outro",
  "discount": 3,
	"category":"NO_GLUTEN",
	"active":false
}
```
>**Resultado Esperado:** Atualização dos campos de um produto existente na base de dados.
<br>**Status:** APROVADO
<br>**Report Do Bug:** Nennhum

Print do Teste #2
![Print do Teste #2](PrintsCasosDeTeste/CasoTeste02.png)

---

### **ID Caso de Teste**: #3
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste deleção de produto.
<br>**Descrição:** Realizar teste na rota de delete em um produto existente, com base em seu id.
<br>**Pré-Condição:** Estar autenticado no sistema, existir um produto na base de dados.
<br>**Passo-a-Passo:** Realizar um método DELETE na rota https://localhost:8080/dona-frost/v1/product, informar no header o campo "Authorization" com o Token de autenticação do tipo Bearer, este que foi gerado no Teste#01, também no header o campo "id" com o número do id do produto a ser deletado.
<br>**Resultado Esperado:** Remover o produto informado.
<br>**Status:** APROVADO
<br>**Report Do Bug:** Nennhum

Print do Teste #3
![Print do Teste #3](PrintsCasosDeTeste/CasoTeste03.png)

---

### **ID Caso de Teste**: #4
>**Prioridade**: Baixa.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste listagem de todos os produtos.
<br>**Descrição:** Realizar teste na rota listagem de produtos.
<br>**Pré-Condição:** Estar autenticado no sistema, existir mais de um produto na base de dados.
<br>**Passo-a-Passo:** Realizar um método GET na rota https://localhost:8080/dona-frost/v1/product, informar no header o campo "Authorization" com o Token de autenticação do tipo Bearer, este que foi gerado no Teste#01.
<br>**Resultado Esperado:** Listar todos os produtos da base de dados.
<br>**Status:** APROVADO
<br>**Report Do Bug:** Nennhum

Print do Teste #4
![Print do Teste #4](PrintsCasosDeTeste/CasoTeste04.png)

---

<br>
Testes - MicroServiço Usuário
<br>

### **ID Caso de Teste**: #5
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste cadastro de usuário.
<br>**Descrição:** Realizar teste na rota de cadastro de usuário.
<br>**Pré-Condição:** Estar autenticado no sistema.
<br>**Passo-a-Passo:** Realizar um método POST na rota https://localhost:8081/dona-frost/v1/user, informando no header da requisição o campo "Authorization" com o Token de autenticação do tipo Bearer, este que foi gerado no Teste#01, também o campo "Content-Type":application/json, e um json com um body similar ao exemplo abaixo.
Ex de body:
```json
{
	"active": true,
	"address": {
		"active": true,
		"city": "Cascavel",
		"district": "Centro",
		"latitude": 4343434,
		"longitude": 4545454,
		"main": true,
		"number": 33,
		"numberAp": 21,
		"state": "PR",
		"street": "Blue baron"
	},
	"document": "10564574902",
	"email": "sandro@hotmail.com",
	"name": "sandro matheus ramos",
	"password": "13291329",
	"phone": "45991039812"
}
```
>**Resultado Esperado:** Cadastrar usuário na base de dados.
<br>**Status:** APROVADO
<br>**Report Do Bug:** Nenhum

Print do Teste #5
![Print do Teste #5](PrintsCasosDeTeste/CasoTeste05.png)

---

### **ID Caso de Teste**: #6
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste atualização/update de usuário.
<br>**Descrição:** Realizar teste na rota de update mudando todos os campos de um usuário existente, com base em seu id.
<br>**Pré-Condição:** Estar autenticado no sistema, existir um usuário na base de dados.
<br>**Passo-a-Passo:** Realizar um método PUT na rota https://localhost:8081/dona-frost/v1/user, informar no header o campo "Authorization" com o Token de autenticação do tipo Bearer, este que foi gerado no Teste#01, também no header o campo "idUser" com o número do id do usuário a ser alterado e o campo "Content-Type":application/json, no body da request informar um json similar ao exemplo abaixo.
Ex de body:
```json
{
	"document": "105640002122",
	"email": "brabo@hotmail.com",
	"name": "sandrolax o brabo",
	"password": "1329222",
	"acceptTerms":true,
	"active": false
}
```
>**Resultado Esperado:** Atualização dos campos de um usuário existente na base de dados.
<br>**Status:** APROVADO
<br>**Report Do Bug:** Nennhum

Print do Teste #6
![Print do Teste #6](PrintsCasosDeTeste/CasoTeste06.png)

---

### **ID Caso de Teste**: #7
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste deleção de usuário.
<br>**Descrição:** Realizar teste na rota de delete em um usuário existente, com base em seu id.
<br>**Pré-Condição:** Estar autenticado no sistema, existir um usuário na base de dados.
<br>**Passo-a-Passo:** Realizar um método DELETE na rota https://localhost:8081/dona-frost/v1/user, informar no header o campo "Authorization" com o Token de autenticação do tipo Bearer, este que foi gerado no Teste#01, também no header o campo "idUser" número do id do usuário a ser deletado.
<br>**Resultado Esperado:** Remover o usuário informado.
<br>**Status:** APROVADO
<br>**Report Do Bug:** Nennhum

Print do Teste #7 Parte 1
![Print do Teste #7_01](PrintsCasosDeTeste/CasoTeste07_01.png)

Print do Teste #7 Parte 2
![Print do Teste #7_02](PrintsCasosDeTeste/CasoTeste07_02.png)

---

### **ID Caso de Teste**: #8
>**Prioridade**: Baixa.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste listagem de todos os usuários.
<br>**Descrição:** Realizar teste na rota listagem de usuários.
<br>**Pré-Condição:** Estar autenticado no sistema, existir mais de um usuário na base de dados.
<br>**Passo-a-Passo:** Realizar um método GET na rota https://localhost:8081/dona-frost/v1/user, informar no header o campo "Authorization" com o Token de autenticação do tipo Bearer, este que foi gerado no Teste#01.
<br>**Resultado Esperado:** Listar todos os usuários da base de dados.
<br>**Status:** APROVADO
<br>**Report Do Bug:** Nennhum

Print do Teste #8
![Print do Teste #6](PrintsCasosDeTeste/CasoTeste07_02.png)

---

### **ID Caso de Teste**: #9
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste cadastro de um novo endereço para um usuário existente.
<br>**Descrição:** Realizar teste na rota de cadastro de um novo endereço para um usuário existente.
<br>**Pré-Condição:** Estar autenticado no sistema, existir um usuário.
<br>**Passo-a-Passo:** Realizar um método POST na rota https://localhost:8081/dona-frost/v1/address, informando no header da requisição o campo "Authorization" com o Token de autenticação do tipo Bearer, este que foi gerado no Teste#01, também o campo "idUser" com o número do id do usuário que será adicionado o novo endereço, e também o campo "Content-Type":application/json, e um json com um body similar ao exemplo abaixo.
Ex de body:
```json
{
	"active": true,
	"city": "Foz",
	"district": "Lapa",
	"latitude": 4343434,
	"longitude": 4545454,
	"main": true,
	"number": 22,
	"numberAp": 12,
	"state": "PR",
	"street": "dark baron"
}
```
>**Resultado Esperado:** Cadastrar o novo endereço a um usuário existente na base de dados.
<br>**Status:** APROVADO
<br>**Report Do Bug:** Nenhum

Print do Teste #9
![Print do Teste #9](PrintsCasosDeTeste/CasoTeste09.png)

---

### **ID Caso de Teste**: #10
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste atualização de um endereço existente.
<br>**Descrição:** Realizar teste na rota de update/atualização de um endereço de um usuário existente.
<br>**Pré-Condição:** Estar autenticado no sistema, existir um endereço na base de dados.
<br>**Passo-a-Passo:** Realizar um método PUT na rota https://localhost:8081/dona-frost/v1/address, informar no header o campo "Authorization" com o Token de autenticação do tipo Bearer, este que foi gerado no Teste#01, também no header o campo "idUser" com o número do id do usuário a ser alterado o endereço, "idAddress" o número do id do endereço, e o campo "Content-Type":application/json, no body da request informar um json similar ao exemplo abaixo.
Ex de body:
```json
{
	"active": false,
	"city": "Paranagua",
	"district": "Neva",
	"latitude": 232323,
	"longitude": 323232,
	"main": false,
	"number": 2323,
	"state": "PR",
	"street": "são gabriel"
}
```
>**Resultado Esperado:** Atualizar os campos do endereço informado na base de dados.
<br>**Status:** APROVADO
<br>**Report Do Bug:** Nenhum

Print do Teste #10
![Print do Teste #10](PrintsCasosDeTeste/CasoTeste10.png)

---

### **ID Caso de Teste**: #11
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste remoção/deleção de um endereço existente.
<br>**Descrição:** Realizar teste na rota de remoção/deleção em um endereço de um usuário existente.
<br>**Pré-Condição:** Estar autenticado no sistema, existir um endereço na base de dados.
<br>**Passo-a-Passo:** Realizar um método DELETE na rota https://localhost:8081/dona-frost/v1/address, informar no header o campo "Authorization" com o Token de autenticação do tipo Bearer, este que foi gerado no Teste#01, também no header o campo "idUser" número do id do usuário e "idAddress" número do id do endereço a ser deletado.
<br>**Resultado Esperado:** Deletar/Remover endereço informado da base de dados.
<br>**Status:** APROVADO
<br>**Report Do Bug:** Nenhum

Print do Teste #11
![Print do Teste #11](PrintsCasosDeTeste/CasoTeste11.png)

---

<br>
Testes - MicroServiço Marketplace
<br>

### **ID Caso de Teste**: #12
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste adicionar um produto ao carrinho do usuário.
<br>**Descrição:** Realizar teste na rota adição de produto no carrinho.
<br>**Passo-a-Passo:** Realizar um método POST na rota https://localhost:8082/dona-frost/v1/cart, informando no header da requisição o campo "Authorization" com o Token de autenticação do tipo Bearer, este que foi gerado no Teste#01, também o campo "idCart" com o número do id do carrinho que será adicionado o produto, "idProduct" com o número do id do produto a ser adicionado no carrinho e também o campo "quantity" com a quantidade a ser adicionada do produto escolhido.
<br>**Resultado Esperado:** Persistir um produto em um carrinho existente na base de dados.
<br>**Status:** APROVADO
<br>**Report Do Bug:** Nenhum

Print do Teste #12
![Print do Teste #12](PrintsCasosDeTeste/CasoTeste12.png)

---

### **ID Caso de Teste**: #13
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste adicionar quantidade a um produto no carrinho do usuário.
<br>**Descrição:** Realizar teste na rota adição de quantidade a um produto no carrinho.
<br>**Pré-Condição:** Estar autenticado no sistema e existir um carrinho com produto na base de dados.
<br>**Passo-a-Passo:** Realizar um método PUT na rota https://localhost:8082/dona-frost/v1/cart, informando no header da requisição o campo "Authorization" com o Token de autenticação do tipo Bearer, este que foi gerado no Teste#01, também o campo "idProductCart" com o número do id do Produto Carrinho que será adicionado quantidade do produto, o campo "quantity" com a quantidade a ser adicionada do Produto Carrinho escolhido.
<br>**Resultado Esperado:** Adicionar a quantidade informada a um produto em um carrinho existente na base de dados.
<br>**Status:** APROVADO
<br>**Report Do Bug:** Nenhum

Print do Teste #13
![Print do Teste #13](PrintsCasosDeTeste/CasoTeste13.png)

---

### **ID Caso de Teste**: #14
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste remover quantidade de um produto no carrinho do usuário.
<br>**Descrição:** Realizar teste na rota remoção de quantidade a um produto no carrinho.
<br>**Pré-Condição:** Estar autenticado no sistema e existir um carrinho com produto na base de dados.
<br>**Passo-a-Passo:** Realizar um método DELETE na rota https://localhost:8082/dona-frost/v1/cart, informando no header da requisição o campo "Authorization" com o Token de autenticação do tipo Bearer, este que foi gerado no Teste#01, também o campo "idProductCart" com o número do id do Produto Carrinho que será removida a quantidade do produto, o campo "quantity" com a quantidade a ser removida do Produto Carrinho escolhido.
<br>**Resultado Esperado:** Remover a quantidade informada de um produto em um carrinho existente na base de dados.
<br>**Status:** APROVADO
<br>**Report Do Bug:** Nenhum

Print do Teste #14
![Print do Teste #14](PrintsCasosDeTeste/CasoTeste14.png)

---

### **ID Caso de Teste**: #15
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste remover um produto carrinho do usuário.
<br>**Descrição:** Realizar teste na rota remoção de quantidade, caso não seja informada a quantidade, ou a quantidade a se remover seja maior que a que o produto já possui, então remover o mesmo do carrinho.
<br>**Pré-Condição:** Estar autenticado no sistema e existir um carrinho com produto na base de dados.
<br>**Passo-a-Passo:** Realizar um método DELETE na rota https://localhost:8082/dona-frost/v1/cart, informando no header da requisição o campo "Authorization" com o Token de autenticação do tipo Bearer, este que foi gerado no Teste#01, também o campo "idProductCart" com o número do id do Produto Carrinho que será deletado do carrinho.
<br>**Resultado Esperado:** Remover o produto do carrinho caso sejam atendidas as condições presentes na descrição do teste.
<br>**Status:** APROVADO
<br>**Report Do Bug:** Nenhum

Print do Teste #15 Parte 1
![Print do Teste #15_01](PrintsCasosDeTeste/CasoTeste15_01.png)

Print do Teste #15 Parte 2
![Print do Teste #15_02](PrintsCasosDeTeste/CasoTeste15_02.png)

---

### **ID Caso de Teste**: #16
>**Prioridade**: Baixa.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste listagem dos ProdutosCarrinho em um carrinho.
<br>**Descrição:** Realizar teste na rota listagem de ProdutosCarrinho.
<br>**Pré-Condição:** Estar autenticado no sistema, existir um carrinho na base de dados.
<br>**Passo-a-Passo:** Realizar um método GET na rota https://localhost:8082/dona-frost/v1/cart, informando no header da requisição o campo "Authorization" com o Token de autenticação do tipo Bearer, este que foi gerado no Teste#01, também o campo "idCart" com o número do id do carrinho que será listado.
<br>**Resultado Esperado:** Listar todos as entidades ProdutosCarrinho de um determinado carrinho da base de dados.
<br>**Status:** APROVADO
<br>**Report Do Bug:** Nennhum

Print do Teste #16
![Print do Teste #16](PrintsCasosDeTeste/CasoTeste16.png)


---

### **ID Caso de Teste**: #17
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste transformar um carrinho em pedido.
<br>**Descrição:** Realizar teste na rota de transformação de carrinho em pedido.
<br>**Pré-Condição:** Estar autenticado no sistema e existir um carrinho na base de dados.
<br>**Passo-a-Passo:** Realizar um método POST na rota https://localhost:8082/dona-frost/v1/order.
<br>**Resultado Esperado:** Transformar um carrinho em pedido e persistir este na base de dados.
<br>**Status:** APROVADO
<br>**Report Do Bug:** Nenhum

Print do Teste #17
![Print do Teste #17](PrintsCasosDeTeste/CasoTeste17.png)

---

### **ID Caso de Teste**: #18
>**Prioridade**: Baixa.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste listagem dos Pedidos de um usuário.
<br>**Descrição:** Realizar teste na rota listagem de Pedidos.
<br>**Pré-Condição:** Estar autenticado no sistema, existir pedidos na base de dados.
<br>**Passo-a-Passo:** Realizar um método GET na rota https://localhost:8082/dona-frost/v1/order, informando no header da requisição o campo "Authorization" com o Token de autenticação do tipo Bearer, este que foi gerado no Teste#01, também o campo "idUser" com o número do id do usuário que será listado os pedidos.
<br>**Resultado Esperado:** Listar todos os pedidos de um determinado usuário da base de dados, trazendo tal informação descriptografada.
<br>**Status:** APROVADO
<br>**Report Do Bug:** Nennhum

Print do Teste #18
![Print do Teste #18](PrintsCasosDeTeste/CasoTeste18.png)

---

### **ID Caso de Teste**: #19
>**Prioridade**: Baixa.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste listagem dos Pedidos de um usuário de acordo com o status do pedido.
<br>**Descrição:** Realizar teste na rota listagem de Pedidos informando um determinado status do pedido.
<br>**Pré-Condição:** Estar autenticado no sistema, existir pedidos no status escolhido na base de dados.
<br>**Passo-a-Passo:** Realizar um método GET na rota https://localhost:8082/dona-frost/v1/order, informando no header da requisição o campo "Authorization" com o Token de autenticação do tipo Bearer, este que foi gerado no Teste#01, também o campo "idUser" com o número do id do usuário que será listado os pedidos, e o campo "orderStatus" com uma das EnumPaymentType, que é o tipo de pagamento que será utilizado para filtrar a listagem do pedido.
<br>**Resultado Esperado:** Listar todos os pedidos do usuário no status escolhido, trazendo tal informação descriptografada.
<br>**Status:** APROVADO
<br>**Report Do Bug:** Nennhum

Print do Teste #19
![Print do Teste #19](PrintsCasosDeTeste/CasoTeste19.png)

