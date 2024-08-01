"""TEMPORARY PLACEHOLDER DOCSTRING!"""

ADD_CLASS = """
            INSERT INTO classes (name)
            VALUES (%s)
            ON CONFLICT (name) DO NOTHING;
            """

ADD_ORDER = """
            INSERT INTO orders (name, class_id)
            VALUES (
                %s,
                (SELECT id FROM classes WHERE name = %s)
            )
            ON CONFLICT (name) DO NOTHING;
            """

ADD_FAMILY = """
            INSERT INTO families (name, order_id)
            VALUES (
                %s,
                (SELECT id FROM orders WHERE name = %s)
            )
            ON CONFLICT (name) DO NOTHING;
            """

ADD_SPECIES = """
            INSERT INTO species (name, family_id)
            VALUES (
                %s,
                (SELECT id FROM families WHERE name = %s)
            )
            ON CONFLICT (name) DO NOTHING;
            """

ADD_SUBSPECIES = """
            INSERT INTO subspecies (name, species_id)
            VALUES (
                %s,
                (SELECT id FROM species WHERE name = %s)
            );
            """

ADD_ANIMAL = """
            INSERT INTO animals (
                common_name,
                class_id,
                order_id,
                family_id,
                species_id,
                subspecies_id,
                scientific_name,
                conservation_status,
                attributes,
                header_img_url,
                addl_img_urls,
                species_desc,
                subspecies_desc,
                sources
            ) VALUES (
                %s,
                (SELECT id FROM classes WHERE name = %s),
                (SELECT id FROM orders WHERE name = %s),
                (SELECT id FROM families WHERE name = %s),
                (SELECT id FROM species WHERE name = %s),
                (SELECT id FROM subspecies WHERE name = %s),
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            );
            """

GET_ANIMALS = """
            SELECT
                a.id,
                a.common_name,
                c.name AS class_name,
                o.name AS order_name,
                f.name AS family_name,
                s.name AS species_name,
                ss.name AS subspecies_name,
                a.scientific_name,
                a.conservation_status,
                a.attributes,
                a.header_img_url,
                a.addl_img_urls,
                a.species_desc,
                a.subspecies_desc,
                a.sources
            FROM animals a
            JOIN classes c ON a.class_id = c.id
            JOIN orders o ON a.order_id = o.id
            JOIN families f ON a.family_id = f.id
            JOIN species s ON a.species_id = s.id
            LEFT JOIN subspecies ss ON a.subspecies_id = ss.id
            """
            
ADD_MARKER = """
            INSERT INTO markers (
                mid,
                marker_lat_lon,
                marker_location,
                marker_title,
                marker_date_placed,
                marker_placed_by_uid,
                marker_status,
                marker_animal_details,
                marker_stats
            ) VALUES (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            );
            """
            
GET_MARKER = """
            SELECT
                m.mid,
                m.marker_lat_lon,
                m.marker_location,
                m.marker_title,
                m.marker_date_placed,
                m.marker_placed_by_uid, 
                m.marker_status,
                m.marker_animal_details,
                m.marker_stats
            FROM markers m
            WHERE m.mid = %s
            """

ADD_USER = """
            INSERT INTO users (
                uid,
                username,
                email,
                hashed_pw,
                user_stats
            ) VALUES (
                %s,
                %s,
                %s,
                %s,
                %s
            );
            """
            
GET_USER = """
            SELECT
                u.uid,
                u.username,
                u.email,
                u.hashed_pw,
                u.user_stats
            FROM users u
            WHERE u.uid = %s
            """
