# Testing Postman

## Task 1

**Question:** Change only the URL in Task-1, click Send, and compare the response. How does it differ? Does the users endpoint return the same fields as the posts endpoint? Write down two differences.

---

### Posts endpoint response — `GET /posts/1`

``` json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum..."
}

 ```

### Users endpoint response — `GET /users/1`

``` json
{
  "id": 1,
  "name": "Leanne Graham",
  "username": "Bret",
  "email": "Sincere@april.biz",
  "address": {
    "street": "Kulas Light",
    "suite": "Apt. 556",
    "city": "Gwenborough",
    "zipcode": "92998-3874",
    "geo": { "lat": "-37.3159", "lng": "81.1496" }
  },
  "phone": "1-770-736-8031 x56442",
  "website": "hildegard.org",
  "company": {
    "name": "Romaguera-Crona",
    "catchPhrase": "Multi-layered client-server neural-net",
    "bs": "harness real-time e-markets"
  }
}

 ```

---

### Answer

**1\. Different fields / structure:**  
The posts endpoint returns 4 flat fields (`userId`, `id`, `title`, `body`) focused on written content. The users endpoint returns 8+ fields including deeply nested objects (`address`, `company`). The two responses share **no common fields except** **`id`**.

**2\. No** **`title`****/****`body`** **in users; no** **`name`****/****`email`** **in posts:**  
Posts are **content-focused** — they describe what was written. Users are **identity-focused** — they describe who wrote it (name, contact info, company). To link the two, use the `userId` field from a post to look up the matching user via `/users/{userId}`.

---

## Task 3

**Request:** `GET https://jsonplaceholder.typicode.com/posts/2`

**Test script:**

``` js
pm.test("Post ID is 1", function () {
  const data = pm.response.json();
  pm.expect(data.id).to.eql(1);
});

 ```

---

**Q1: Why can the HTTP status be 200 while a test fails?**  
**Answer:** The HTTP status code `200 OK` only means the server successfully received and responded to the request — it says nothing about the content of the response. A Postman test is a separate assertion written by the developer that checks the response body, headers, or values. The server can return `200` with perfectly valid JSON, but if that JSON doesn't match what the test expects, the test will still fail. Status codes and test assertions are independent of each other.

---

**Q2: What value does the failing test expect?**  
**Answer:** The test expects `data.id` to equal `1` (`pm.expect(data.id).to.eql(1)`).

---

**Q3: What value did the API actually return?**  
**Answer:** The API returned `"id": 2` — because the request hits `/posts/2`, which is post number 2.

``` json
{
  "userId": 1,
  "id": 2,
  "title": "qui est esse",
  "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque..."
}

 ```

---

**Q4: How can you fix the test for** **`/posts/2`****?**  
**Answer:** Update the test assertion to expect `id` to equal `2`, matching the actual post being fetched:

``` js
pm.test("Post ID is 2", function () {
  const data = pm.response.json();
  pm.expect(data.id).to.eql(2);
});

 ```

Alternatively, if the intent is always to test post ID 1, change the URL back to `/posts/1`.

---

## Submission Checklist

- ✓ GET /posts/1 request and response checked
    
- ✓ Four automated tests added and executed
    
- ✓ One intentionally failing test demonstrated
    
- ✓ Failure corrected and retested
    
- ✓ Missing-resource response observed
    
- ✓ POST request sent with JSON body
    
- ✓ POST response tests executed
    
- ✓ Reflection questions completed
    

---

## Viva / Reflection Questions

**1\. What is the difference between GET and POST?**  
**Answer:** GET is used to **retrieve** data from a server — it sends no body and should not change any data. POST is used to **send** data to a server (e.g., create a new resource) — it includes a request body (commonly JSON) and may change server state. GET is idempotent (repeating it has no side effect); POST is not.

---

**2\. What does HTTP status code 200 mean?**  
**Answer:** `200 OK` means the request was received, understood, and processed successfully by the server. It is the standard success response for GET requests and many POST requests.

---

**3\. Does 200 OK guarantee that every field in the response is correct? Explain.**  
**Answer:** No. `200 OK` only confirms that the server responded without an error — it says nothing about the correctness of the data inside the response body. The body could contain wrong values, missing fields, or stale data. That is exactly why we write automated test assertions: to verify the actual content, not just the status code.

---

**4\. What is the purpose of Scripts → After response?**  
**Answer:** The **After response** script (previously called "Tests") runs automatically after a response is received. It is used to write assertions that validate the response — checking status codes, response body values, headers, response time, etc. — and to set variables from the response for use in later requests.

---

**5\. What is an assertion in API testing?**  
**Answer:** An assertion is a statement that checks whether a specific condition is true. In Postman, assertions are written using `pm.expect(...)` inside the After response script. If the condition holds, the test passes; if not, the test fails. For example: `pm.expect(data.id).to.eql(1)` asserts that the `id` field in the response equals `1`.

---

**6\. Why did the Post ID test fail for /posts/2 when the expected ID was 1?**  
**Answer:** The test was written to assert `data.id === 1`, but the request was sent to `/posts/2`, which returns a post with `"id": 2`. The assertion compared the expected value (`1`) against the actual value (`2`) — they did not match, so the test failed. The HTTP status was still `200` because the server responded correctly; only the test logic failed.

---

**7\. What is JSON, and why is it used in APIs?**  
**Answer:** JSON (JavaScript Object Notation) is a lightweight, human-readable data format that represents data as key-value pairs, arrays, and nested objects. It is used in APIs because it is language-independent, easy to parse in virtually every programming language, compact, and widely supported. Most modern REST APIs send and receive data in JSON format.

---

**8\. Why should we inspect both status code and response body?**  
**Answer:** The status code tells us whether the request succeeded or failed at the transport/protocol level (e.g., 200, 404, 500). The response body contains the actual data or error message. A `200` response could still contain incorrect, incomplete, or unexpected data. Inspecting both gives a complete picture: the server responded correctly _and_ the data is what we expect.

---

**9\. Does JSONPlaceholder permanently store a post submitted through POST?**  
**Answer:** No. JSONPlaceholder is a fake/mock REST API used for testing and prototyping. It simulates a successful POST response (returning `201 Created` with the submitted data and a fake `id`), but it does not actually persist any data. If you send a GET request for the newly "created" resource, it will not be found.

---

**10\. What is the difference between a test failure and a network/request failure?**  
**Answer:** A **network/request failure** occurs before a response is received — for example, the server is unreachable, the URL is wrong, or there is a connection timeout. Postman will show an error like "Could not get any response." A **test failure** occurs after a valid response is received — the server responded successfully, but a written assertion did not pass (e.g., the response body did not contain the expected value). One is an infrastructure problem; the other is a data/logic problem.
