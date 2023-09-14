# -*- coding:utf-8 -*-
from cx_Oracle import connect


# 권역별 미세+초미세 평균
con = connect("ljh/dlwnsgk0108@195.168.9.65:1521/xe")
cur = con.cursor()
sql = "SELECT sm_MSRRGN_NM,avg(sm_PM10+sm_PM25) FROM seoul_misaemungi group BY sm_MSRRGN_NM order by sm_MSRRGN_NM"


cur.execute(sql)

for misae_nm , misae in cur:
    print(misae_nm, misae)

cur.close()
con.close()





