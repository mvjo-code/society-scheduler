CREATE TABLE "clientes" (
  "id" integer PRIMARY KEY,
  "nome" varchar,
  "telefone" varchar,
  "endereco_id" integer
);

CREATE TABLE "endereco" (
  "id" integer PRIMARY KEY,
  "cidade" varchar,
  "bairro" varchar,
  "rua" varchar,
  "n_casa" varchar
);

CREATE TABLE "agendamentos" (
  "id" integer PRIMARY KEY,
  "cliente_id" integer,
  "data_hora_inicio" timestamp,
  "data_hora_fim" timestamp,
  "status" varchar
);

ALTER TABLE "agendamentos" ADD FOREIGN KEY ("cliente_id") REFERENCES "clientes" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "clientes" ADD FOREIGN KEY ("endereco_id") REFERENCES "endereco" ("id") DEFERRABLE INITIALLY IMMEDIATE;
