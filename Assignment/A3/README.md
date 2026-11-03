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

## Why did the test fail?

The test failed because the request was sent to `/todos/4`, which correctly returned an object with `id: 4`, but the test script still expected `id: 3`. The ID assertion therefore failed even though the API request itself was successful. The API is not defective; the expected value in the test was incorrect.

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

# Task 5 - Software Quality Assurance (SQA)

| Report Item | Student Response |
|---|---|
| **Endpoint tested** | `GET /todos/4` |
| **Expected result** | HTTP 200 OK with a valid JSON response containing an `id`, a non-empty `title`, and a Boolean `completed` field. The returned ID should be 4. |
| **Actual result** | HTTP 200 OK. The API returned valid JSON data with ID 4 and all expected fields. However, only 4 out of 5 automated tests passed. |
| **Test status** | FAIL — 4/5 tests passed |
| **Issue identified** | The ID assertion in the test script expected ID 3 instead of ID 4. The API response was correct, but the test assertion was incorrect. |
| **Suggested improvement** | Correct the assertion from `pm.expect(jsonData.id).to.eql(3)` to `pm.expect(jsonData.id).to.eql(4)`. Alternatively, dynamically validate the returned ID against the requested endpoint. |
