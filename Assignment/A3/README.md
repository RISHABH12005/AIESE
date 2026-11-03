# Task 1 - API Request and Response Analysis

| Endpoint | Status | Three fields observed |
|---|---|---|
| `GET /users/2` | `200 OK` | `id: 2`, `name: "Ervin Howell"`, `email: "Shanna@melissa.tv"` |
| `GET /comments/5` | `200 OK` | `postId: 1`, `id: 5`, `name: " vero eaque aliquid doloribus et culpa"` |
| `GET /todos/3` | `200 OK` | `userId: 1`, `id: 3`, `title: "fugiat veniam minus"` |

# Task 2 - Automated API Testing

| Result item | Recorded value |
|---|---|
| Number of tests passed | **5** |
| Number of tests failed | **0** |
| Screenshot attached? | **Yes** |

**Endpoint:** `GET https://jsonplaceholder.typicode.com/todos/3`

```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

const jsonData = pm.response.json();

pm.test("Response contains an ID field", function () {
    pm.expect(jsonData).to.have.property("id");
});

pm.test("Title is a non-empty string", function () {
    pm.expect(jsonData.title).to.be.a("string")
        .and.to.have.length.above(0);
});

pm.test("Completed field is Boolean", function () {
    pm.expect(jsonData.completed).to.be.a("boolean");
});

pm.test("Returned ID is 3", function () {
    pm.expect(jsonData.id).to.eql(3);
});
```

# Task 3 - Intelligent Debugging

| Observation item | Result |
|---|---|
| Expected value | `3` |
| Actual value | `4` |
| HTTP response | `200 OK` |
| Test result | **4 passed, 1 failed** |

## Why did the test fail?

The request was sent to `/todos/4`, which correctly returned an object with `id: 4`, but the test script still expected `id: 3`. The ID assertion therefore failed even though the API request itself was successful. The API was not defective; the expected value in the test was incorrect.

## How did you fix it?

I updated the ID assertion to expect `4` instead of `3`.

**Original assertion:**

```javascript
pm.expect(jsonData.id).to.eql(3);
```

**Corrected assertion:**

```javascript
pm.test("Returned ID is 4", function () {
    pm.expect(jsonData.id).to.eql(4);
});
```

# Task 4 - Regression Testing

| Stage | Result | What happened? |
|---|---|---|
| Initial run | **Not verified** | Run both saved requests with the correct expected IDs. Record the collection-run result after checking Postman. |
| Incorrect expected ID | **Not verified** | Change one expected user ID to an incorrect value and run the collection again. The corresponding ID assertion should fail. |
| After correction | **Not verified** | Restore the correct expected ID and rerun the collection to confirm that the tests pass. |

# Task 5 - Software Quality Assurance (SQA)

| Report Item | Student Response |
|---|---|
| **Endpoint tested** | `GET /todos/4` |
| **Expected result** | HTTP 200 OK with a valid JSON response containing an `id`, a non-empty `title`, and a Boolean `completed` field. The returned ID should be 4. |
| **Actual result** | HTTP 200 OK. The API returned valid JSON data with ID 4 and all expected fields. However, only 4 out of 5 automated tests passed. |
| **Test status** | FAIL — 4/5 tests passed |
| **Issue identified** | The ID assertion in the test script expected ID 3 instead of ID 4. The API response was correct, but the test assertion was incorrect. |
| **Suggested improvement** | Correct the assertion from `pm.expect(jsonData.id).to.eql(3)` to `pm.expect(jsonData.id).to.eql(4)`. Alternatively, dynamically validate the returned ID against the requested endpoint. |

---

# Viva Questions and Answers

### 1. What is an API endpoint?

An API endpoint is a specific URL through which a client can access a resource or perform an operation on a server. For example, `GET /users/2` retrieves the user whose ID is 2.

### 2. What is the difference between an API request and a response?

An API request is a message sent by a client to a server asking for data or an operation. An API response is the server's reply, which contains a status code and may include the requested data or an error message.

### 3. What is an assertion in API testing?

An assertion is a condition used to verify whether the actual API response matches the expected result. For example, checking that the response status is `200` or that the returned ID equals `3`.

### 4. Why can a request return 200 OK while a test fails?

HTTP `200 OK` means that the server successfully processed the request. However, a test can still fail if the response data does not match an assertion. For example, the API may return ID `4` while the test incorrectly expects ID `3`.

### 5. How does intelligent debugging help identify the cause of a failure?

Intelligent debugging helps analyze the failed assertion, compare expected and actual values, and identify the root cause of the failure. It helps distinguish between an API problem and an incorrect test script or expectation.

### 6. How is regression testing different from testing a single request?

Testing a single request checks one API request independently. Regression testing runs previously created tests again, often as a collection, to verify that existing functionality continues to work after changes.

### 7. Why is response validation important for software quality?

Response validation ensures that an API returns the correct status, data types, fields, and expected values. It helps detect defects, maintain reliability, and ensure that the API meets its requirements.

---

## Final Submission Requirement

- Completed SQA report and answers to all seven viva questions.
