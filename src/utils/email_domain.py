def return_domain_and_orgunit(classroom_description: str) -> tuple:
    if not isinstance(classroom_description, str):
        raise TypeError("A descrição da turma deve ser uma string.")
    
    classroom_description = classroom_description.upper()
    
    # Mapping of substrings to domains and orgunits
    mappings = {
        ("ENF", "PED", "ADM", "ADS", "PSI", "PIS", "DIR"): ("faculdadecci.com.br", "/Faculdade/Turmas Fac"),
        ("TÉC.",): ("tecscci.com.br", "/Escola Técnica/2024")
    }
    
    # Verify the classroom_description and return the domain and orgnuits.
    for keywords, (domain, orgunit) in mappings.items():
        if any(keyword in classroom_description for keyword in keywords):
            return domain, orgunit
    
    return "cciweb.com.br", "/Turmas 2025"
