CREATE VIEW IF NOT EXISTS vw_carteira_consolidada AS

SELECT codigo_negociacao, 

    SUM(CASE tipo_movimentacao WHEN 'venda' THEN - quantidade ELSE quantidade END) AS quantidade_ajustada,

    ROUND(SUM(quantidade * preco) / SUM(quantidade), 2) AS preco_medio

FROM tb_negociacoes

GROUP BY codigo_negociacao

HAVING quantidade_ajustada > 0;