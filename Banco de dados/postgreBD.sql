create database postgresBD

create table aluno(
ID_aluno serial primary key,
nome_aluno varchar(100) not null,
idade_aluno integer not null,
email_aluno varchar (100) unique not null,
endereco_aluno varchar(150),
telefone_aluno varchar(20) unique
);

create table curso (
ID_curso serial primary key,
nome_curso varchar (30) not null,
descricao varchar (300) not null,
valor_curso float not null,
carga_horaria integer not null,
numero_vagas integer not null
);

create table professor(
ID_professor serial primary key,
nome_professor varchar(100) not null,
idade_professor integer not null,
email_professor varchar(100) unique not null,
telefone_professor varchar(20) unique,
formacao varchar (50)
);

create table usuario(
ID_usuario serial primary key,
nome_usuario varchar(100),
email_usuario varchar(100) not null unique,
senha_hash text not null,
role VARCHAR(20) NOT NULL DEFAULT 'usuario'
);

--usuários pré programados: 
--AdminCESAL@CESAL.edu.br senha: admCESAL123
--juninho@CESAL.edu.br senha: juninhoexadm1234
--

create table matricula(
ID_matricula serial primary key,
ID_aluno integer not null references aluno (ID_aluno) on delete cascade,
ID_curso integer not null references curso (ID_curso) on delete cascade,
data_matricula date not null default current_date,
unique (ID_aluno, ID_curso)
);

CREATE TABLE disciplina (
    ID_disciplina SERIAL PRIMARY KEY,
    nome_disciplina VARCHAR(100) NOT NULL,
    descricao_disciplina VARCHAR(300) NOT NULL
);

CREATE TABLE curso_disciplina (
    ID_curso INTEGER NOT NULL REFERENCES curso(ID_curso),
    ID_disciplina INTEGER NOT NULL REFERENCES disciplina(ID_disciplina),
    PRIMARY KEY (ID_curso, ID_disciplina)
);

CREATE TABLE professor_disciplina (
    ID_professor INTEGER NOT NULL REFERENCES professor(ID_professor),
    ID_disciplina INTEGER NOT NULL REFERENCES disciplina(ID_disciplina),
    PRIMARY KEY (ID_professor, ID_disciplina)
);

INSERT INTO curso (nome_curso, descricao, valor_curso, carga_horaria, numero_vagas)
VALUES
('Administração', 'Curso de gestão empresarial', 1200.00, 60, 30),
('Análise de Sistemas', 'Curso sobre desenvolvimento de software', 1500.00, 80, 25),
('Ciência da Computação', 'Foco em algoritmos e estruturas de dados', 2000.00, 100, 30),
('Engenharia Civil', 'Projetos e execução de obras civis', 2500.00, 120, 20),
('Arquitetura', 'Design e planejamento de edificações', 2400.00, 100, 20),
('Marketing Digital', 'Técnicas e estratégias de marketing online', 1100.00, 40, 30),
('Enfermagem', 'Cuidado com a saúde e bem-estar', 1300.00, 60, 25),
('Biomedicina', 'Estudo de processos biológicos', 1400.00, 80, 20),
('Direito', 'Legislação e prática jurídica', 2200.00, 120, 40),
('Psicologia', 'Estudo do comportamento humano', 1800.00, 100, 30),
('Educação Física', 'Ensino e promoção da saúde física', 1000.00, 60, 35),
('Nutrição', 'Estudos sobre alimentação saudável', 1200.00, 50, 25),
('Odontologia', 'Saúde bucal e procedimentos odontológicos', 3000.00, 150, 15),
('Medicina', 'Formação em ciências médicas', 4000.00, 200, 10),
('Veterinária', 'Cuidado com a saúde animal', 2200.00, 120, 15),
('Fisioterapia', 'Reabilitação física e motora', 1600.00, 80, 20),
('Engenharia Elétrica', 'Projetos de sistemas elétricos', 2500.00, 120, 20),
('Engenharia Mecânica', 'Projetos de sistemas mecânicos', 2400.00, 120, 20),
('Engenharia de Produção', 'Gestão e otimização de processos', 2300.00, 100, 25),
('Ciências Contábeis', 'Gestão financeira e contabilidade', 1100.00, 60, 30),
('Administração Pública', 'Gestão em instituições públicas', 1000.00, 60, 35),
('Logística', 'Gestão de transporte e armazenagem', 900.00, 50, 40),
('Design Gráfico', 'Criação visual e comunicação', 950.00, 40, 30),
('Fotografia', 'Técnicas de captura e edição de imagens', 800.00, 30, 20),
('Moda', 'Design e criação de roupas e acessórios', 1200.00, 50, 25),
('Gastronomia', 'Técnicas culinárias e gestão de cozinha', 1400.00, 60, 15),
('Turismo', 'Gestão de atividades turísticas', 1000.00, 40, 30),
('Hotelaria', 'Gestão de hotéis e eventos', 1100.00, 40, 25),
('Relações Internacionais', 'Estudos sobre política global', 1500.00, 80, 20),
('Serviço Social', 'Atuação em políticas públicas', 900.00, 50, 30),
('História', 'Estudo de eventos históricos', 800.00, 40, 25),
('Geografia', 'Estudo do espaço e meio ambiente', 800.00, 40, 25),
('Filosofia', 'Estudo do pensamento humano', 700.00, 30, 20),
('Sociologia', 'Estudo das relações sociais', 700.00, 30, 20),
('Letras', 'Estudos linguísticos e literários', 900.00, 40, 25),
('Pedagogia', 'Formação de educadores', 1000.00, 50, 30),
('Matemática', 'Estudos matemáticos aplicados', 900.00, 40, 20),
('Física', 'Estudos sobre fenômenos naturais', 950.00, 50, 20),
('Química', 'Estudos das transformações da matéria', 950.00, 50, 20),
('Biologia', 'Estudos sobre seres vivos', 950.00, 50, 20),
('Computação Gráfica', 'Modelagem e animação digital', 1100.00, 40, 15),
('Desenvolvimento de Jogos', 'Criação e programação de games', 1300.00, 60, 20),
('Robótica', 'Desenvolvimento de sistemas automatizados', 1400.00, 60, 20),
('Segurança da Informação', 'Proteção de dados e sistemas', 1500.00, 60, 25),
('Banco de Dados', 'Gerenciamento e modelagem de dados', 1200.00, 50, 20),
('Inteligência Artificial', 'Desenvolvimento de sistemas inteligentes', 1600.00, 70, 15),
('Machine Learning', 'Algoritmos de aprendizado de máquina', 1700.00, 80, 10);

