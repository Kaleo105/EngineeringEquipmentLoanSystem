import json
import os

FILE_NAME = "loans.json"

def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME,"r") as f:
                return json.load(f)
        except (json.JSONDecodeError, ValueError):
            return []
    return []

def save_data(loans):
    with open(FILE_NAME,"w") as f:
        json.dump(loans,f,indent=4)

def register_loan(loans):
    print("\n====== REGISTER EQUIPMENT LOAN ======")
    while True:
        sid=input("Student ID: ").strip()
        if sid: break
        print("Student ID cannot be blank.")
    sname=input("Student Name: ").strip()
    prog=input("Programme: ").strip()
    while True:
        equip=input("Equipment Name: ").strip()
        if equip: break
        print("Equipment name cannot be blank.")
    while True:
        try:
            qty=int(input("Quantity Borrowed: "))
            if qty>0: break
            print("Quantity must be greater than zero.")
        except ValueError:
            print("Enter a valid integer.")
    bdate=input("Borrow Date (YYYY-MM-DD): ")
    rdate=input("Expected Return Date (YYYY-MM-DD): ")
    loans.append({
        "student_id":sid,
        "student_name":sname,
        "programme":prog,
        "equipment":equip,
        "quantity":qty,
        "borrow_date":bdate,
        "return_date":rdate,
        "returned":False
    })
    save_data(loans)
    print("Loan registered successfully.")

def view_loans(loans):
    if not loans:
        print("No loan records found."); return
    print(f"{'Student ID':12} {'Name':20} {'Equipment':20} {'Qty':>3} {'Returned'}")
    for l in loans:
        print(f"{l['student_id']:12} {l['student_name'][:20]:20} {l['equipment'][:20]:20} {l['quantity']:>3} {'Yes' if l['returned'] else 'No'}")

def search_student(loans):
    sid=input("Enter Student ID: ").strip()
    for l in loans:
        if l["student_id"]==sid:
            for k,v in l.items():
                print(f"{k}: {v}")
            return
    print("Loan record not found.")

def return_equipment(loans):
    sid=input("Enter Student ID: ").strip()
    for l in loans:
        if l["student_id"]==sid:
            if l["returned"]:
                print("Equipment already returned.")
            else:
                l["returned"]=True
                save_data(loans)
                print("Equipment returned successfully.")
            return
    print("Loan record not found.")

def generate_report(loans):
    total=len(loans)
    qty=sum(l["quantity"] for l in loans)
    returned=sum(1 for l in loans if l["returned"])
    outstanding=total-returned
    counts={}
    for l in loans:
        counts[l["equipment"]]=counts.get(l["equipment"],0)+1
    most=max(counts,key=counts.get) if counts else None
    print("\n====== SUMMARY ======")
    print("Total Loans:",total)
    print("Total Equipment Borrowed:",qty)
    print("Returned Loans:",returned)
    print("Outstanding Loans:",outstanding)
    if most:
        print("Most Borrowed Equipment:")
        print(f"{most} ({counts[most]} loans)")
    else:
        print("No records available.")

def main():
    loans=load_data()
    while True:
        print("\n====== ENGINEERING EQUIPMENT LOAN SYSTEM ======")
        print("1. Register Equipment Loan")
        print("2. View All Loans")
        print("3. Search Loan by Student ID")
        print("4. Return Equipment")
        print("5. Generate Summary Report")
        print("6. Exit")
        ch=input("Choose an option: ")
        if ch=="1": register_loan(loans)
        elif ch=="2": view_loans(loans)
        elif ch=="3": search_student(loans)
        elif ch=="4": return_equipment(loans)
        elif ch=="5": generate_report(loans)
        elif ch=="6":
            print("Thank you for using the Engineering Equipment Loan System.")
            break
        else:
            print("Invalid option.")

if __name__=="__main__":
    main()
