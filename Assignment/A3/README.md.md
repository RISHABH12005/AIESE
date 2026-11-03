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