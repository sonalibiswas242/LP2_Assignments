class Ticket:
    def __init__(self, ticket_id, title, description, status):
        self.ticket_id = ticket_id
        self.title = title
        self.description = description
        self.status = status


class Helpdesk:
    def __init__(self):
        self.tickets = []

    def create_ticket(self, ticket_id, title, description):
        ticket = Ticket(ticket_id, title, description, "Open")
        self.tickets.append(ticket)
        print("Ticket created successfully.")

    def view_tickets(self):
        if not self.tickets:
            print("No tickets available.")
        else:
            print("All Tickets:")
            for ticket in self.tickets:
                print(f"Ticket ID: {ticket.ticket_id}")
                print(f"Title: {ticket.title}")
                print(f"Description: {ticket.description}")
                print(f"Status: {ticket.status}")
                print("-------------------------")

    def update_ticket_status(self, ticket_id, status):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                ticket.status = status
                print("Ticket status updated successfully.")
                return
        print("Ticket not found.")

    def delete_ticket(self, ticket_id):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                self.tickets.remove(ticket)
                print("Ticket deleted successfully.")
                return
        print("Ticket not found.")


def menu():
    helpdesk = Helpdesk()
    while True:
        print("\n--- Helpdesk Management System ---")
        print("1. Create a ticket")
        print("2. View all tickets")
        print("3. Update ticket status")
        print("4. Delete a ticket")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            ticket_id = input("Enter ticket ID: ")
            title = input("Enter ticket title: ")
            description = input("Enter ticket description: ")
            helpdesk.create_ticket(ticket_id, title, description)

        elif choice == "2":
            helpdesk.view_tickets()

        elif choice == "3":
            ticket_id = input("Enter ticket ID to update status: ")
            status = input("Enter new status: ")
            helpdesk.update_ticket_status(ticket_id, status)

        elif choice == "4":
            ticket_id = input("Enter ticket ID to delete: ")
            helpdesk.delete_ticket(ticket_id)

        elif choice == "5":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
menu()