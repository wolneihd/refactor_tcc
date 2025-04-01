--        analise_ia: str,
--        status: int,
--        tipo: str,
--        timestamp_data_de: int,
--        timestamp_data_ate: int,
--        nome_sobrenome: str,
--        categoria: str,
--        llm_selecionada: int

set @categoria:='atendimento';
set @analise_ia:='positivo';
set @tipo:='text';
set @respondido:=0;
set @timestamp_data_de:=1740787200;
set @timestamp_data_ate:=1743379200;
set @nome_sobrenome:="Wolnei";
set @llm_selecionada:=1;

SELECT 
    mensagens.id,
    mensagens.usuario_id,
    usuarios.nome,
    usuarios.sobrenome,
    mensagens.texto_msg,
    mensagens.timestamp,
    mensagens.tipo_mensagem,
    mensagens.respondido,
    mensagens.nome_imagem,
    mensagens.llm_id,
    mensagens.analise_ia,
    mensagens.categoria,
    mensagens.feedback,
    mensagens.resposta
FROM aplicacao.mensagens
JOIN usuarios ON mensagens.usuario_id = usuarios.id
WHERE 
    (
    mensagens.analise_ia LIKE CONCAT('%', @analise_ia, '%')
    AND mensagens.tipo_mensagem LIKE CONCAT('%', @tipo, '%')
    AND mensagens.respondido LIKE CONCAT('%', @respondido, '%')
    AND mensagens.categoria LIKE CONCAT('%', @categoria, '%')
    AND usuarios.nome LIKE CONCAT('%', @nome_sobrenome, '%')
    AND mensagens.llm_id LIKE CONCAT('%', @llm_selecionada, '%')
    AND mensagens.timestamp between @timestamp_data_de AND @timestamp_data_ate
    );

