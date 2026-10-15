# SMARTWASTE AI
# Waste Segregation and Management System

from datetime import datetime

waste_records = []
issue_reports = []

# Waste disposal guidance
guidance = {
    "1": ("Paper", "Keep paper clean and dry for recycling."),
    "2": ("Plastic", "Follow local plastic recycling rules."),
    "3": ("Metal", "Place recyclable metal cans in the correct bin."),
    "4": ("Organic Waste", "Food scraps may be suitable for composting."),
    "5": ("Glass", "Use a designated glass collection point."),
    "6": ("E-Waste", "Take electronics to an authorised collection centre."),
    "7": ("General Waste", "Use the general waste bin when recycling is unsuitable.")
}


def show_guidance():
    print("\n--- WASTE DISPOSAL GUIDANCE ---")

    for key, value in guidance.items():
        print(key + ". " + value[0] + " - " + value[1])


def sort_waste():
    print("\n--- WASTE SORTING ---")

    item = input("Enter the waste item name: ")

    print("\nSelect the waste category:")

    for key, value in guidance.items():
        print(key + ". " + value[0])

    print("8. Not Sure")

    choice = input("Enter your choice: ")

    if choice in guidance:
        category, advice = guidance[choice]

    elif choice == "8":
        category = "Not Sure"
        advice = "Check local disposal guidelines before disposal."

    else:
        print("Invalid category. Please try again.")
        return

    record = {
        "item": item,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    waste_records.append(record)

    print("\nWaste Record Saved Successfully!")
    print("Item:", item)
    print("Category:", category)
    print("Disposal Advice:", advice)


def report_issue():
    print("\n--- REPORT A BIN ISSUE ---")

    print("1. Overflowing Bin")
    print("2. Missed Collection")
    print("3. Waste Hotspot")
    print("4. Damaged Bin")
    print("5. Other")

    choice = input("Select issue type: ")

    issue_types = {
        "1": "Overflowing Bin",
        "2": "Missed Collection",
        "3": "Waste Hotspot",
        "4": "Damaged Bin",
        "5": "Other"
    }

    if choice not in issue_types:
        print("Invalid issue type.")
        return

    location = input("Enter location: ")
    description = input("Describe the issue: ")

    report = {
        "type": issue_types[choice],
        "location": location,
        "description": description,
        "status": "Open",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    issue_reports.append(report)

    print("\nIssue Report Submitted Successfully!")


def admin_dashboard():
    print("\n--- ADMIN DASHBOARD ---")

    print("Total Waste Records:", len(waste_records))
    print("Total Issue Reports:", len(issue_reports))

    open_issues = sum(
        1 for report in issue_reports
        if report["status"] == "Open"
    )

    print("Open Issues:", open_issues)

    print("\n--- WASTE RECORDS ---")

    if not waste_records:
        print("No waste records available.")

    else:
        for number, record in enumerate(waste_records, start=1):
            print("\nRecord:", number)
            print("Item:", record["item"])
            print("Category:", record["category"])
            print("Date:", record["date"])

    print("\n--- ISSUE REPORTS ---")

    if not issue_reports:
        print("No issue reports available.")

    else:
        for number, report in enumerate(issue_reports, start=1):
            print("\nReport:", number)
            print("Type:", report["type"])
            print("Location:", report["location"])
            print("Description:", report["description"])
            print("Status:", report["status"])
            print("Date:", report["date"])

    if issue_reports:
        print("\n--- UPDATE ISSUE STATUS ---")
        print("Enter 0 to skip.")

        report_number = input("Enter report number to update: ")

        if report_number.isdigit():
            number = int(report_number)

            if 1 <= number <= len(issue_reports):
                print("1. Open")
                print("2. In Review")
                print("3. Resolved")

                status_choice = input("Choose new status: ")

                statuses = {
                    "1": "Open",
                    "2": "In Review",
                    "3": "Resolved"
                }

                if status_choice in statuses:
                    issue_reports[number - 1]["status"] = (
                        statuses[status_choice]
                    )
                    print("Issue status updated successfully!")

                elif status_choice != "0":
                    print("Invalid status choice.")

            elif number != 0:
                print("Invalid report number.")


def main():
    while True:
        print("\n================================")
        print("       SMARTWASTE AI")
        print("================================")

        print("1. Waste Sorting")
        print("2. Disposal Guidance")
        print("3. Report a Bin Issue")
        print("4. Admin Dashboard")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sort_waste()

        elif choice == "2":
            show_guidance()

        elif choice == "3":
            report_issue()

        elif choice == "4":
            admin_dashboard()

        elif choice == "5":
            print("Thank you for using SmartWaste AI!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
