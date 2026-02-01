# 🌐 Plano de Aula Interativo: Desvendando o Modelo OSI com IA
> **Desafio de Projeto:** Criando um Ecossistema de IA para Educação (DIO)

Este repositório contém o plano de aula e a documentação do processo de criação de uma experiência de aprendizado personalizada para a disciplina de **Redes de Computadores**, utilizando ferramentas de Inteligência Artificial.

---

## 🎯 Objetivo do Projeto
O objetivo é transformar a teoria densa do **Modelo OSI** em uma experiência prática e visual, utilizando IAs generativas para criar analogias, scripts de simulação e tutores personalizados.

## 🛠️ Ecossistema de IA Utilizado
* **ChatGPT/Gemini:** Para estruturação do plano de aula e criação de analogias complexas.
* **Claude.ai:** Para geração de scripts de simulação de tráfego (Python/Scapy).
* **Gamma.app / Canva Magic Design:** Para criação visual dos slides da aula.
* **DALL-E 3 / Midjourney:** Para gerar representações visuais das "camadas" da rede.

---

## 📝 O Plano de Aula

### 1. Tema: A Jornada do Pacote (Modelo OSI)
* **Público-alvo:** Alunos de Graduação em TI / Técnico em Redes.
* **Duração:** 2 horas.

### 2. Metodologia Ativa com IA
Em vez de apenas slides, os alunos utilizarão um **Tutor de IA Personalizado** (via prompt) para resolver um problema de rede.

#### O Prompt de Ouro (System Prompt para o Aluno):
> *"Atue como um Engenheiro de Redes Sênior. Seu objetivo é explicar para o aluno como o protocolo HTTP se transforma em bits, camada por camada. Use a analogia de uma transportadora logística e peça para o aluno identificar qual 'etiqueta' (header) é adicionada em cada etapa."*

### 3. Atividade Prática: "Onde o Pacote Parou?"
Os alunos devem usar a IA para gerar um script simples em Python que simula o encapsulamento e, em seguida, analisar o resultado no Wireshark.

---

## 🚀 Processo de Desenvolvimento

1.  **Brainstorming de Analogias:** Usei o Gemini para comparar o Modelo OSI com o processo de envio de uma pizza via app (do pedido à entrega física).
2.  **Refinamento Técnico:** O Claude ajudou a validar se os conceitos de *Data Link* (Frames) e *Network* (Packets) estavam tecnicamente precisos no material didático.
3.  **Documentação:** Estruturação deste README para servir como guia para outros professores.

## 📊 Resultados Esperados
* Aumento do engajamento através de exemplos personalizados.
* Redução da curva de aprendizado em conceitos abstratos.
* Capacidade do aluno de "conversar" com a tecnologia enquanto estuda.

---

## 📁 Estrutura do Repositório
* `/prompts`: Lista de comandos usados para gerar o conteúdo.
* `/scripts`: Exemplo de código Python para simulação de pacotes.
* `/images`: Diagramas gerados por IA.

---

**Professor:** Bruno Camargo Ribeiro  
**Disciplina:** Redes de Computadores  
**Instituição:** Etec Sales Gomes
