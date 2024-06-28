from .Database import Database


class DataRepository:
    @staticmethod
    def json_or_formdata(request):
        if request.method != 'GET' and request.content_type == 'application/json':
            gegevens = request.get_json()
        else:
            gegevens = request.form.to_dict()
        return gegevens

    # ------------------------------- #
    #  - - - - - - READ - - - - - - - #

    @staticmethod
    def read_all_cocktails():
        sql = "SELECT c.*, d.strCategory as strDrinkType, i1.strName as ingredient1, ifnull(i2.strName,'') as ingredient2, ifnull(i3.strName,'') as ingredient3, ifnull(i4.strName, '') as ingredient4 FROM tblcocktails c LEFT JOIN tblcocktailrecipes r ON c.idDrink = r.idCocktail LEFT JOIN tblingredients i1 ON r.idIngredient1 = i1.id LEFT JOIN tblingredients i2 ON r.idIngredient2 = i2.id LEFT JOIN tblingredients i3 ON r.idIngredient3 = i3.id LEFT JOIN tblingredients i4 ON r.idIngredient4 = i4.id LEFT JOIN tbldrinktype d ON c.idDrinkType = d.id"
        return Database.get_rows(sql)

    @staticmethod
    def read_possible_cocktails(ingredient1, ingredient2, ingredient3, ingredient4):
        sql = "SELECT c.*, d.strCategory as strDrinkType, i1.strName as ingredient1, ifnull(i2.strName,'') as ingredient2, ifnull(i3.strName,'') as ingredient3, ifnull(i4.strName, '') as ingredient4 FROM tblcocktails c LEFT JOIN tblcocktailrecipes r ON c.idDrink = r.idCocktail LEFT JOIN tblingredients i1 ON r.idIngredient1 = i1.id LEFT JOIN tblingredients i2 ON r.idIngredient2 = i2.id LEFT JOIN tblingredients i3 ON r.idIngredient3 = i3.id LEFT JOIN tblingredients i4 ON r.idIngredient4 = i4.id LEFT JOIN tblingredientcategories cat1 ON i1.categoryID = cat1.id LEFT JOIN tblingredientcategories cat2 ON i2.categoryID = cat2.id LEFT JOIN tblingredientcategories cat3 ON i3.categoryID = cat3.id LEFT JOIN tblingredientcategories cat4 ON i4.categoryID = cat4.id LEFT JOIN tbldrinktype d ON c.idDrinkType = d.id WHERE (cat1.id IN (%s) OR cat1.id IN (SELECT id FROM tblingredientcategories where isOnMachine = 0)) AND (cat2.id IN (%s) OR cat2.id IN (SELECT id FROM tblingredientcategories where isOnMachine = 0)) AND (cat3.id IN (%s) OR cat3.id IN (SELECT id FROM tblingredientcategories where isOnMachine = 0)) AND (cat4.id IN (%s) OR cat4.id IN (SELECT id FROM tblingredientcategories where isOnMachine = 0));"
        params = [ingredient1, ingredient2, ingredient3, ingredient4]
        return Database.get_rows(sql, params)

    @staticmethod
    def read_cocktail_by_id(id):
        sql = "SELECT c.*, i1.strName as ingredient1, ifnull(i2.strName,'') as ingredient2, ifnull(i3.strName,'') as ingredient3, ifnull(i4.strName, '') as ingredient4 FROM tblcocktails c LEFT JOIN tblcocktailrecipes r ON c.idDrink = r.idCocktail LEFT JOIN tblingredients i1 ON r.idIngredient1 = i1.id LEFT JOIN tblingredients i2 ON r.idIngredient2 = i2.id LEFT JOIN tblingredients i3 ON r.idIngredient3 = i3.id LEFT JOIN tblingredients i4 ON r.idIngredient4 = i4.id WHERE c.idDrink = %s"
        params = [id]
        return Database.get_one_row(sql, params)

    @staticmethod
    def read_cocktail_instructions_by_id(id):
        sql = """
        SELECT
            c.strDrink AS name,
            i1.strName AS ingredient_1, r.intAmount1 AS amount_1, ic1.isOnMachine AS is_on_machine_1,
            i2.strName AS ingredient_2, r.intAmount2 AS amount_2, ic2.isOnMachine AS is_on_machine_2,
            i3.strName AS ingredient_3, r.intAmount3 AS amount_3, ic3.isOnMachine AS is_on_machine_3,
            i4.strName AS ingredient_4, r.intAmount4 AS amount_4, ic4.isOnMachine AS is_on_machine_4,
            i5.strName AS ingredient_5, r.intAmount5 AS amount_5, ic5.isOnMachine AS is_on_machine_5,
            i6.strName AS ingredient_6, r.intAmount6 AS amount_6, ic6.isOnMachine AS is_on_machine_6,
            i7.strName AS ingredient_7, r.intAmount7 AS amount_7, ic7.isOnMachine AS is_on_machine_7,
            i8.strName AS ingredient_8, r.intAmount8 AS amount_8, ic8.isOnMachine AS is_on_machine_8,
            i9.strName AS ingredient_9, r.intAmount9 AS amount_9, ic9.isOnMachine AS is_on_machine_9,
            c.intShakeDuration AS shake_duration
        FROM
            tblcocktails c
        LEFT JOIN
            tblcocktailrecipes r ON c.idDrink = r.idCocktail
        LEFT JOIN
            tblingredients i1 ON r.idIngredient1 = i1.id
        LEFT JOIN
            tblingredientcategories ic1 ON i1.categoryID = ic1.id
        LEFT JOIN
            tblingredients i2 ON r.idIngredient2 = i2.id
        LEFT JOIN
            tblingredientcategories ic2 ON i2.categoryID = ic2.id
        LEFT JOIN
            tblingredients i3 ON r.idIngredient3 = i3.id
        LEFT JOIN
            tblingredientcategories ic3 ON i3.categoryID = ic3.id
        LEFT JOIN
            tblingredients i4 ON r.idIngredient4 = i4.id
        LEFT JOIN
            tblingredientcategories ic4 ON i4.categoryID = ic4.id
        LEFT JOIN
            tblingredients i5 ON r.idIngredient5 = i5.id
        LEFT JOIN
            tblingredientcategories ic5 ON i5.categoryID = ic5.id
        LEFT JOIN
            tblingredients i6 ON r.idIngredient6 = i6.id
        LEFT JOIN
            tblingredientcategories ic6 ON i6.categoryID = ic6.id
        LEFT JOIN
            tblingredients i7 ON r.idIngredient7 = i7.id
        LEFT JOIN
            tblingredientcategories ic7 ON i7.categoryID = ic7.id
        LEFT JOIN
            tblingredients i8 ON r.idIngredient8 = i8.id
        LEFT JOIN
            tblingredientcategories ic8 ON i8.categoryID = ic8.id
        LEFT JOIN
            tblingredients i9 ON r.idIngredient9 = i9.id
        LEFT JOIN
            tblingredientcategories ic9 ON i9.categoryID = ic9.id
        WHERE c.idDrink = %s
        """
        params = [id]
        return Database.get_one_row(sql, params)

    @staticmethod
    def read_ingredients():
        sql = "SELECT i.id AS ingredient_id, i.strName AS ingredient_name, cat.strCategory AS category_name, i.picture AS ingredient_picture FROM tblingredients i JOIN tblingredientcategories cat ON i.categoryID = cat.id;"
        return Database.get_rows(sql)

    @staticmethod
    def read_ingredient_by_id(id):
        sql = "SELECT i.strName AS ingredient_name, cat.strCategory AS category_name, i.picture AS ingredient_picture FROM tblingredients i JOIN tblingredientcategories cat ON i.categoryID = cat.id WHERE i.id = %s"
        params = [id]
        return Database.get_one_row(sql, params)

    @staticmethod
    def get_category_by_ingredient_id(ingredient_id):
        sql = "SELECT cat.id as category_id, cat.strCategory AS category_name FROM tblingredients i JOIN tblingredientcategories cat ON i.categoryID = cat.id WHERE i.id = %s"
        params = [ingredient_id]
        return Database.get_one_row(sql, params)

    @staticmethod
    def read_history():
        sql = "SELECT c.strDrink, lo.dateTime from logorder lo join tblcocktails c on lo.cocktailId = c.idDrink limit 10;"
        return Database.get_rows(sql)

    @staticmethod
    def total_cocktails_drunk():
        sql = "SELECT COUNT(*) AS total_cocktails_drunk FROM logorder;"
        return Database.get_one_row(sql)

    @staticmethod
    def total_shaken_time():
        sql = "SELECT SUM(c.intShakeDuration) AS total_time_shaken FROM logorder l JOIN tblcocktails c ON l.cocktailId = c.idDrink;"
        return Database.get_one_row(sql)

    @staticmethod
    def different_ingredients_tasted():
        sql = "SELECT COUNT(DISTINCT i.id) AS different_ingredients_tasted FROM logorder l JOIN tblcocktailrecipes r ON l.cocktailId = r.idCocktail JOIN tblingredients i ON i.id IN (r.idIngredient1, r.idIngredient2, r.idIngredient3, r.idIngredient4, r.idIngredient5, r.idIngredient6, r.idIngredient7, r.idIngredient8, r.idIngredient9);"
        return Database.get_one_row(sql)

    @staticmethod
    def fav_ingredient():
        sql = "SELECT i.strName AS ingredient, COUNT(*) AS times_used FROM tblcocktailrecipes r JOIN tblingredients i ON i.id IN (r.idIngredient1, r.idIngredient2, r.idIngredient3, r.idIngredient4, r.idIngredient5, r.idIngredient6, r.idIngredient7, r.idIngredient8, r.idIngredient9) GROUP BY i.strName ORDER BY times_used DESC LIMIT 1;"
        return Database.get_one_row(sql)

    @staticmethod
    def read_temp_history():
        sql = "SELECT * FROM logtemp LIMIT 10;"
        return Database.get_rows(sql)

    # CREATE

    @staticmethod
    def create_temp_log(temperature):
        sql = "INSERT INTO logtemp (temperature) VALUES (%s);"
        params = [temperature]
        return Database.execute_sql(sql, params)

    @staticmethod
    def create_order_log(cocktail_id):
        sql = "INSERT INTO logorder (cocktailId, scannedColor) VALUES (%s, %s);"
        params = [cocktail_id, "ERROR"]
        return Database.execute_sql(sql, params)

    # UPDATE

    @staticmethod
    def update_order_log(id, color):
        sql = "UPDATE logorder SET scannedColor = %s WHERE id = %s;"
        params = [color, id]
        return Database.execute_sql(sql, params)

    # DELETE

    @staticmethod
    def delete_temp_log():
        sql = "DELETE FROM logtemp;"
        return Database.execute_sql(sql)

    @staticmethod
    def delete_order_log():
        sql = "DELETE FROM logorder;"
        return Database.execute_sql(sql)

    @staticmethod
    def delete_all_logs():
        sql = "DELETE FROM logorder; DELETE FROM logtemp;"
        return Database.execute_sql(sql)