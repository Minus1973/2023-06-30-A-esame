from database.DB_connect import DBConnect
from model.team import Team


class DAO():

    @staticmethod
    # restituisce tutti gli aeroporti
    def getAllYears():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct YEAR 
                    from teams 
                    where year >=1980
                    order by year desc
                """

        cursor.execute(query)

        for row in cursor:
            #non faccio un oggetto perche è un dato primotivo (int)
            result.append(row["YEAR"])

        cursor.close()
        conn.close()
        return result



    #ATTENZIONE: in questo aso particolare i nodi contengono anche altre informazioni per poi fare gli archi.
    #quindi faccio solo una query dei nodi e con essa genero anche gli archi in python
    #potevo però fare la query nodi e query archi più complessa
    @staticmethod
    def getTeams(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        #prendo tutti i campi dell'oggetto, non solo quelli che mi servono
        query = """select t.teamCode, t.name, t.ID, sum(s.salary) as totSalary
                    from appearances a, teams t, salaries s
                    where a.year=%s
                    and s.year=a.year
                    and a.teamID =t.ID
                    and a.playerID = s.playerID 
                    group by t.teamCode
                """
        cursor.execute(query,(year,))

        for row in cursor:
            result.append(Team(**row))

        cursor.close()
        conn.close()
        return result


    # @staticmethod
    # def getSalaryOfTeams(year,idMap):
    #     conn = DBConnect.get_connection()
    #
    #     result = []
    #
    #     cursor = conn.cursor(dictionary=True)
    #     #da questa query prendo id e salario. li mettoo in un dizionario che ha come chiave l'oggetto e come valore il salario
    #     query = """select t.teamCode, t.ID, sum(s.salary) as totSalary
    #                 from appearances a, teams t, salaries s
    #                 where a.year=%s
    #                 and s.year=%s
    #                 and a.teamID =t.ID
    #                 and a.playerID = s.playerID
    #                 group by t.teamCode
    #             """
    #
    #     cursor.execute(query,(year,year))
    #     #
    #     result={}
    #     for row in cursor:
    #         #l'oggetto Connessione è composto da due oggetti aeroporto e il numero di voli
    #         result[idMap[row["ID"]]] = row["totSalary"]
    #
    #     cursor.close()
    #     conn.close()
    #     return result