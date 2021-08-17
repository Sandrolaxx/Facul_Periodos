# Casos de Teste ✨

Testes - MicroServiço Produto
<br>

### **ID Caso de Teste**: #1
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste cadastro de produto.
<br>**Descrição:** Realizar teste na rota de cadastro de produto.
<br>**Pré-Condição:** Estar autenticado no sistema.
<br>**Passo-a-Passo:** Realizar um método POST na rota https://localhost:8080/dona-frost/v1/product, informando no header da requisição o campo Authorization com o Token de autenticação do tipo Bearer, o campo Content-Type : application/json, um json com um body similar ao exemplo abaixo.
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
>**Resultado Esperado:** Cadastrar produto na base de dados
<br>**Status:** APROVADO/BUG
<br>**Report Do Bug:** Nenhum

---

### **ID Caso de Teste**: #2
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste atualização/update de produto.
<br>**Descrição:** Realizar teste na rota de update mudando todos os campos de um produto existente, com base em seu id.
<br>**Pré-Condição:** Estar autenticado no sistema, existir um produto na base de dados.
<br>**Passo-a-Passo:** Realizar um método PUT na rota https://localhost:8080/dona-frost/v1/product.
<br>**Resultado Esperado:** Atualização dos campos de um produto existente na base de dados.
<br>**Status:** APROVADO/BUG
<br>**Report Do Bug:** Nennhum

---

### **ID Caso de Teste**: #3
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste deleção de produto.
<br>**Descrição:** Realizar teste na rota de delete em um produto existente, com base em seu id.
<br>**Pré-Condição:** Estar autenticado no sistema, existir um produto na base de dados.
<br>**Passo-a-Passo:** Realizar um método DELETE na rota https://localhost:8080/dona-frost/v1/product.
<br>**Resultado Esperado:** Remover o produto informado.
<br>**Status:** APROVADO/BUG
<br>**Report Do Bug:** Nennhum

---

### **ID Caso de Teste**: #4
>**Prioridade**: Baixa.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste listagem de todos os produtos.
<br>**Descrição:** Realizar teste na rota listagem de produtos.
<br>**Pré-Condição:** Estar autenticado no sistema, existir mais de um produto na base de dados.
<br>**Passo-a-Passo:** Realizar um método GET na rota https://localhost:808/dona-frost/v1/product.
<br>**Resultado Esperado:** Listar todos os produtos da base de dados.
<br>**Status:** APROVADO/BUG
<br>**Report Do Bug:** Nennhum

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
<br>**Passo-a-Passo:** Realizar um método POST na rota https://localhost:8081/dona-frost/v1/user.
<br>**Resultado Esperado:** Cadastrar usuário na base de dados
<br>**Status:** APROVADO/BUG
<br>**Report Do Bug:** Nenhum

---

### **ID Caso de Teste**: #6
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste atualização/update de usuário.
<br>**Descrição:** Realizar teste na rota de update mudando todos os campos de um usuário existente, com base em seu id.
<br>**Pré-Condição:** Estar autenticado no sistema, existir um usuário na base de dados.
<br>**Passo-a-Passo:** Realizar um método PUT na rota https://localhost:8081/dona-frost/v1/user.
<br>**Resultado Esperado:** Atualização dos campos de um usuário existente na base de dados.
<br>**Status:** APROVADO/BUG
<br>**Report Do Bug:** Nennhum

---

### **ID Caso de Teste**: #7
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste deleção de usuário.
<br>**Descrição:** Realizar teste na rota de delete em um usuário existente, com base em seu id.
<br>**Pré-Condição:** Estar autenticado no sistema, existir um usuário na base de dados.
<br>**Passo-a-Passo:** Realizar um método DELETE na rota https://localhost:8081/dona-frost/v1/user.
<br>**Resultado Esperado:** Remover o usuário informado.
<br>**Status:** APROVADO/BUG
<br>**Report Do Bug:** Nennhum

---

### **ID Caso de Teste**: #8
>**Prioridade**: Baixa.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste listagem de todos os usuários.
<br>**Descrição:** Realizar teste na rota listagem de usuários.
<br>**Pré-Condição:** Estar autenticado no sistema, existir mais de um usuário na base de dados.
<br>**Passo-a-Passo:** Realizar um método GET na rota https://localhost:8081/dona-frost/v1/user.
<br>**Resultado Esperado:** Listar todos os usuários da base de dados.
<br>**Status:** APROVADO/BUG
<br>**Report Do Bug:** Nennhum

---

### **ID Caso de Teste**: #9
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste cadastro de um novo endereço para um usuário existente.
<br>**Descrição:** Realizar teste na rota de cadastro de um novo endereço para um usuário existente.
<br>**Pré-Condição:** Estar autenticado no sistema, existir um usuário.
<br>**Passo-a-Passo:** Realizar um método POST na rota https://localhost:8081/dona-frost/v1/user/address.
<br>**Resultado Esperado:** Cadastrar o novo endereço na base de dados.
<br>**Status:** APROVADO/BUG
<br>**Report Do Bug:** Nenhum

---

### **ID Caso de Teste**: #10
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste atualização de um endereço existente.
<br>**Descrição:** Realizar teste na rota de update/atualização de um endereço de um usuário existente.
<br>**Pré-Condição:** Estar autenticado no sistema, existir um endereço na base de dados.
<br>**Passo-a-Passo:** Realizar um método PUT na rota https://localhost:8081/dona-frost/v1/user/address.
<br>**Resultado Esperado:** Atualizar os campos do endereço informado na base de dados.
<br>**Status:** APROVADO/BUG
<br>**Report Do Bug:** Nenhum

