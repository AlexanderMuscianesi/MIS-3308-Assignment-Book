#Problem 4) Help Desk Ticket
import sys
p1_count = 0 
p2_count = 0 
p3_count = 0
# -- INPUT -- 
total_tickets= int(input("How many tickets would you like to create?:"))
if total_tickets <= 0:
    print("Invalid number of tickets.")
    sys.exit()
# -- LOOP --
for i in range(total_tickets):
    print("Entering Ticket",i+1)
    ticket_id = input("Ticket ID ")
    severity = int(input("Severity (1-5): "))
    if 1 >= severity >= 5:
        print("Severity must be between 1 and 5")
    system_down = input("Is the system down? (y/n):")
    # -- SLA Classifications --
    if system_down == "y" or severity == 5:
        priority = "P1"
        sla = "1 hour"
        p1_count += 1
    elif severity in (3,4):
        priority = "P2"
        sla = "24 hours"
        p2_count += 1
    else:
        priority = "P3"
        sla = "72 hours"
        p3_count += 1
    print("Priority:",priority)
    print("Response Time:",sla)
print("Final Report")
print("Total Tickets:",total_tickets)
print("P1 Count:",p1_count)
print("P2 Count:",p2_count)
print("P3 Count:",p3_count)
p1_percent = (p1_count/total_tickets) * 100
print(f"P1 Percent:{p1_percent:.1f}%")
print("End Problem 4")