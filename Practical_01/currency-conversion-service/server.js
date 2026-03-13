const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

app.use(bodyParser.json());

// This single endpoint handles both Currency and Temperature based on the input key
app.post('/convert', (req, res) => {
    // 1. Currency Conversion (Slip 1)
    if (req.body.amount_in_rs !== undefined) {
        const amountInRs = req.body.amount_in_rs;
        const amountInUsd = amountInRs / 75;
        return res.json({ amount_in_usd: amountInUsd });
    }

    // 2. Temperature Conversion (Slip 2)
    if (req.body.fahrenheit !== undefined) {
        const fahrenheit = req.body.fahrenheit;
        const celsius = (fahrenheit - 32) * 5 / 9;
        return res.json({ celsius: celsius });
    }

    // 3. Factorial (Slip 3)
    if (req.body.number_for_factorial !== undefined) {
        let n = req.body.number_for_factorial;
        let fact = 1;
        for (let i = 1; i <= n; i++) fact *= i;
        return res.json({ factorial: fact });
    }

    // 4. Prime Number (Slip 4)
    if (req.body.number_to_check_prime !== undefined) {
        let n = req.body.number_to_check_prime;
        let isPrime = n > 1;
        for (let i = 2; i <= Math.sqrt(n); i++) {
            if (n % i === 0) { isPrime = false; break; }
        }
        return res.json({ is_prime: isPrime });
    }

    res.status(400).json({ error: "Invalid request parameters" });
});

app.listen(port, () => {
    console.log(`Web services running on http://localhost:${port}`);
    console.log("Supported inputs: amount_in_rs, fahrenheit, number_for_factorial, number_to_check_prime");
});
