import pymysql
connection = pymysql.connect(host='pc-bp18rn0tqu85a1600-public.rwlb.rds.aliyuncs.com',
                       port=3306,
                       user='lab_1506359621',
                       passwd='19152398ed17_#@Aa',
                       db='final_pj')
try:
    with connection.cursor() as cursor:
        # 以查询courses表为例

        sql = "SELECT * FROM `courses`"
        cursor.execute(sql)
        for result in cursor:
             # 输出查询结果
             r=[str(s)+(20-len(str(s)))*' ' for s in result]

             print(' '.join(r))

finally:
    connection.close()