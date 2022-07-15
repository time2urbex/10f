import json
def load_json() -> list:
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)
        return candidates
def format_candidates(candidates):
    """Форматирование списка кандидатов"""
    candidates = load_json()
    result = '<pre>'
    for candidate in candidates:
        result += f"""
            {candidate["name"]}\n
            {candidate["position"]}\n
            {candidate["skills"]}\n
        """
    result += '</pre>'
    return result
def get_all_candidates():
    return load_json()
def get_candidate_by_id():
    candidates = get_all_candidates()
    for candidate in candidates:
        if candidate['id'] == uid:
            return candidate
    return None
def get_candidate_by_skill():
    candidates = get_all_candidates()
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].split(','):
            result.append(candidate)
    return result