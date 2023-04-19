class Ticket:
    ticket_count = 0
    open_tickets = 0
    closed_tickets = 0

    def __init__(self, staff_id, ticket_creator, contact_email, description):
        Ticket.ticket_count += 1
        Ticket.open_tickets += 1
        self.ticket_number = Ticket.ticket_count + 2000
        self.staff_id = staff_id
        self.ticket_creator = ticket_creator
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"

    def resolve_password_change(self):
        if "Password Change" in self.description:
            new_password = self.staff_id[:2] + self.ticket_creator[:3]
            self.response = f"New password generated: {new_password} "
            self.status = "Closed"
            Ticket.open_tickets -= 1
            Ticket.closed_tickets += 1
    def resolve_monitor_problems(self):
        if "My monitor stopped working" in self.description:
            solution="The Monitor has been replaced"
            self.response=solution
            self.status="Closed"
            Ticket.open_tickets -= 1
            Ticket.closed_tickets += 1

    def resolve_ticket(self, response):
        self.response = response
        self.status = "Closed"
        Ticket.open_tickets -= 1
        Ticket.closed_tickets += 1

    def reopen_ticket(self):
        self.status = "Reopened"
        Ticket.open_tickets += 1
        Ticket.closed_tickets -= 1

    
    def ticket_stats():
        print("Tickets Created:", Ticket.ticket_count)
        print("Tickets Resolved:", Ticket.closed_tickets)
        print("Tickets To Solve:", Ticket.open_tickets)

    def print_ticket(self):
        print("Ticket Number:", self.ticket_number)
        print("Ticket Creator:", self.ticket_creator)
        print("Staff ID:", self.staff_id)
        print("Email Address:", self.contact_email)
        print("Description:", self.description)
        print("Response:", self.response)
        print("Ticket Status:", self.status)
        

# Submitting Tickets
tickets = []

for i in range(3):
    staff_id = input("Enter Staff ID: ")
    ticket_creator = input("Enter Ticket Creator Name: ")
    contact_email = input("Enter Contact Email: ")
    description = input("Enter Description: ")
    ticket = Ticket(staff_id, ticket_creator, contact_email, description)
    ticket.resolve_password_change()
    tickets.append(ticket)

# Displaying Ticket Statistics
Ticket.ticket_stats()



# Displaying the ticket information and ticket statistics
print("\n\nPrinting Tickets:")
for ticket in tickets:
    print("\n")
    ticket.print_ticket()

# Reopening one of the resolved tickets
tickets[0].reopen_ticket()




# Displaying the ticket information and ticket statistics
print("\n\nPrinting Tickets:")
for ticket in tickets:
    ticket.resolve_monitor_problems()
    print("\n")
    ticket.print_ticket()
    
# Displaying Ticket Statistics
Ticket.ticket_stats()    

