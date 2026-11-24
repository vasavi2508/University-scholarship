
# University Scholarship Allocation System

SUBJECTS = ["Python", "Mathematics", "English", "Physics", "Chemistry"]

MIN_MARKS = 40
MIN_ATTENDANCE = 75
MAX_INCOME = 250000


def check_eligibility(applicant):
    reasons = []

    # Check subject-wise minimum marks
    for subject in SUBJECTS:
        if applicant["marks"][subject] < MIN_MARKS:
            reasons.append(subject + " marks below minimum")

    # Check attendance
    if applicant["attendance"] < MIN_ATTENDANCE:
        reasons.append("Attendance below 75%")

    # Check family income
    if applicant["income"] > MAX_INCOME:
        reasons.append("Family income exceeds Rs. 250000")

    return reasons


def calculate_aggregate(marks):
    total = sum(marks.values())
    percentage = total / len(SUBJECTS)
    return total, percentage


def main():
    applicants = []

    n = int(input("Enter number of applicants: "))

    # Collect applicant details
    for i in range(n):
        print("\nEnter details of Applicant", i + 1)

        name = input("Enter applicant name: ")

        marks = {}

        for subject in SUBJECTS:
            marks[subject] = float(
                input("Enter " + subject + " marks: ")
            )

        attendance = float(input("Enter attendance percentage: "))
        income = float(input("Enter annual family income: "))

        total, percentage = calculate_aggregate(marks)

        applicant = {
            "name": name,
            "marks": marks,
            "total": total,
            "percentage": percentage,
            "attendance": attendance,
            "income": income
        }

        applicants.append(applicant)

    # Separate eligible and rejected applicants
    eligible = []
    rejected = []

    for applicant in applicants:
        reasons = check_eligibility(applicant)

        if len(reasons) == 0:
            eligible.append(applicant)
        else:
            rejected.append((applicant, reasons))

    # Rank eligible applicants
    eligible.sort(
        key=lambda x: (
            -x["percentage"],
            -x["attendance"],
            x["income"],
            x["name"].lower()
        )
    )

    # Display eligible applicants
    print("\n========== SCHOLARSHIP RANK LIST ==========")

    if len(eligible) == 0:
        print("No eligible applicants found.")

    else:
        for rank, applicant in enumerate(eligible, start=1):
            print("\nRank:", rank)
            print("Name:", applicant["name"])
            print("Total Marks:", applicant["total"], "/ 500")
            print("Aggregate:", round(applicant["percentage"], 2), "%")
            print("Attendance:", applicant["attendance"], "%")
            print("Annual Income: Rs.", applicant["income"])

    # Display rejected applicants
    print("\n========== REJECTED APPLICANTS ==========")

    if len(rejected) == 0:
        print("No rejected applicants.")

    else:
        for applicant, reasons in rejected:
            print("\nName:", applicant["name"])
            print("Reason(s):")

            for reason in reasons:
                print("-", reason)

    print("\n========== SUMMARY ==========")
    print("Total Applicants:", n)
    print("Eligible Applicants:", len(eligible))
    print("Rejected Applicants:", len(rejected))


# Main program execution
main()
