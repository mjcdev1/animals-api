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
