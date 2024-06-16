from .Database import Database


class DataRepository:
    @staticmethod
    def json_or_formdata(request):
        if request.method != 'GET' and request.content_type == 'application/json':
            gegevens = request.get_json()
        else:
            gegevens = request.form.to_dict()
        return gegevens

    # ------------------------------ #
    #  - - - - - VOORBEELD - - - - - #

    @staticmethod
    def read_status_lampen():
        sql = "SELECT * from lampen"
        return Database.get_rows(sql)

    @staticmethod
    def read_status_lamp_by_id(id):
        sql = "SELECT * from lampen WHERE id = %s"
        params = [id]
        return Database.get_one_row(sql, params)

    @staticmethod
    def update_status_lamp(id, status):
        sql = "UPDATE lampen SET status = %s WHERE id = %s"
        params = [status, id]
        return Database.execute_sql(sql, params)

    @staticmethod
    def update_status_alle_lampen(status):
        sql = "UPDATE lampen SET status = %s"
        params = [status]
        return Database.execute_sql(sql, params)

    @staticmethod
    def insert_temperature(temp):
        sql = "INSERT INTO logtemp (dateTime, tempInC) VALUES (NOW(), %s)"
        params = [temp]
        return Database.execute_sql(sql, params)
    
    # ------------------------------ #
    #  - - - - - COCKTAILS - - - - - #

    @staticmethod
    def read_all_cocktails():
        sql = "SELECT c.*, i1.strName as ingredient, ifnull(i2.strName,'') as ingredient, ifnull(i3.strName,'') as ingredient, ifnull(i4.strName, '') as ingredient FROM tblcocktails c LEFT JOIN tblcocktailrecipes r ON c.idDrink = r.idCocktail LEFT JOIN tblingredients i1 ON r.idIngredient1 = i1.id LEFT JOIN tblingredients i2 ON r.idIngredient2 = i2.id LEFT JOIN tblingredients i3 ON r.idIngredient3 = i3.id LEFT JOIN tblingredients i4 ON r.idIngredient4 = i4.id"
        return Database.get_rows(sql)
    
    @staticmethod
    def read_possible_cocktails(ingredient1, ingredient2, ingredient3, ingredient4):
        sql = "SELECT c.*, i1.strName as ingredient, ifnull(i2.strName,'') as ingredient, ifnull(i3.strName,'') as ingredient, ifnull(i4.strName, '') as ingredient FROM tblcocktails c LEFT JOIN tblcocktailrecipes r ON c.idDrink = r.idCocktail LEFT JOIN tblingredients i1 ON r.idIngredient1 = i1.id LEFT JOIN tblingredients i2 ON r.idIngredient2 = i2.id LEFT JOIN tblingredients i3 ON r.idIngredient3 = i3.id LEFT JOIN tblingredients i4 ON r.idIngredient4 = i4.id LEFT JOIN tblingredientcategories cat1 ON i1.categoryID = cat1.id LEFT JOIN tblingredientcategories cat2 ON i2.categoryID = cat2.id LEFT JOIN tblingredientcategories cat3 ON i3.categoryID = cat3.id LEFT JOIN tblingredientcategories cat4 ON i4.categoryID = cat4.id WHERE (cat1.id IN (%s) OR cat1.id IN (SELECT id FROM tblingredientcategories where isOnMachine = 0)) AND (cat2.id IN (%s) OR cat2.id IN (SELECT id FROM tblingredientcategories where isOnMachine = 0)) AND (cat3.id IN (%s) OR cat3.id IN (SELECT id FROM tblingredientcategories where isOnMachine = 0)) AND (cat4.id IN (%s) OR cat4.id IN (SELECT id FROM tblingredientcategories where isOnMachine = 0));"
        params = f"{ingredient1},{ingredient2},{ingredient3},{ingredient4}"
        return Database.get_rows(sql, params)

    @staticmethod
    def read_cocktail_by_id(id):
        sql = "SELECT c.*, i1.strName as ingredient, ifnull(i2.strName,'') as ingredient, ifnull(i3.strName,'') as ingredient, ifnull(i4.strName, '') as ingredient FROM tblcocktails c LEFT JOIN tblcocktailrecipes r ON c.idDrink = r.idCocktail LEFT JOIN tblingredients i1 ON r.idIngredient1 = i1.id LEFT JOIN tblingredients i2 ON r.idIngredient2 = i2.id LEFT JOIN tblingredients i3 ON r.idIngredient3 = i3.id LEFT JOIN tblingredients i4 ON r.idIngredient4 = i4.id WHERE c.idDrink = %s"
        params = [id]
        return Database.get_one_row(sql, params)
    
    @staticmethod
    def read_ingredients():
        sql = "SELECT i.strName AS ingredient_name, cat.strCategory AS category_name, i.picture AS ingredient_picture FROM tblingredients i JOIN tblingredientcategories cat ON i.categoryID = cat.id;"
        return Database.get_rows(sql)
