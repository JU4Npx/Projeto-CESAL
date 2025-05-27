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
--juninho@CESAL.edu.br senha: juninhoCESAL12
