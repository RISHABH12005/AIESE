## Task 1 — API Endpoint Testing

### Objective

Test the specified JSONPlaceholder GET endpoints in Postman, verify that each request returns a successful response, and inspect three fields in each response.

### API Endpoints and Observations

| Endpoint | Status | Three fields observed |
|---|---|---|
| `GET /users/2` | `200 OK` | `id: 2`, `name: "Ervin Howell"`, `email: "Shanna@melissa.tv"` |
| `GET /comments/5` | `200 OK` | `postId: 1`, `id: 5`, `name: " vero eaque aliquid doloribus et culpa"` |
| `GET /todos/3` | `200 OK` | `userId: 1`, `id: 3`, `title: "fugiat veniam minus"` |

### Test Procedure

1. Open Postman and create a new request.
2. Select the **GET** method.
3. Enter the endpoint using the base URL `https://jsonplaceholder.typicode.com`.
4. Click **Send** and verify that the response status is `200 OK`.
5. Inspect the JSON response and record the three fields listed in the table.
6. Repeat the procedure for all three endpoints.

### Expected Result

All three endpoints should return **HTTP 200 OK** with a valid JSON object containing the requested resource data. The observed fields should match the endpoint responses.

### Conclusion

All three GET endpoints are expected to return successful responses. The response fields confirm that the API provides user, comment, and to-do resource data for the requested IDs.

---

## Task 5 — Software Quality Assurance (SQA)

### API Endpoint Tested

`GET https://jsonplaceholder.typicode.com/todos/4`

### Test Report

| Report Item | Student Response |
|---|---|
| **Endpoint tested** | `GET /todos/4` |
| **Expected result** | HTTP 200 OK with a valid JSON response containing an `id`, a non-empty `title`, and a Boolean `completed` field. The returned ID should be 4. |
| **Actual result** | HTTP 200 OK. The API returned valid JSON data with ID 4 and all expected fields. However, only 4 out of 5 automated tests passed. |
| **Test status** | FAIL — 4/5 tests passed |
| **Issue identified** | The ID assertion in the test script expected ID 3 instead of ID 4. The API response was correct, but the test assertion was incorrect. |
| **Suggested improvement** | Correct the assertion from `pm.expect(jsonData.id).to.eql(3)` to `pm.expect(jsonData.id).to.eql(4)`. Alternatively, dynamically validate the returned ID against the requested endpoint. |

### Automated Test Script

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

pm.test("Returned ID is 4", function () {
    pm.expect(jsonData.id).to.eql(4);
});
```

### Conclusion

The API endpoint is functioning correctly and returns the expected response. The test failure was caused by an incorrect ID assertion in the automated test script rather than an API defect. After correcting the assertion, all five automated tests should pass.
