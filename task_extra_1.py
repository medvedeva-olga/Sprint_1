types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
} 
tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
} 

def clean_tickets(tickets):
    used_tickets = []
    result = {}
    for ticket_level in sorted(tickets.keys()):
        tickets_for_level = []
        for ticket in tickets[ticket_level]:
            if ticket not in used_tickets:
                used_tickets.append(ticket)
                tickets_for_level.append(ticket)
        result[ticket_level] = tickets_for_level
    return result

def create_tickets_by_level_name(types, tickets):
    tickets_by_level_name = {}
    cleaned_tickets = clean_tickets(tickets)
    for level, tickets_by_level in cleaned_tickets.items():
        tickets_by_level_name[types[level]] = cleaned_tickets[level]
    return tickets_by_level_name

tickets_by_type = {
    'Блокирующий': ['API_45', 'API_76', 'E2E_4'],
    'Критический': ['UI_19', 'API_65', 'E2E_45'],
    'Значительный': ['E2E_2'],
    'Незначительный': ['E2E_9'],
    'Тривиальный': ['API_61']
} 