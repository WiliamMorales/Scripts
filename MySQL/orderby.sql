use cadastro;
select nome,ano,descricao from cursos
where ano in ('2014','2016','2018')
order by ano;
describe cursos;