# Casos de Teste - Back-End Aplicativo Aktie ✨

### **ID Caso de Teste**: #1
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste cadastro de usuário.
<br>**Descrição:** Realizar teste na rota de cadastro de usuário.
<br>**Resultado Esperado:** Cadastrar usuário na base de dados.
<br>**Status:** APROVADO/REPROVADO
<br>**Report Do Bug:** Nenhum

---

### **ID Caso de Teste**: #2
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste atualização/update de usuário.
<br>**Descrição:** Realizar teste na rota de update mudando os campos de um usuário existente, com base em seu id.
<br>**Pré-Condição:** Estar autenticado no sistema, existir um usuário na base de dados.
<br>**Status:** APROVADO/REPROVADO
<br>**Report Do Bug:** Nennhum

---

### **ID Caso de Teste**: #3
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste Geração Token de Autenticação.
<br>**Descrição:** Realizar Teste na Rota de Geração do Token de Autenticação.
<br>**Pré-Condição:** Possuir credenciais do sistema para gerar o token de autenticação.
<br>**Resultado Esperado:** Gerar o Token de Autenticação para poder realizar chamadas nas outras rotas.
<br>**Status:** APROVADO/REPROVADO
<br>**Report Do Bug:** Nennhum

---

### **ID Caso de Teste**: #4
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste cadastro de evento.
<br>**Descrição:** Realizar teste na rota de cadastro de evento.
<br>**Pré-Condição:** Estar autenticado no sistema.
<br>**Resultado Esperado:** Cadastrar um novo evento na base de dados.
<br>**Status:** APROVADO/REPROVADO
<br>**Report Do Bug:** Nenhum

---

### **ID Caso de Teste**: #5
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste atualização/update de evento.
<br>**Descrição:** Realizar teste na rota de update mudando os campos de um evento existente, com base em seu id.
<br>**Pré-Condição:** Estar autenticado no sistema, existir um evento na base de dados.
<br>**Resultado Esperado:** Atualização dos campos de um evento existente na base de dados.
<br>**Status:** APROVADO/REPROVADO
<br>**Report Do Bug:** Nennhum

---

### **ID Caso de Teste**: #6
>**Prioridade**: Média.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste deleção de evento.
<br>**Descrição:** Realizar teste na rota de delete em um evento existente, com base em seu id.
<br>**Pré-Condição:** Estar autenticado no sistema, existir um evento na base de dados.
<br>**Resultado Esperado:** Remover o evento informado.
<br>**Status:** APROVADO/REPROVADO
<br>**Report Do Bug:** Nennhum

---

### **ID Caso de Teste**: #7
>**Prioridade**: Baixa.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste listagem das disciplinas.
<br>**Descrição:** Realizar teste na rota listagem das disciplinas.
<br>**Pré-Condição:** Estar autenticado no sistema, existir mais de uma disciplina na base de dados.
<br>**Resultado Esperado:** Listar todos as disciplinas da base de dados.
<br>**Status:** APROVADO/REPROVADO
<br>**Report Do Bug:** Nennhum

---

### **ID Caso de Teste**: #8
>**Prioridade**: Baixa.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste listagem dos eventos por filtro.
<br>**Descrição:** Realizar teste na rota listagem dos eventos por filtro, como apresentações/workshops ou grupos de estudo.
<br>**Pré-Condição:** Estar autenticado no sistema, existir mais de um eventos na base de dados.
<br>**Resultado Esperado:** Listar todos os eventos da base de dados por filtro de evento.
<br>**Status:** APROVADO/REPROVADO
<br>**Report Do Bug:** Nennhum

---

### **ID Caso de Teste**: #9
>**Prioridade**: Baixa.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste buscar informações do evento por id.
<br>**Descrição:** Realizar teste na rota de busca de informações do evento por id, como local, horário, interessados e etc.
<br>**Pré-Condição:** Estar autenticado no sistema, existir um evento na base de dados.
<br>**Resultado Esperado:** Retornar as informações do evento.
<br>**Status:** APROVADO/REPROVADO
<br>**Report Do Bug:** Nennhum

---

### **ID Caso de Teste**: #10
>**Prioridade**: Baixa.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste participar de um evento.
<br>**Descrição:** Realizar teste na rota de participação de evento.
<br>**Pré-Condição:** Estar autenticado no sistema, existir um evento na base de dados.
<br>**Resultado Esperado:** Adicionar a participação do usuário no evento pretendido.
<br>**Status:** APROVADO/REPROVADO
<br>**Report Do Bug:** Nennhum

---

### **ID Caso de Teste**: #11
>**Prioridade**: Baixa.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste atribuir 5 disciplinas a um usuário.
<br>**Descrição:** Realizar teste na rota de atribuição de disciplinas a um usuário.
<br>**Pré-Condição:** Estar autenticado no sistema, existir disciplinas na base de dados.
<br>**Resultado Esperado:** Informar 5 disciplinas e atribuir a um usuário.
<br>**Status:** APROVADO/REPROVADO
<br>**Report Do Bug:** Nennhum

---

### **ID Caso de Teste**: #12
>**Prioridade**: Baixa.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste listagem datas dos eventos.
<br>**Descrição:** Realizar teste na rota listagem das datas dos eventos.
<br>**Pré-Condição:** Estar autenticado no sistema, existir mais de um eventos na base de dados.
<br>**Resultado Esperado:** Listar todas as datas de eventos em um período de tempo.
<br>**Status:** APROVADO/REPROVADO
<br>**Report Do Bug:** Nennhum

---

### **ID Caso de Teste**: #13
>**Prioridade**: Baixa.
<br>**Testado Por**: Sandro Ramos.
<br>**Data do Teste:** DD/MM/YYYY
<br>**Nome do Caso de Teste:** Teste listagem dos eventos por dia.
<br>**Descrição:** Realizar teste na rota listagem dos eventos informando um dia em específico.
<br>**Pré-Condição:** Estar autenticado no sistema, existir mais de um eventos na base de dados.
<br>**Resultado Esperado:** Listar todos os eventos para o dia informado.
<br>**Status:** APROVADO/REPROVADO
<br>**Report Do Bug:** Nennhum