INSERT INTO disciplina (nome_disciplina, descricao_disciplina) VALUES
('Algoritmos', 'Estudo de estruturas lógicas para resolução de problemas'),
('Banco de Dados', 'Modelagem e gerenciamento de dados'),
('Redes de Computadores', 'Comunicação entre sistemas'),
('Sistemas Operacionais', 'Gerenciamento de recursos computacionais'),
('Programação Orientada a Objetos', 'Paradigma essencial de desenvolvimento'),
('Engenharia de Software', 'Processos para desenvolvimento de sistemas'),
('Estruturas de Dados', 'Organização de informações para eficiência'),
('Computação Gráfica', 'Criação de imagens digitais'),
('Inteligência Artificial', 'Simulação de inteligência humana'),
('Machine Learning', 'Aprendizado automático de padrões'),
('Big Data', 'Processamento de grandes volumes de dados'),
('Cloud Computing', 'Tecnologias para computação em nuvem'),
('Segurança da Informação', 'Proteção de sistemas e dados'),
('Desenvolvimento Web', 'Criação de aplicações para internet'),
('Mobile Development', 'Criação de aplicativos para dispositivos móveis'),
('Gestão de Projetos', 'Planejamento e execução de projetos'),
('Matemática Discreta', 'Matemática aplicada à computação'),
('Física Geral', 'Fundamentos físicos aplicados'),
('Cálculo Diferencial', 'Estudos de taxas de variação'),
('Estatística', 'Análise de dados e probabilidades'),
('Direito Constitucional', 'Normas fundamentais do estado'),
('Direito Penal', 'Regras e punições criminais'),
('Psicologia Social', 'Estudo das interações humanas'),
('Anatomia Humana', 'Estrutura do corpo humano'),
('Fisiologia', 'Funcionamento dos sistemas do corpo'),
('Microbiologia', 'Estudo de micro-organismos'),
('Patologia', 'Estudo das doenças'),
('Enfermagem Clínica', 'Cuidados em ambiente hospitalar'),
('Farmacologia', 'Estudo de medicamentos'),
('Gestão Hospitalar', 'Administração de unidades de saúde'),
('Contabilidade', 'Registro e análise financeira'),
('Finanças Corporativas', 'Gestão de recursos empresariais'),
('Marketing Digital', 'Promoção de marcas online'),
('Comportamento do Consumidor', 'Estudos sobre hábitos de compra'),
('Logística Empresarial', 'Gestão de fluxo de mercadorias'),
('Cadeia de Suprimentos', 'Organização de processos produtivos'),
('História Geral', 'Estudo de eventos históricos'),
('Geografia Física', 'Análise de aspectos naturais'),
('Filosofia Contemporânea', 'Reflexão sobre o pensamento atual'),
('Sociologia das Organizações', 'Estudo das relações institucionais'),
('Educação Infantil', 'Formação de crianças na fase inicial'),
('Metodologia do Ensino', 'Técnicas pedagógicas'),
('Literatura Brasileira', 'Análise de obras nacionais'),
('Gramática Normativa', 'Regras da língua portuguesa'),
('Lógica de Programação', 'Fundamentos da codificação'),
('Empreendedorismo', 'Criação e gestão de negócios'),
('E-commerce', 'Comércio eletrônico e suas práticas'),
('Design de Interface', 'Criação de experiências digitais'),
('UX/UI Design', 'Experiência e interação com o usuário'),
('Fotografia Digital', 'Técnicas de captura de imagens'),
('Edição de Imagem', 'Manipulação e ajuste de fotos'),
('Cozinha Internacional', 'Técnicas culinárias de diversos países'),
('Panificação', 'Produção de pães e derivados'),
('Gestão de Restaurantes', 'Administração de estabelecimentos alimentícios'),
('Turismo Cultural', 'Promoção de experiências locais'),
('Hotelaria', 'Gerenciamento de serviços de hospedagem'),
('Eventos e Cerimoniais', 'Planejamento de eventos'),
('Relações Internacionais', 'Estudos sobre política global'),
('Política Externa', 'Atuação diplomática de países'),
('Serviço Social', 'Atuação em políticas públicas'),
('Psicologia Organizacional', 'Comportamento humano nas empresas'),
('História da Arte', 'Evolução das expressões artísticas'),
('Estética', 'Análise do belo e do gosto artístico'),
('Moda e Estilo', 'Criação de tendências e coleções'),
('Desenho Técnico', 'Representação gráfica de projetos'),
('Cálculo Estrutural', 'Dimensionamento de construções'),
('Materiais de Construção', 'Estudo dos componentes de obras'),
('Geotecnia', 'Análise do solo para engenharia'),
('Hidráulica', 'Fluxos de líquidos em sistemas'),
('Eletrônica Analógica', 'Circuitos eletrônicos clássicos'),
('Eletrônica Digital', 'Sistemas lógicos e computacionais'),
('Automação Industrial', 'Processos automáticos na indústria'),
('Robótica', 'Sistemas automatizados e inteligentes'),
('Programação de Jogos', 'Desenvolvimento de games'),
('Inteligência Emocional', 'Gestão das emoções'),
('Técnicas de Negociação', 'Mediação de interesses'),
('Gestão de Pessoas', 'Administração de recursos humanos'),
('Ética Profissional', 'Conduta adequada no trabalho'),
('Legislação Trabalhista', 'Normas sobre relações de emprego'),
('Produção Audiovisual', 'Criação de vídeos e filmes'),
('Roteirização', 'Criação de scripts para mídia'),
('Edição de Vídeo', 'Pós-produção audiovisual'),
('Análise de Dados', 'Processamento e interpretação de dados'),
('Visualização de Dados', 'Representação gráfica de informações'),
('Deep Learning', 'Redes neurais profundas'),
('Processamento de Imagens', 'Análise automatizada de imagens'),
('Processamento de Linguagem Natural', 'Interação entre humanos e máquinas via linguagem'),
('Bioinformática', 'Análise computacional de dados biológicos'),
('Genética', 'Estudo dos genes e hereditariedade'),
('Ecologia', 'Relações dos seres vivos com o meio'),
('Geoprocessamento', 'Análise espacial via sistemas computacionais'),
('Meteorologia', 'Estudo das condições climáticas'),
('Astronomia', 'Exploração do universo'),
('Criptografia', 'Proteção de informações via codificação'),
('Blockchain', 'Tecnologia de registros descentralizados'),
('Desenvolvimento Ágil', 'Metodologias como Scrum e Kanban'),
('Testes de Software', 'Validação de sistemas computacionais');

