INSERT INTO 
        {table} (city_coord_lat, city_coord_lon, weather_id,
                    weather_main, weather_desc, weather_icon,
                    base, main_temp, main_pressure, main_humidity,
                    main_temp_min, main_temp_max, main_sea_level,
                    main_grnd_level, wind_speed, wind_deg, clouds_all,
                    rain_1h, rain_3h, dt, sys_type, sys_id, sys_message, 
                    sys_country, sys_sunrise, sys_sunset, city_id, 
                    cod, city_name, snow_1h, snow_3h, main_temp_kf,
                    dt_text, cnt, city_country, city_population, sys_pod
                    )
        VALUES
            ({city_coord_lat}, {city_coord_lon}, {weather_id},
                    '{weather_main}', '{weather_desc}', '{weather_icon}',
                    '{base}', {main_temp}, {main_pressure}, {main_humidity},
                    {main_temp_min}, {main_temp_max}, {main_sea_level},
                    {main_grnd_level}, {wind_speed}, {wind_deg}, {clouds_all},
                    {rain_1h}, {rain_3h}, {dt}, {sys_type}, {sys_id}, {sys_message}, 
                    '{sys_country}', {sys_sunrise}, {sys_sunset}, {city_id}, 
                    {cod}, '{city_name}', {snow_1h}, {snow_3h}, {main_temp_kf},
                    '{dt_text}', {cnt}, '{city_country}', {city_population}, '{sys_pod}')