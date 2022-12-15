CREATE TABLE IF NOT EXISTS estoque(
   produto    TEXT NOT NULL PRIMARY KEY
  ,preco     MONEY NOT NULL
  ,quantidade INT  NOT NULL
);
INSERT INTO mytable(produto,preco,quantidade) VALUES
 ('maça',4,42)
,('pera',3,22)
,('melancia',8,30)
,('queijo',25,60)
,('melao',8,38)
,('manga',8,50)
,('leite',10,70)
,('ovos',10,60)
,('Abacaxi',6,30)
,('agua',2,43)
,('farofa',10,40)
,('goiba',6,50)
,('pitanga',5,45);


