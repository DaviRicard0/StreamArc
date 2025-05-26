<h1>🧱 Projeto Streamlit com Arquitetura Limpa</h1>

<p>Este projeto tem como objetivo demonstrar uma implementação de <strong>Arquitetura Limpa (Clean Architecture)</strong> em uma aplicação Python que utiliza o <strong>Streamlit</strong> como interface de usuário, <strong>SQLAlchemy</strong> com <strong>SQLite</strong> para persistência de dados, <strong>Dependency Injector</strong> para gerenciamento de dependências e <strong>Matplotlib</strong> para visualização de dados.</p>

<h2>🛠️ Tecnologias Utilizadas</h2>
<ul>
  <li><a href="https://streamlit.io/">Streamlit</a> – Interface web interativa e rápida para aplicações Python.</li>
  <li><a href="https://www.sqlalchemy.org/">SQLAlchemy</a> – ORM para interação com banco de dados.</li>
  <li><a href="https://www.sqlite.org/">SQLite</a> – Banco de dados leve e embutido.</li>
  <li><a href="https://python-dependency-injector.ets-labs.org/">Dependency Injector</a> – Contêiner para injeção de dependência e inversão de controle.</li>
  <li><a href="https://matplotlib.org/">Matplotlib</a> – Biblioteca para geração de gráficos e visualizações.</li>
</ul>

<h2>🧩 Sobre a Arquitetura</h2>
<p>Este projeto segue os princípios da <strong>Arquitetura Limpa</strong>, que busca separar responsabilidades em camadas bem definidas. Os principais módulos são:</p>
<ul>
  <li><strong>Domain</strong>: entidades e regras de negócio.</li>
  <li><strong>Application</strong>: casos de uso (orquestração de lógica).</li>
  <li><strong>Infrastructure</strong>: persistência de dados (repositórios), serviços externos, etc.</li>
  <li><strong>Web</strong>: camada de apresentação (Streamlit).</li>
  <li><strong>Container</strong>: configuração das dependências com <code>Dependency Injector</code>.</li>
</ul>

<p>Essa organização facilita testes, manutenção, escalabilidade e separação de responsabilidades.</p>

<h2>🎯 Objetivos</h2>
<ul>
  <li>Demonstrar como aplicar arquitetura limpa em um projeto com Streamlit.</li>
  <li>Promover boas práticas de organização de código em projetos Python.</li>
  <li>Facilitar testes unitários e integração com injeção de dependência.</li>
  <li>Exibir dados e interações de forma clara com visualizações usando Matplotlib.</li>
</ul>

<h2>🚀 Como Executar</h2>
<pre><code>pip install -r requirements.txt
streamlit run app.py
</code></pre>

<h2>📂 Estrutura de Diretórios (Exemplo)</h2>
<pre><code>├── src/
│   ├── domain/
│   ├── application/
│   ├── infrastructure/
│   ├── web/
│   ├── app.py
│   └── container.py
├── requirements.txt
└── README.md
</code></pre>

<h2>✅ Status</h2>
<p>🔧 Em desenvolvimento – sugestões e melhorias são bem-vindas!</p>