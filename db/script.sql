-- escolaridade definition

CREATE TABLE escolaridade(
	id int primary key,
	descricao varchar(50)
);


-- estado_civil definition

CREATE TABLE estado_civil(
	id int primary key,
	descricao varchar(50)
);


-- parentesco definition

CREATE TABLE parentesco(
	id int primary key,
	descricao varchar(50) not null
);


-- pessoa definition

CREATE TABLE pessoa(
	id int primary key,
	nome varchar(100) not null,
	endereco varchar(255),
	nascimento date,
	telefone varchar(20),
	rg varchar(9),
	cpf varchar(11)
);


-- tipo_auxilio definition

CREATE TABLE tipo_auxilio (
	id INT,
	descricao VARCHAR not null,
	informa_outros BOOLEAN not null,
	CONSTRAINT TIPO_CONTRUCAO_PK PRIMARY KEY (id)
);


-- tipo_contrucao definition

CREATE TABLE tipo_contrucao (
	id INT,
	descricao VARCHAR not null,
	informa_valor BOOLEAN not null,
	CONSTRAINT TIPO_CONTRUCAO_PK PRIMARY KEY (id)
);


-- composicao_familiar definition

CREATE TABLE composicao_familiar (
	id INT,
	pessoa INT NOT NULL,
	sequencia INT NOT NULL,
	nome VARCHAR NOT NULL,
	parentesco INT NOT NULL,
	nascimento DATE,
	estado_civil INT,
	profissao VARCHAR,
	renda_mensal NUMERIC,
	CONSTRAINT COMPOSICAO_FAMILIAR_PK PRIMARY KEY (id),
	CONSTRAINT composicao_familiar_pessoa_FK FOREIGN KEY (pessoa) REFERENCES pessoa(id),
	CONSTRAINT composicao_familiar_parentesco_FK FOREIGN KEY (parentesco) REFERENCES parentesco(id),
	CONSTRAINT composicao_familiar_estado_civil_FK FOREIGN KEY (estado_civil) REFERENCES estado_civil(id)
);

CREATE UNIQUE INDEX composicao_familiar_pessoa_IDX ON composicao_familiar (pessoa,sequencia);


-- entrevistador definition

CREATE TABLE entrevistador (
	id INT,
	pessoa INT NOT NULL,
	ativo BOOLEAN NOT NULL,
	CONSTRAINT ENTREVISTADOR_PK PRIMARY KEY (id),
	CONSTRAINT entrevistador_pessoa_FK FOREIGN KEY (pessoa) REFERENCES pessoa(id)
);

CREATE UNIQUE INDEX entrevistador_pessoa_IDX ON entrevistador (pessoa);


-- habitacao definition

CREATE TABLE habitacao (
	id INT,
	pessoa INT NOT NULL,
	tipo_construcao INT NOT NULL,
	valor NUMERIC,
	CONSTRAINT HABITACAO_PK PRIMARY KEY (id),
	CONSTRAINT habitacao_pessoa_FK FOREIGN KEY (pessoa) REFERENCES pessoa(id),
	CONSTRAINT habitacao_tipo_contrucao_FK FOREIGN KEY (tipo_construcao) REFERENCES tipo_contrucao(id)
);

CREATE UNIQUE INDEX habitacao_pessoa_IDX ON habitacao (pessoa);


-- saude definition

CREATE TABLE saude (
	id INT,
	pessoa INT NOT NULL,
	inss BOOLEAN,
	funeral BOOLEAN,
	outra BOOLEAN,
	descricao VARCHAR,
	CONSTRAINT SAUDE_PK PRIMARY KEY (id),
	CONSTRAINT saude_pessoa_FK FOREIGN KEY (pessoa) REFERENCES pessoa(id)
);

CREATE UNIQUE INDEX saude_pessoa_IDX ON saude (pessoa);


-- auxilio definition

CREATE TABLE auxilio (
	id INT,
	pessoa INT NOT NULL,
	escolaridade INT,
	renda_mensal NUMERIC NOT NULL,
	estado_civil INT,
	tipo_auxilio INT NOT NULL,
	descricao_outros VARCHAR,
	problema_saude VARCHAR,
	diagnostico VARCHAR NOT NULL,
	providencia VARCHAR NOT NULL,
	"data" DATE NOT NULL,
	entrevistador INT NOT NULL,
	observacao TEXT,
	CONSTRAINT AUXILIO_PK PRIMARY KEY (id),
	CONSTRAINT auxilio_entrevistador_FK FOREIGN KEY (entrevistador) REFERENCES entrevistador(id),
	CONSTRAINT auxilio_escolaridade_FK FOREIGN KEY (escolaridade) REFERENCES escolaridade(id),
	CONSTRAINT auxilio_estado_civil_FK FOREIGN KEY (estado_civil) REFERENCES estado_civil(id),
	CONSTRAINT auxilio_pessoa_FK FOREIGN KEY (pessoa) REFERENCES pessoa(id),
	CONSTRAINT auxilio_tipo_auxilio_FK FOREIGN KEY (tipo_auxilio) REFERENCES tipo_auxilio(id)
);

CREATE UNIQUE INDEX auxilio_pessoa_IDX ON auxilio (pessoa);