# Task 1 - API Request and Response Analysis

| Endpoint | Status | Three fields observed |
|---|---|---|
| `GET /users/2` | `200 OK` | `id: 2`, `name: "Ervin Howell"`, `email: "Shanna@melissa.tv"` |
| `GET /comments/5` | `200 OK` | `postId: 1`, `id: 5`, `name: " vero eaque aliquid doloribus et culpa"` |
| `GET /todos/3` | `200 OK` | `userId: 1`, `id: 3`, `title: "fugiat veniam minus"` |

# Task 2 - Automated API Testing

**Endpoint:** `GET https://jsonplaceholder.typicode.com/todos/3`

### Test conditions

The following five automated tests were added in Postman under **Scripts → After response**:

1. Verify that the HTTP status code is `200`.
2. Verify that the response contains an `id` field.
3. Verify that the `title` is a non-empty string.
4. Verify that the `completed` field is a Boolean value.
5. Verify that the returned `id` is `3`.

### Post-response test script

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

### Record your result

| Result item | Recorded value |
|---|---|
| Number of tests passed | **5** |
| Number of tests failed | **0** |
| Overall result | **PASS** |
| Screenshot attached? | **Yes** |

### Conclusion

All five automated tests passed for the `GET /todos/3` endpoint. The response returned HTTP `200 OK`, contained the required fields, used the expected data types, and returned the expected ID of `3`. The Postman test-results screenshot is attached as evidence.

---

# Task 5 - Software Quality Assurance (SQA)

| Report Item | Student Response |
|---|---|
| **Endpoint tested** | `GET /todos/4` |
| **Expected result** | HTTP 200 OK with a valid JSON response containing an `id`, a non-empty `title`, and a Boolean `completed` field. The returned ID should be 4. |
| **Actual result** | HTTP 200 OK. The API returned valid JSON data with ID 4 and all expected fields. However, only 4 out of 5 automated tests passed. |
| **Test status** | FAIL — 4/5 tests passed |
| **Issue identified** | The ID assertion in the test script expected ID 3 instead of ID 4. The API response was correct, but the test assertion was incorrect. |
| **Suggested improvement** | Correct the assertion from `pm.expect(jsonData.id).to.eql(3)` to `pm.expect(jsonData.id).to.eql(4)`. Alternatively, dynamically validate the returned ID against the requested endpoint. |
