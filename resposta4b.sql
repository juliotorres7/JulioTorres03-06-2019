select tb_est.nm_est, tb_est.id_est, sum(tb_trn.vl_trn)
from tb_est
join tb_trn on tb_est.id_est = tb_trn.id_est
group by tb_est.id_est;
