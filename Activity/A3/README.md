# Activity 3: Log Analysis

## Worked Example 1 — Easy

```text
09:00:01 INFO    Student portal started
09:00:05 INFO    Database connected
09:02:10 WARNING High CPU usage: 82%
09:03:15 ERROR   Database connection timeout
09:03:20 ERROR   Student login failed
09:04:00 INFO    Service restarted
```

## Questions and Answers

| Question | Answer |
| --- | --- |
| What warning was recorded? | **High CPU usage: 82%** |
| What was the first error? | **Database connection timeout** |
| Which event happened immediately after the database timeout? | **Student login failed** |
| What could be one possible reason for the login failure? | **Because of Database connection timeout** |

## Worked Explanation