INSERT INTO curso_disciplina (ID_curso, ID_disciplina) VALUES
(1, 1), (1, 2),
(2, 1), (2, 3),
(3, 1), (3, 4),
(4, 5), (4, 6),
(5, 7), (5, 8),
(6, 9), (6, 10),
(7, 24), (7, 25),
(8, 26), (8, 27),
(9, 21), (9, 22),
(10, 23), (10, 24),
(11, 40), (11, 41),
(12, 42), (12, 43),
(13, 24), (13, 28),
(14, 24), (14, 25),
(15, 26), (15, 27),
(16, 31), (16, 32),
(17, 33), (17, 34),
(18, 35), (18, 36),
(19, 30), (19, 31),
(20, 30), (20, 32),
(21, 33), (21, 34),
(22, 45), (22, 46),
(23, 47), (23, 48),
(24, 49), (24, 50),
(25, 51), (25, 52),
(26, 53), (26, 54),
(27, 55), (27, 56),
(28, 57), (28, 58),
(29, 59), (29, 60),
(30, 61), (30, 62),
(31, 63), (31, 64),
(32, 65), (32, 66),
(33, 67), (33, 68),
(34, 69), (34, 70),
(35, 71), (35, 72),
(36, 73), (36, 74),
(37, 75), (37, 76),
(38, 77), (38, 78),
(39, 79), (39, 80),
(40, 81), (40, 82),
(41, 83), (41, 84),
(42, 85), (42, 86),
(43, 87), (43, 88),
(44, 89), (44, 90),
(45, 91), (45, 92),
(46, 93), (46, 94),
(47, 95), (47, 96);

