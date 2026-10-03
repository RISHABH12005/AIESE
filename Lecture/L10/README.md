# Calculator Test Cases

The calculator reads two integer values: `x` and `y`.

| Test ID | Category | Input (`x y`) | Expected output |
|---|---|---:|---|
| TC01 | Normal | `10 2` | `Sum =12`; `Difference =8`; `Product =20`; `Quotient =5` |
| TC02 | Normal | `7 3` | `Sum =10`; `Difference =4`; `Product =21`; `Quotient =2.33333...` |
| TC03 | Boundary: both values are zero | `0 0` | `Sum =0`; `Difference =0`; `Product =0`; `Cannot divide by zero` |
| TC04 | Boundary: first value is zero | `0 5` | `Sum =5`; `Difference =-5`; `Product =0`; `Quotient =0` |
| TC05 | Boundary: divisor is zero | `5 0` | `Sum =5`; `Difference =5`; `Product =0`; `Cannot divide by zero` |
| TC06 | Boundary: negative values | `-5 -2` | `Sum =-7`; `Difference =-3`; `Product =10`; `Quotient =2.5` |
| TC07 | Invalid: nonnumeric first input | `abc 2` | Input conversion fails; the current program does not provide a defined error message. |
| TC08 | Invalid: nonnumeric second input | `5 xyz` | Input conversion fails; the current program does not provide a defined error message. |
| TC09 | Invalid: missing input | `5` | Input conversion fails; the current program does not provide a defined error message. |

## How to run a test

Compile the program:

```powershell
g++ calculator.cpp -o calculator.exe
```

Run it:

```powershell
.\calculator.exe
```

Enter the input from the test-case table and compare the output with the expected output.

## Note about invalid input

The current program does not validate `std::cin`. For invalid input cases, it should eventually be updated to detect failed input and print a clear message such as `Invalid input`.
