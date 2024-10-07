init -1 python:

    def mountain_dew(Owner):
        name = "mountain dew"
        string = "mountain_dew"

        criteria = []

        shop_type = "gift"
        filter_type = "gifts"

        description = "A gorgeous bottle of Mountain Dew !!!"
        
        price = 8
        
        return ItemClass(
            Owner, 
            name, string,
            criteria,
            shop_type, 
            filter_type,
            description,
            price = int(price))