INSERT INTO professor (nome_professor, idade_professor, email_professor, telefone_professor, formacao)
values
('Wagner', 33, 'wagner@cesal.edu.br', '5582997685315', 'programação'),
('Geraldo', 43, 'geraldo@cesal.edu.br', '558298989898',  'programação'),
('Carlos Silva', 45, 'carlos.silva@cesal.edu.br', '5582912345678', 'Doutor em Física'),
('Ana Souza', 38, 'ana.souza@cesal.edu.br', '5582923456789', 'Mestre em Matemática'),
('Ricardo Almeida', 50, 'ricardo.almeida@cesal.edu.br', '5582934567890', 'Mestre em Química'),
('Patrícia Oliveira', 42, 'patricia.oliveira@cesal.edu.br', '5582945678901', 'Doutora em Biologia'),
('Felipe Santos', 35, 'felipe.santos@cesal.edu.br', '5582956789012', 'Especialista em História'),
('Mariana Costa', 40, 'mariana.costa@cesal.edu.br', '5582967890123', 'Mestre em Geografia'),
('Vinicius Rocha', 47, 'vinicius.rocha@cesal.edu.br', '5582978901234', 'Doutor em Filosofia'),
('Letícia Martins', 33, 'leticia.martins@cesal.edu.br', '5582989012345', 'Mestre em Letras'),
('Bruno Ferreira', 39, 'bruno.ferreira@cesal.edu.br', '5582990123456', 'Especialista em Sociologia'),
('Juliana Dias', 36, 'juliana.dias@cesal.edu.br', '5582901234567', 'Mestre em Artes'),
('Lucas Mendes', 41, 'lucas.mendes@cesal.edu.br', '5582912345679', 'Doutor em Psicologia'),
('Camila Barros', 37, 'camila.barros@cesal.edu.br', '5582923456780', 'Mestre em Pedagogia'),
('Gabriel Pinto', 34, 'gabriel.pinto@cesal.edu.br', '5582934567891', 'Especialista em Educação Física'),
('Amanda Ribeiro', 43, 'amanda.ribeiro@cesal.edu.br', '5582945678902', 'Doutora em Química'),
('Thiago Lima', 46, 'thiago.lima@cesal.edu.br', '5582956789013', 'Mestre em Física'),
('Beatriz Gomes', 32, 'beatriz.gomes@cesal.edu.br', '5582967890124', 'Especialista em Informática'),
('Rafael Carvalho', 48, 'rafael.carvalho@cesal.edu.br', '5582978901235', 'Mestre em Engenharia'),
('Isabela Fernandes', 44, 'isabela.fernandes@cesal.edu.br', '5582989012346', 'Doutora em Ciências Sociais'),
('Diego Azevedo', 35, 'diego.azevedo@cesal.edu.br', '5582990123457', 'Mestre em Arquitetura'),
('Larissa Teixeira', 30, 'larissa.teixeira@cesal.edu.br', '5582901234568', 'Especialista em Design'),
('André Castro', 50, 'andre.castro@cesal.edu.br', '5582912345680', 'Mestre em Engenharia Civil'),
('Fernanda Moreira', 49, 'fernanda.moreira@cesal.edu.br', '5582923456781', 'Doutora em Engenharia Elétrica'),
('Pedro Araújo', 39, 'pedro.araujo@cesal.edu.br', '5582934567892', 'Mestre em Administração'),
('Sara Correia', 31, 'sara.correia@cesal.edu.br', '5582945678903', 'Especialista em Contabilidade'),
('Eduardo Nascimento', 42, 'eduardo.nascimento@cesal.edu.br', '5582956789014', 'Mestre em Economia'),
('Luana Figueiredo', 36, 'luana.figueiredo@cesal.edu.br', '5582967890125', 'Doutora em Direito'),
('Fábio Cunha', 33, 'fabio.cunha@cesal.edu.br', '5582978901236', 'Mestre em Logística'),
('Paula Batista', 40, 'paula.batista@cesal.edu.br', '5582989012347', 'Especialista em Recursos Humanos'),
('João Monteiro', 45, 'joao.monteiro@cesal.edu.br', '5582990123458', 'Mestre em Turismo'),
('Cíntia Rezende', 34, 'cintia.rezende@cesal.edu.br', '5582901234569', 'Doutora em Gastronomia'),
('Leandro Peixoto', 37, 'leandro.peixoto@cesal.edu.br', '5582912345681', 'Mestre em Marketing'),
('Priscila Barata', 32, 'priscila.barata@cesal.edu.br', '5582923456782', 'Especialista em Comunicação'),
('Otávio Fonseca', 44, 'otavio.fonseca@cesal.edu.br', '5582934567893', 'Mestre em Relações Internacionais'),
('Vanessa Pires', 41, 'vanessa.pires@cesal.edu.br', '5582945678904', 'Doutora em Ciências Políticas'),
('Henrique Lopes', 38, 'henrique.lopes@cesal.edu.br', '5582956789015', 'Mestre em Logística'),
('Natália Barros', 29, 'natalia.barros@cesal.edu.br', '5582967890126', 'Especialista em Educação Infantil'),
('Rodrigo Brito', 43, 'rodrigo.brito@cesal.edu.br', '5582978901237', 'Mestre em Música'),
('Tatiane Silveira', 40, 'tatiane.silveira@cesal.edu.br', '5582989012348', 'Doutora em Linguística'),
('Murilo Andrade', 39, 'murilo.andrade@cesal.edu.br', '5582990123459', 'Mestre em Filosofia'),
('Kelly Coelho', 31, 'kelly.coelho@cesal.edu.br', '5582901234570', 'Especialista em Teatro'),
('Wesley Guedes', 34, 'wesley.guedes@cesal.edu.br', '5582912345682', 'Mestre em Cinema'),
('Débora Simões', 42, 'debora.simoes@cesal.edu.br', '5582923456783', 'Doutora em Antropologia'),
('Samuel Prado', 36, 'samuel.prado@cesal.edu.br', '5582934567894', 'Mestre em Ciências da Computação'),
('Renata Dias', 33, 'renata.dias@cesal.edu.br', '5582945678905', 'Especialista em Robótica'),
('Douglas Leal', 39, 'douglas.leal@cesal.edu.br', '5582956789016', 'Mestre em Inteligência Artificial'),
('Elaine Moura', 47, 'elaine.moura@cesal.edu.br', '5582967890127', 'Doutora em Bioinformática'),
('Luciano Barros', 38, 'luciano.barros@cesal.edu.br', '5582978901238', 'Mestre em Ciência de Dados'),
('Aline Campos', 35, 'aline.campos@cesal.edu.br', '5582989012349', 'Especialista em Cibersegurança');

