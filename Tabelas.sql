drop TABLE  t_ac_usuario CASCADE CONSTRAINTS;
drop TABLE t_ac_acoes CASCADE CONSTRAINTS;
drop TABLE  t_ac_dicas CASCADE CONSTRAINTS;

CREATE TABLE T_AC_USUARIO (
  id NUMBER(10) generated always as identity NOT NULL ,
  nome VARCHAR2(50) NOT NULL,
  email VARCHAR2(255) NOT NULL,
  senha VARCHAR2(255) NOT NULL,
  nascimento DATE NOT NULL,
  peso NUMBER(5,2) NOT NULL,
  altura NUMBER(3,2) NOT NULL,
  CONSTRAINT PK_T_AC_USUARIO PRIMARY KEY (id),
  CONSTRAINT UQ_T_AC_USUARIO_EMAIL UNIQUE (email)
);

-- Criação da tabela T_AC_ACOES
CREATE TABLE T_AC_ACOES (
  id NUMBER(10) generated always as identity NOT NULL,
  T_AC_USUARIO_id NUMBER(10) NOT NULL,
  score NUMBER(4) NOT NULL,
  descricao VARCHAR2(255) NOT NULL,
  duracao NUMBER(5,2) NOT NULL,
  data DATE NOT NULL,
  CONSTRAINT PK_T_AC_ACOES PRIMARY KEY (id),
  CONSTRAINT FK_T_AC_ACOES_T_AC_USUARIO FOREIGN KEY (T_AC_USUARIO_id) REFERENCES T_AC_USUARIO (id)
);

-- Criação da tabela T_AC_DICAS
CREATE TABLE T_AC_DICAS (
  id NUMBER(10) generated always as identity NOT NULL,
  categoria VARCHAR2(10) NOT NULL,
  texto VARCHAR2(255) NOT NULL,
  CONSTRAINT PK_T_AC_DICAS PRIMARY KEY (id)
);