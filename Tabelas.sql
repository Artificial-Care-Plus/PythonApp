

CREATE TABLE t_ac_acoes (
    id_acoes                NUMBER(10) NOT NULL,
    score                   NUMBER(4) NOT NULL,
    descricao               VARCHAR2(255) NOT NULL,
    duracao                 NUMBER(5, 2) NOT NULL,
    data                    DATE NOT NULL,
    t_ac_usuario_id_usuario NUMBER(10) NOT NULL
);

ALTER TABLE t_ac_acoes ADD CONSTRAINT t_ac_acoes_pk PRIMARY KEY ( id_acoes );

CREATE TABLE t_ac_dicas (
    id_dicas  NUMBER(10) NOT NULL,
    categoria VARCHAR2(10) NOT NULL,
    texto     VARCHAR2(255) NOT NULL
);

ALTER TABLE t_ac_dicas ADD CONSTRAINT t_ac_dicas_pk PRIMARY KEY ( id_dicas );

CREATE TABLE t_ac_usuario (
    id_usuario NUMBER(10) NOT NULL,
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



-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             3
-- CREATE INDEX                             0
-- ALTER TABLE                              5
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0