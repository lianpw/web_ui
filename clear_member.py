import traceback
import sys
import pymysql


def main():
    # args = sys.argv
    # if len(args) != 2:
    #     print('命令格式有误! 请按照 python xxx.py mid格式执行.')
    #     return
    # if not args[1].isdigit():
    #     print('输入的第二个参数mid不为整数!!')
    #     return
    # mid = int(args[1])
    # print('mid:', mid)

    mid = '1637728644216159'

    conn = pymysql.connect(user='web_user',
                           password='l%meFN!Z88yRgrjz',
                           host='rm-2zeti0v9e6940n93p.mysql.rds.aliyuncs.com',
                           charset='utf8',
                           port=3306)
    cursor = conn.cursor()
    sql1 = f'DELETE FROM wm_interest_center.t_member_interest WHERE member_id = {mid}'
    sql2 = f'DELETE FROM wm_interest_center.t_member_interest_consume WHERE member_id = {mid};'
    sql3 = f'DELETE FROM wm_interest_center.t_member_interest_package WHERE member_id = {mid};'
    sql4 = f'DELETE FROM dushuhui.mh_dsh_sp_log WHERE mid = {mid};'
    sql5 = f'DELETE FROM dushuhui.mh_dsh_memberorder WHERE mid = {mid};'
    try:
        cursor.execute(sql1)
        cursor.execute(sql2)
        cursor.execute(sql3)
        cursor.execute(sql4)
        cursor.execute(sql5)
        conn.commit()
        print('删除数据成功')
    except:
        print(f'删除数据失败:{traceback.format_exc()}')
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


main()