---

### **ID Caso de Teste**: #11
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste remoção/deleção de um endereço existente.
<br>**Descrição:** Realizar teste na rota de remoção/deleção em um endereço de um usuário existente.
<br>**Pré-Condição:** Estar autenticado no sistema, existir um endereço na base de dados.
<br>**Passo-a-Passo:** Realizar um método DELETE na rota https://localhost:8081/dona-frost/v1/user/address.
<br>**Resultado Esperado:** Deletar/Remover endereço informado da base de dados.
<br>**Status:** APROVADO/BUG
<br>**Report Do Bug:** Nenhum

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
<br>**Pré-Condição:** Estar autenticado no sistema e existir um carrinho na base de dados.
<br>**Passo-a-Passo:** Realizar um método POST na rota https://localhost:8082/dona-frost/v1/cart.
<br>**Resultado Esperado:** Persistir um produto em um carrinho existente na base de dados.
<br>**Status:** APROVADO/BUG
<br>**Report Do Bug:** Nenhum

---

### **ID Caso de Teste**: #13
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste adicionar quantidade a um produto no carrinho do usuário.
<br>**Descrição:** Realizar teste na rota adição de quantidade a um produto no carrinho.
<br>**Pré-Condição:** Estar autenticado no sistema e existir um carrinho com produto na base de dados.
<br>**Passo-a-Passo:** Realizar um método PUT na rota https://localhost:8082/dona-frost/v1/cart.
<br>**Resultado Esperado:** Adicionar a quantidade informada a um produto em um carrinho existente na base de dados.
<br>**Status:** APROVADO/BUG
<br>**Report Do Bug:** Nenhum

---

### **ID Caso de Teste**: #14
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste remover quantidade de um produto no carrinho do usuário.
<br>**Descrição:** Realizar teste na rota remoção de quantidade a um produto no carrinho.
<br>**Pré-Condição:** Estar autenticado no sistema e existir um carrinho com produto na base de dados.
<br>**Passo-a-Passo:** Realizar um método DELETE na rota https://localhost:8082/dona-frost/v1/cart.
<br>**Resultado Esperado:** Remover a quantidade informada de um produto em um carrinho existente na base de dados.
<br>**Status:** APROVADO/BUG
<br>**Report Do Bug:** Nenhum

---

### **ID Caso de Teste**: #15
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste remover um produto carrinho do usuário.
<br>**Descrição:** Realizar teste na rota remoção de quantidade, caso não seja informada a quantidade, ou a quantidade a se remover seja maior que a que o produto já possui, então remover o mesmo do carrinho.
<br>**Pré-Condição:** Estar autenticado no sistema e existir um carrinho com produto na base de dados.
<br>**Passo-a-Passo:** Realizar um método DELETE na rota https://localhost:8082/dona-frost/v1/cart.
<br>**Resultado Esperado:** Remover o produto do carrinho caso sejam atendidas as condições presentes na descrição do teste.
<br>**Status:** APROVADO/BUG
<br>**Report Do Bug:** Nenhum

---

### **ID Caso de Teste**: #16
>**Prioridade**: Baixa.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste listagem dos ProdutosCarrinho em um carrinho.
<br>**Descrição:** Realizar teste na rota listagem de ProdutosCarrinho.
<br>**Pré-Condição:** Estar autenticado no sistema, existir um carrinho na base de dados.
<br>**Passo-a-Passo:** Realizar um método GET na rota https://localhost:8082/dona-frost/v1/cart.
<br>**Resultado Esperado:** Listar todos as entidades ProdutosCarrinho de um determinado carrinho da base de dados.
<br>**Status:** APROVADO/BUG
<br>**Report Do Bug:** Nennhum

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
<br>**Status:** APROVADO/BUG
<br>**Report Do Bug:** Nenhum

---

### **ID Caso de Teste**: #18
>**Prioridade**: Baixa.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste listagem dos Pedidos de um usuário.
<br>**Descrição:** Realizar teste na rota listagem de Pedidos.
<br>**Pré-Condição:** Estar autenticado no sistema, existir pedidos na base de dados.
<br>**Passo-a-Passo:** Realizar um método GET na rota https://localhost:8082/dona-frost/v1/order.
<br>**Resultado Esperado:** Listar todos os pedidos de um determinado usuário da base de dados, trazendo tal informação descriptografada.
<br>**Status:** APROVADO/BUG
<br>**Report Do Bug:** Nennhum

---

### **ID Caso de Teste**: #19
>**Prioridade**: Baixa.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste listagem dos Pedidos de um usuário de acordo com o status do pedido.
<br>**Descrição:** Realizar teste na rota listagem de Pedidos informando um determinado status do pedido.
<br>**Pré-Condição:** Estar autenticado no sistema, existir pedidos no status escolhido na base de dados.
<br>**Passo-a-Passo:** Realizar um método GET na rota https://localhost:8082/dona-frost/v1/order.
<br>**Resultado Esperado:** Listar todos os pedidos do usuário no status escolhido, trazendo tal informação descriptografada.
<br>**Status:** APROVADO/BUG
<br>**Report Do Bug:** Nennhum
