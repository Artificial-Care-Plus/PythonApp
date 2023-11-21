drop TABLE  t_ac_usuario CASCADE CONSTRAINTS;
drop TABLE t_ac_acoes CASCADE CONSTRAINTS;
drop TABLE  t_ac_dicas CASCADE CONSTRAINTS;

CREATE TABLE t_ac_acoes (
    id_acoes                NUMBER(10) generated always as identity NOT NULL,
    score                   NUMBER(4) NOT NULL,
    descricao               VARCHAR2(255) NOT NULL,
    duracao                 NUMBER(5, 2) NOT NULL,
    data                    DATE NOT NULL,
    t_ac_usuario_id_usuario NUMBER(10) NOT NULL
);

ALTER TABLE t_ac_acoes ADD CONSTRAINT t_ac_acoes_pk PRIMARY KEY ( id_acoes );

CREATE TABLE t_ac_dicas (
    id_dicas  NUMBER(10) generated always as identity NOT NULL,
    categoria VARCHAR2(10) NOT NULL,
    texto     VARCHAR2(255) NOT NULL
);

ALTER TABLE t_ac_dicas ADD CONSTRAINT t_ac_dicas_pk PRIMARY KEY ( id_dicas );

CREATE TABLE t_ac_usuario (
    id_usuario NUMBER(10) generated always as identity NOT NULL,
    email      VARCHAR2(255) NOT NULL,
    nome       VARCHAR2(50) NOT NULL,
    senha      VARCHAR2(255) NOT NULL,
    dt_nasc    DATE NOT NULL,
    peso       NUMBER(5, 2) NOT NULL,
    altura     NUMBER(3, 2) NOT NULL
);

ALTER TABLE t_ac_usuario ADD CONSTRAINT t_ac_usuario_pk PRIMARY KEY ( id_usuario );

ALTER TABLE t_ac_usuario ADD CONSTRAINT t_ac_usuario_email_un UNIQUE ( email );

ALTER TABLE t_ac_acoes
    ADD CONSTRAINT t_ac_acoes_t_ac_usuario_fk FOREIGN KEY ( t_ac_usuario_id_usuario )
        REFERENCES t_ac_usuario ( id_usuario );
