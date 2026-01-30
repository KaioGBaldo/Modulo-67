# 📚 Bookstore API - Django REST Framework & Pagination

Uma API profissional de gerenciamento de produtos (livros) desenvolvida com **Django** e **Django REST Framework**. O projeto foca na arquitetura modular, persistência de dados e na otimização da entrega de recursos através de paginação nativa.

---

# 📝 Resumo (Resume)
Neste projeto, estruturei uma API robusta onde cada componente segue o princípio da responsabilidade única. Utilizei **Models** para definir o esquema do banco de dados, **Serializers** para transformar dados complexos em JSON e **ViewSets** para centralizar a lógica de operações CRUD. O diferencial técnico desta implementação foi a configuração do `REST_FRAMEWORK` no `settings.py`, onde estabeleci uma estratégia de **Paginação Global**, garantindo que a API entregue dados de forma fracionada (5 itens por página), melhorando drasticamente a performance e a experiência do consumidor da API (Front-End).



## 🚀 Tecnologias e Ferramentas (Tech Stack)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/DRF-A30000?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

## 📋 Funcionalidades em Destaque
* **Paginação Automática:** Configuração global via `PageNumberPagination`, permitindo que o cliente navegue por grandes volumes de dados através de parâmetros de página.
* **Mapeamento de Modelos (ORM):** Uso de `DecimalField` para garantir precisão financeira nos preços e `TextField` para descrições detalhadas.
* **Serialização Model-Driven:** Implementação de `ModelSerializer` para automação do mapeamento de campos, reduzindo código repetitivo e erros de tipagem.
* **Roteamento Dinâmico:** Uso de `DefaultRouter` para registrar automaticamente os endpoints de produtos sob o prefixo `/api/`.
* **Configurações de Produção:** Separação clara de `BASE_DIR`, `SECRET_KEY` e gerenciamento de `INSTALLED_APPS` para escalabilidade do projeto.
* **Interface Administrativa:** Integração total com o Django Admin para gestão de estoque e monitoramento dos registros no banco SQLite3.



---

# 👨‍💻 Sobre mim (About Me)
Olá, meu nome é **Kaio**, tenho 22 anos. Como meu foco principal é o **Back-End com Python**, este projeto de Bookstore consolidou minha compreensão sobre como servir dados de forma eficiente. No Front-End com **React**, eu sofria para gerenciar listas gigantescas sem paginação; agora, no Back-End, aprendi a resolver esse problema na raiz. Minha transição está focada em criar APIs que não sejam apenas funcionais, mas que sigam as melhores práticas de tráfego de rede e performance de banco de dados.

### Entre em contato (Contact me)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=092E20)](https://linkedin.com/in/kaio-grativol-baldo-071a74150/)
[![Instagram](https://img.shields.io/badge/Instagram-000?style=for-the-badge&logo=instagram&logoColor=092E20)](https://www.instagram.com/kaiull__/)
[![GitHub](https://img.shields.io/badge/Github-000?style=for-the-badge&logo=github&logoColor=092E20)](https://github.com/SeuUsuarioAqui)

---
*Projeto desenvolvido para consolidar o desenvolvimento de APIs escaláveis com paginação e DRF.*
