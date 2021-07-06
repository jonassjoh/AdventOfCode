class Field:
    def __init__(self, name, range1, range2):
        self.r1 = tuple(map(int, range1))
        self.r2 = tuple(map(int, range2))
        self.name = name

    def valid(self, x):
        return self.r1[0] <= x <= self.r1[1] or self.r2[0] <= x <= self.r2[1]

class Ticket:
    def __init__(self, values):
        self.values = values
        self.invalid = None

    def valid(self, fields):
        for value in self.values:
            def inner():
                for field in fields:
                    if field.valid(value):
                        return True
                return False
            if not inner():
                self.invalid = value
                return False
        return True

def solve(tickets, fields):
    field_names = [field.name for field in fields]
    field_order = { i: [name for name in field_names] for i in range(len(field_names)) }

    for ticket in tickets:
        for i, value in enumerate(ticket.values):
            for field in fields:
                if not field.valid(value):
                    field_order[i].remove(field.name)

    redo = True
    while redo:
        redo = False
        for k, v in field_order.items():
            if len(v) == 1:
                v = v[0]
                for k2 in field_order:
                    if k2 != k and v in field_order[k2]:
                        field_order[k2].remove(v)
                        redo = True

    return { k: v[0] for k, v in field_order.items() }

with open('input', 'r') as f:
    fields = []
    while (line := f.readline().strip()) and line != "":
        name, ranges = line.split(': ')
        ranges = [r.split('-') for r in ranges.split(' or ')]
        field = Field(name, *ranges)
        fields.append(field)

    f.readline()
    my_ticket = Ticket(list(map(int, f.readline().split(','))))
    f.readline()
    f.readline()

    error_rate = 0

    valid_tickets = []

    while (line := f.readline().strip()) and line != "":
        line = line.split(',')
        ticket = Ticket(list(map(int, line)))
        if not ticket.valid(fields):
            error_rate += ticket.invalid
        else:
            valid_tickets.append(ticket)

    field_order = solve(valid_tickets, fields)
    part2 = 1
    for k, v in field_order.items():
        if v.startswith('departure'):
            part2 *= my_ticket.values[k]

    print(f"The ticket scanning error rate is {error_rate}.")
    print(f"Multiplying the six values on my ticket gives {part2}.")