INSERT INTO professor_disciplina (ID_professor, ID_disciplina) VALUES
(1, 1),
(15, 1),
(2, 2),
(3, 3),
(14, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(30, 7),
(8, 8),
(9, 9),
(10, 10),
(11, 11),
(12, 12),
(13, 13),
(16, 40),
(17, 14),
(21, 14),
(22, 14),
(18, 15),
(23, 15),
(24, 16),
(25, 17),
(26, 18),
(27, 19),
(39, 19),
(28, 20),
(29, 21),
(30, 22),
(31, 23),
(32, 24),
(33, 25),
(34, 26),
(35, 27),
(36, 28),
(37, 29),
(38, 30),
(39, 31),
(40, 32),
(41, 33),
(42, 34),
(43, 35),
(44, 36),
(45, 37),
(46, 38),
(47, 39),
(48, 40),
(49, 40);

INSERT INTO professor_disciplina (ID_professor, ID_disciplina) VALUES
(1, 1),(2, 1),(44, 1),
(44, 2),
(44, 3),
(44, 4),
(1, 5),(2, 5),(44, 5),
(44, 9),(46, 9),
(44, 10),(46, 10),
(44, 11),(48, 11),
(44, 12),
(44, 13),(49, 13),
(44, 14),
(44, 15),
(3, 17),(4, 17),(17, 17),
(3, 18),(17, 18),
(3, 19),(4, 19),(17, 19),
(30, 21),
(30, 22),
(13, 23),
(6, 24),
(6, 25),
(6, 26),
(6, 27),
(5, 29),(16, 29),
(27, 30),
(28, 31),
(28, 32),(29, 32),
(33, 34),(37, 34),
(33, 35),(37, 35),
(7, 38),
(8, 39),
(9, 40),(41, 40),
(11, 41),
(14, 42),(15, 42),(38, 42),
(14, 43),(38, 43),
(10, 44),
(10, 46),(40, 46),
(1, 47),(2, 47),
(22, 49),
(22, 50),
(22, 51),
(22, 52),
(27, 58),
(11, 60),
(13, 61),
(7, 62),(12, 62),
(12, 63),
(12, 64),
(3, 66),(17, 66),(19, 66),(23, 66),(24, 66),
(19, 67),(23, 67),(24, 67),
(19, 68),(23, 68),(24, 68),
(19, 69),(23, 69),(24, 69),
(24, 70),
(24, 71),
(24, 72),(45, 72),
(44, 73),(45, 73),
(44, 74),(48, 74),
(44, 75),(48, 75),
(44, 76),(46, 76),
(39, 77),(42, 77),(43, 77),
(42, 78),(43, 78),(30, 78),
(42, 79),(43, 79),
(27, 80),
(5, 84),(16, 84),(47, 84),
(6, 85),(47, 85),
(6, 86),
(8, 87),
(8, 88),
(44, 89),(49, 89),
(44, 90),
(44, 91),
(44, 92);

-- disciplinas e professores vinculados a elas

SELECT 
  d.nome_disciplina,
  COALESCE(string_agg(p.nome_professor, ', '), 'Nenhum professor vinculado') AS professor
FROM
  disciplina d
LEFT JOIN
  professor_disciplina pd ON d.id_disciplina = pd.id_disciplina
LEFT JOIN
  professor p ON pd.id_professor = p.id_professor
GROUP BY
  d.id_disciplina, d.nome_disciplina
ORDER BY
  d.nome_disciplina;

-- cursos ordenados por materias que não há professores cadastrados (e na ordem alfabeta de curso)

SELECT 
  d.nome_disciplina,
  COALESCE(string_agg(p.nome_professor, ', '), 'Nenhum professor vinculado') AS professor
FROM
  disciplina d
LEFT JOIN
  professor_disciplina pd ON d.id_disciplina = pd.id_disciplina
LEFT JOIN
  professor p ON pd.id_professor = p.id_professor
GROUP BY
  d.id_disciplina, d.nome_disciplina
ORDER BY
  COUNT(p.id_professor) ASC,
  d.nome_disciplina;

-- nome do curso com total de disciplinas vinculadas

SELECT 
    c.nome_curso AS nome_curso,
    COUNT(cd.ID_disciplina) AS total_disciplinas
FROM 
    curso c
INNER JOIN 
    curso_disciplina cd ON c.ID_curso = cd.ID_curso
GROUP BY 
    c.nome_curso 
ORDER BY 
    total_disciplinas DESC;


--pesquisar disciplina

SELECT 
    d.nome_disciplina,
    c.nome_curso AS nome_curso
FROM 
    disciplina d
INNER JOIN 
    curso_disciplina cd ON d.ID_disciplina = cd.ID_disciplina
INNER JOIN 
    curso c ON cd.ID_curso = c.ID_curso
WHERE 
    d.nome_disciplina ILIKE '%humana%'
ORDER BY 
    d.nome_disciplina, c.nome_curso;


-- vizualizar os alunos matriculados em cada curso

SELECT
  c.nome_curso,
  a.nome_aluno,
  a.email_aluno
FROM
  curso c
JOIN
  matricula m ON c.ID_curso = m.ID_curso
JOIN
  aluno a ON m.ID_aluno = a.ID_aluno
ORDER BY
  c.nome_curso, a.nome_aluno;



INSERT INTO aluno (nome_aluno, idade_aluno, email_aluno, endereco_aluno, telefone_aluno) values
('José Juan', 22, 'jose.juan@cesal.edu.br', 'Rua São José nº 23', '5582999999999' ),
('Vinicius Bezerra', 22, 'vinicius.bezerra@cesal.edu.br', 'Rua da Fé nº 237', '5582988888888'),
('Marcelo Ribeiro', 23, 'marcelo.ribeiro@cesal.edu.br', 'Rua Paraíba, nº 458', '5582997654323'),
('Sabrina Costa', 25, 'sabrina.costa@cesal.edu.br', 'Rua Ceará, nº 820', '5582996543218'),
('Lucas Moreira', 19, 'lucas.moreira@cesal.edu.br', 'Rua São Paulo, nº 196', '5582995432117'),
('Jéssica Martins', 18, 'jéssica.martins@cesal.edu.br', 'Rua Pará, nº 702', '5582994321105'),
('Felipe Dias', 24, 'felipe.dias@cesal.edu.br', 'Rua Maranhão, nº 430', '5582993210994'),
('Larissa Almeida', 22, 'larissa.almeida@cesal.edu.br', 'Rua Alagoas, nº 54', '5582992109883'),
('Bruno Costa', 21, 'bruno.costa@cesal.edu.br', 'Rua Tocantins, nº 342', '5582991098772'),
('Aline Mendes', 20, 'aline.mendes@cesal.edu.br', 'Rua Mato Grosso, nº 763', '5582990987661'),
('Thiago Barbosa', 23, 'thiago.barbosa@cesal.edu.br', 'Rua Rondônia, nº 217', '5582999876549'),
('Renata Cardoso', 25, 'renata.cardoso@cesal.edu.br', 'Rua Bahia, nº 389', '5582998765437'),
('Gustavo Rocha', 19, 'gustavo.rocha@cesal.edu.br', 'Rua Minas Gerais, nº 520', '5582997654320'),
('Juliana Lima', 18, 'juliana.lima@cesal.edu.br', 'Rua Amazonas, nº 431', '5582996543220'),
('Rafael Gomes', 24, 'rafael.gomes@cesal.edu.br', 'Rua Goiás, nº 642', '5582995432121'),
('Fernanda Ribeiro', 22, 'fernanda.ribeiro@cesal.edu.br', 'Rua Paraíba, nº 789', '5582994321092'),
('Eduardo Costa', 21, 'eduardo.costa@cesal.edu.br', 'Rua Ceará, nº 387', '5582993210998'),
('Carolina Rocha', 20, 'carolina.rocha@cesal.edu.br', 'Rua São Paulo, nº 195', '5582992109887'),
('Marcelo Silva', 23, 'marcelo.silva@cesal.edu.br', 'Rua Pará, nº 431', '5582991098779'),
('Sabrina Almeida', 25, 'sabrina.almeida@cesal.edu.br', 'Rua Maranhão, nº 572', '5582990987652'),
('Lucas Barbosa', 19, 'lucas.barbosa@cesal.edu.br', 'Rua Alagoas, nº 765', '5582999876548'),
('Jéssica Cardoso', 18, 'jéssica.cardoso2@cesal.edu.br', 'Rua Tocantins, nº 489', '5582998765435'),
('Felipe Costa', 24, 'felipe.costa@cesal.edu.br', 'Rua Mato Grosso, nº 643', '5582997654326'),
('Larissa Mendes', 22, 'larissa.mendes@cesal.edu.br', 'Rua Rondônia, nº 209', '5582996543219'),
('Bruno Ribeiro', 21, 'bruno.ribeiro@cesal.edu.br', 'Rua Bahia, nº 511', '5582995432119'),
('Aline Rocha', 20, 'aline.rocha@cesal.edu.br', 'Rua Minas Gerais, nº 874', '5582994321107'),
('Thiago Gomes', 23, 'thiago.gomes@cesal.edu.br', 'Rua Amazonas, nº 264', '5582993210981'),
('Renata Silva', 25, 'renata.silva@cesal.edu.br', 'Rua Goiás, nº 337', '5582992109874'),
('Gustavo Almeida', 19, 'gustavo.almeida@cesal.edu.br', 'Rua Paraíba, nº 198', '5582991098761'),
('Juliana Cardoso', 18, 'juliana.cardoso@cesal.edu.br', 'Rua Ceará, nº 690', '5582990987653'),
('Rafael Rocha', 24, 'rafael.rocha@cesal.edu.br', 'Rua São Paulo, nº 219', '5582999876541'),
('Fernanda Silva', 22, 'fernanda.silva@cesal.edu.br', 'Rua Pará, nº 406', '5582998765436'),
('Eduardo Mendes', 21, 'eduardo.mendes@cesal.edu.br', 'Rua Maranhão, nº 817', '5582997654328'),
('Carolina Cardoso', 20, 'carolina.cardoso@cesal.edu.br', 'Rua Alagoas, nº 245', '5582996543216'),
('Marcelo Costa', 23, 'marcelo.costa@cesal.edu.br', 'Rua Tocantins, nº 584', '5582995432124'),
('Sabrina Mendes', 25, 'sabrina.mendes@cesal.edu.br', 'Rua Mato Grosso, nº 739', '5582994321109'),
('Lucas Rocha', 19, 'lucas.rocha@cesal.edu.br', 'Rua Rondônia, nº 973', '5582993210997'),
('Jéssica Silva', 18, 'jéssica.silva@cesal.edu.br', 'Rua Bahia, nº 154', '5582992109885'),
('Felipe Gomes', 24, 'felipe.gomes@cesal.edu.br', 'Rua Minas Gerais, nº 619', '5582991098773'),
('Larissa Costa', 22, 'larissa.costa@cesal.edu.br', 'Rua Amazonas, nº 782', '5582990987664'),
('Bruno Almeida', 21, 'bruno.almeida@cesal.edu.br', 'Rua Goiás, nº 305', '5582999876540'),
('Aline Cardoso', 20, 'aline.cardoso@cesal.edu.br', 'Rua Paraíba, nº 472', '5582998765438'),
('Thiago Costa', 23, 'thiago.costa@cesal.edu.br', 'Rua Ceará, nº 159', '5582997654327'),
('Renata Mendes', 25, 'renata.mendes@cesal.edu.br', 'Rua São Paulo, nº 846', '5582996543212'),
('Mariana Silva', 24, 'mariana.silva@cesal.edu.br', 'Rua das Flores, nº 278', '8182998123456'),
('Lucas Oliveira', 22, 'lucas.oliveira@cesal.edu.br', 'Avenida Paulista, nº 1552', '7582997123467'),
('Ana Pereira', 21, 'ana.pereira@cesal.edu.br', 'Rua das Acácias, nº 340', '8182996345789'),
('Rafael Souza', 20, 'rafael.souza@cesal.edu.br', 'Rua José Bonifácio, nº 89', '7582995432167'),
('Camila Rodrigues', 23, 'camila.rodrigues@cesal.edu.br', 'Rua Dom Pedro II, nº 432', '8182999876543'),
('Bruno Fernandes', 25, 'bruno.fernandes@cesal.edu.br', 'Rua Santa Catarina, nº 982', '7582998765431'),
('Fernanda Costa', 19, 'fernanda.costa@cesal.edu.br', 'Rua Marechal Deodoro, nº 120', '8182997654322'),
('Pedro Almeida', 18, 'pedro.almeida@cesal.edu.br', 'Rua XV de Novembro, nº 551', '7582996543213'),
('Juliana Santos', 24, 'juliana.santos@cesal.edu.br', 'Rua Bahia, nº 774', '8182995432108'),
('Gustavo Lima', 22, 'gustavo.lima@cesal.edu.br', 'Rua Tiradentes, nº 415', '7582994321097'),
('Letícia Martins', 21, 'letícia.martins@cesal.edu.br', 'Rua do Comércio, nº 99', '8182993210986'),
('Thiago Ribeiro', 20, 'thiago.ribeiro@cesal.edu.br', 'Rua Sete de Setembro, nº 387', '7582992109875'),
('Patrícia Carvalho', 23, 'patrícia.carvalho@cesal.edu.br', 'Rua Santos Dumont, nº 265', '8182991098764'),
('Felipe Rocha', 25, 'felipe.rocha@cesal.edu.br', 'Rua Marechal Floriano, nº 1003', '7582990987653'),
('Amanda Vieira', 19, 'amanda.vieira@cesal.edu.br', 'Rua Amazonas, nº 623', '8182999876542');

INSERT INTO matricula (ID_aluno, ID_curso) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(11, 1),
(12, 2),
(13, 3),
(14, 4),
(15, 5),
(16, 6),
(17, 7),
(18, 8),
(19, 9),
(20, 10),
(21, 11),
(22, 12),
(23, 13),
(24, 14),
(25, 15),
(26, 16),
(27, 17),
(28, 18),
(29, 19),
(30, 20),
(31, 21),
(32, 22),
(33, 23),
(34, 24),
(35, 25),
(36, 26),
(37, 27),
(38, 28),
(39, 29),
(40, 30),
(41, 31),
(42, 32),
(43, 33),
(44, 34),
(45, 35),
(46, 36),
(47, 37),
(48, 38),
(49, 39),
(50, 40),
(51, 41),
(52, 42),
(53, 43),
(54, 44),
(55, 45),
(56, 46),
(57, 47),
(58, 1),
(59, 2);


SELECT
    c.nome_curso AS Curso,
    d.nome_disciplina AS Disciplina
FROM
    curso AS c
JOIN
    curso_disciplina AS cd ON c.ID_curso = cd.ID_curso
JOIN
    disciplina AS d ON cd.ID_disciplina = d.ID_disciplina
ORDER BY
    c.nome_curso, d.nome_disciplina;








SELECT
    a.nome_aluno AS Aluno,
    c.nome_curso AS Curso,
    d.nome_disciplina AS Disciplina,
    -- Usa string_agg para listar múltiplos professores se uma disciplina tiver mais de um
    COALESCE(string_agg(p.nome_professor, ', ') FILTER (WHERE p.nome_professor IS NOT NULL), 'Nenhum Professor Designado') AS Professor
FROM
    aluno AS a
JOIN
    matricula AS m ON a.id_aluno = m.id_aluno
JOIN
    curso AS c ON m.id_curso = c.id_curso
JOIN
    curso_disciplina AS cd ON c.id_curso = cd.id_curso
JOIN
    disciplina AS d ON cd.id_disciplina = d.id_disciplina
LEFT JOIN
    professor_disciplina AS pd ON d.id_disciplina = pd.id_disciplina
LEFT JOIN
    professor AS p ON pd.id_professor = p.id_professor
GROUP BY
    a.id_aluno, a.nome_aluno, c.id_curso, c.nome_curso, d.id_disciplina, d.nome_disciplina
ORDER BY
    a.nome_aluno, c.nome_curso, d.nome_disciplina;


SELECT
    C.nome_curso AS Curso,
    A.nome_aluno AS Aluno,
    D.nome_disciplina AS Disciplina
FROM
    curso AS C
INNER JOIN
    matricula AS M ON C.ID_curso = M.ID_curso
INNER JOIN
    aluno AS A ON M.ID_aluno = A.ID_aluno
INNER JOIN
    curso_disciplina AS CD ON C.ID_curso = CD.ID_curso
INNER JOIN
    disciplina AS D ON CD.ID_disciplina = D.ID_disciplina
ORDER BY
    C.nome_curso, A.nome_aluno, D.nome_disciplina;

