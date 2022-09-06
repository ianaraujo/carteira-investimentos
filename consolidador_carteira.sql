SELECT codigo_negociacao, SUM(quantidade) AS quantidade
FROM tb_negociacoes
GROUP BY codigo_negociacao


