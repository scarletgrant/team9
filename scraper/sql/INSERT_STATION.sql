INSERT INTO station 
        (id, contract_name, name, pos_lat, pos_lon,
        banking, bonus, status, bike_stands, available_bike_stands,
        available_bikes, last_update, address)

        VALUES (
            {id}, '{contract_name}', '{name}', {pos_lat}, {pos_lon},
            {banking}, {bonus}, '{status}', {bike_stands}, {available_bike_stands},
            {available_bikes}, '{last_update}', '{address}'
        )

        ON CONFLICT (id, contract_name)
        DO NOTHING;