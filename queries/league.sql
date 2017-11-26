select League.id, League.name, Country.name from League join country on (League.country_id = Country.id);
