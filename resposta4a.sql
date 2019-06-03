select tb_cli.nm_cli, tb_cli.id_cli, sum(tb_trn.vl_trn)
from tb_cli
join tb_trn ontb_cli.id_cli = tb_trn.id_cli
group by tb_cli.id_cli;
