from database.DB_connect import DBConnect
from model.arco import Arco
from model.prodotto import Prodotto


class DAO():

    @staticmethod
    def getAllNodes(colore):

        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)

        result = []

        query = """select * 
                    from go_products c
                    where c.Product_color = %s
                                    """

        cursor.execute(query, (colore,))

        for row in cursor:
            result.append(Prodotto(**row))

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getAllArchi(idMap,year):

        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """ select gds.Product_number as p1, gds2.Product_number as p2, count(*) as peso
                    from go_daily_sales gds, go_daily_sales gds2
                    where year ( gds.`Date` ) = %s 
                    and gds.Retailer_code = gds2.Retailer_code 
                    and gds2.Product_number > gds.Product_number
                    and gds2.`Date` = gds.`Date` 
                    group by gds.Product_number, gds2.Product_number,gds2.`Date` 
                    order by peso desc 
                                        """

        cursor.execute(query, (year,))

        for row in cursor:
            result.append(Arco(idMap[row["p1"]], idMap[row["p2"]], row["peso"]))

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getAllColori():

        conn = DBConnect.get_connection()
        cursor = conn.cursor()

        result = []

        query = """select gp.Product_color 
                    from go_products gp 
                    group by gp.Product_color 
                                       """

        cursor.execute(query)

        for row in cursor:
            result.append(row[0])

        cursor.close()
        conn.close()

        return result

