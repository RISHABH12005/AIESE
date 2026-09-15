# Task 1
## Situation 1 (Hostel Fee Module) :-
### Context :
The Hostel Fee Module calculates student accommodation charges, applies late-payment penalties, records payments, and displays outstanding balances.
### Code/Problem :
The fee-calculation function produces an incorrect total when a student pays late, possibly because the penalty is omitted or applied more than once.
### Task :
Analyse the function, identify the root cause, correct the calculation, and add tests for on-time, late, partial, full, and overpayments.
### Constraints :
Require nonnegative fees, payments, and penalties; apply late penalties once, calculate balances, prevent negatives, handle overpayments, and preserve two-decimal precision.

## Situation 2 (Complaint Management Module):-
### Context :
Complaint management records student reports about hostel services, facilities, and staff, including details needed for tracking updates and effective resolution.
### Code/Problem :
Complaints may accept missing fields, duplicate submissions, invalid statuses, or incorrect resolution updates, causing unreliable records and inconsistent complaint handling.
### Task :
Validate submissions and updates, enforce lifecycle rules, prevent duplicates, assign identifiers, and test valid, invalid, duplicate, and closed-complaint scenarios appropriately.
### Constraints :
Require valid IDs, unique identifiers, nonempty descriptions, supported categories, controlled status transitions, resolution details, duplicate prevention, and clear error handling.

# Task 2
## Prompt 1 :
Generate comprehensive test cases for the `calculateHostelFee()` function, including:
- Normal case
- Boundary case
- Invalid case

For each test case, provide the input and the expected output.

Do not modify the function. First, explain each test case.

## Prompt 2 :
Perform a security audit of the login code.

Identify all potential security vulnerabilities.

For each vulnerability, provide :
- Vulnerability name
- Vulnerable code statement
- Potential security risk
- Recommended mitigation
- Severity: Low, Medium, or High

Do not modify the code. First, provide the complete security analysis.

## Prompt 3 :
Modify this login code to prevent SQL injection.

Use a secure approach such as parameterized queries or prepared statements.

Do not change the intended login functionality. Explain the changes you made and why they prevent the identified vulnerability.

## Prompt 4 :
Analyse the time complexity of this function. Identify the performance bottleneck and explain whether the function can be optimized without changing its behavior.
